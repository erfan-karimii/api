from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateAPIView
from .serilizers import PostSerilizers,UserSerilizers
from .models import Post
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication

class PostListView(ListCreateAPIView):
	queryset = Post.objects.all()
	# serializer_class = PostSerilizers
	authentication_classes =(SessionAuthentication,)


class DetailView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerilizers


class UserListView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerilizers
	# authentication_classes = [SessionAuthentication]