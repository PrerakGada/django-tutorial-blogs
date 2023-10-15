from django.urls import path
from .views import Index, DetailArticleView, DeleteArticleView, CreateBlogView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
]