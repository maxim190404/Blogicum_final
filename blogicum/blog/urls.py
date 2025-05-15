from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, UpdateProfileView, BlogView
from .views import CategoryPostsListView


app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('category/<slug:category_slug>/',
         CategoryPostsListView.as_view(), name='category_posts'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('auth/registration/', views.registration, name='registration'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit_profile/', UpdateProfileView.as_view(), name='edit_profile'),
    path('posts/create/', PostCreateView.as_view(), name='create_post'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='edit_post'),
    path('posts/<int:post_id>/comment/', views.comments_post,
         name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='edit_comment'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='delete_post'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.comment_delete, name='delete_comment'),
]
