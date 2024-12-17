from django.urls import path
from .views import user_feed
from .views import like_post

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
]

from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
urlpatterns += [
    path('protected/', protected_view, name='protected_view'),
]
