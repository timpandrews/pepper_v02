from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from gardeners.models import Following

class FollowingDetailSerializer(ModelSerializer):
    userName = SerializerMethodField()
    followingName = SerializerMethodField()
    class Meta:
        model = Following
        fields = [
            'id',
            'user',
            'userName',
            'following',
            'followingName',
        ]

    def get_userName(self, obj):
        return str(obj.user.username)

    def get_followingName(self, obj):
        return str(obj.following.username)


class FollowingListSerializer(ModelSerializer):
    userName = SerializerMethodField()
    followingName = SerializerMethodField()
    class Meta:
        model = Following
        fields = [
            'id',
            'user',
            'userName',
            'following',
            'followingName',
        ]

    def get_userName(self, obj):
        return str(obj.user.username)

    def get_followingName(self, obj):
        return str(obj.following.username)


