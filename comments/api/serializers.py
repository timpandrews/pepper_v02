from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from comments.models import Comment
from profiles.api.serializers import UserDetailSerializer

class CommentSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'content',
        ]


class CommentDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'content',
            'createTS',
            'updateTS',
        ]

