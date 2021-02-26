from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'], url_path='like')
    def like_post(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if not post.marks.filter(user=request.user):
            post.like(request.user)
            return Response({"status": "liked"})
        return Response({"status": "user is already mark this post"})

    @action(detail=True, methods=['delete'], url_path='dislike')
    def dislike_post(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if not post.marks.filter(user=request.user):
            post.dislike(request.user)
            return Response({"status": "disliked"})
        return Response({"status": "user is already mark this post"})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
