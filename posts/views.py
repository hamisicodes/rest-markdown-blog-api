from rest_framework import generics, permissions
from .permissions import isAuthor
from .models import Post
from .serializers import PostCreateSerializer, PostSerializer , PostUpdateSerializer


class PostListView(generics.ListAPIView):
    permission_classes =[permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    permission_classes =[permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_serializer_context(self):
        context = super(PostDetailView,self).get_serializer_context()
        context.update({
            "request":self.request
        })

        return context

class PostCreateView(generics.CreateAPIView):
    permission_classes =[permissions.IsAuthenticated]
    serializer_class = PostCreateSerializer

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class PostUpdateView(generics.UpdateAPIView):
    permission_classes =[permissions.IsAuthenticated,isAuthor]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'

class PostDeleteView(generics.DestroyAPIView):
    permission_classes =[permissions.IsAuthenticated,isAuthor]
    queryset = Post.objects.all()
    lookup_field = 'slug'




