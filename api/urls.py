from django.urls import path

from . import views

urlpatterns = [
	path('',views.PostListView.as_view(),name='postlist'),
	path('<int:pk>/',views.DetailView.as_view(),name='DetailView'),
	path('user/',views.UserListView.as_view(),name='UserListView')
]
