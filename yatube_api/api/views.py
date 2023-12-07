from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для сообществ."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Сохранение записи в БД с автором поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        """Получение комментариев поста."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer):
        """Сохранение записи в БД с автором комментария."""
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        )


class FollowViewSet(
    viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    """Вьюсет для подписок."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('=following__username', '=user__username',)

    def get_queryset(self):
        """Получение пописок пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Сохранение  подписавшегося пользователя в БД."""
        serializer.save(user=self.request.user)
