from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    """
    Endpoint to fetch posts from followed users.
    """
    user = request.user
    followed_users = user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=200)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    """
    Endpoint to like or unlike a post.
    """
    user = request.user
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)
    
    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        like.delete()
        return Response({"message": "Post unliked", "likes_count": post.like_set.count()}, status=200)
    
    return Response({"message": "Post liked", "likes_count": post.like_set.count()}, status=201)

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class LoginView(APIView):
    """
    Login endpoint to authenticate user and return their token.
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        return Response({"error": "Invalid credentials"}, status=400)
