from django.urls import path
from .views import PostListView,PostDetailView,category,search
urlpatterns = [
  path('' ,PostListView.as_view(), name='frontpage'),
  path('search', search, name = 'search'),
  path('<slug:category_slug>/<slug:slug>',PostDetailView.as_view(),name='post_detail'),
  path('<slug:slug>/',category , name='category')

]