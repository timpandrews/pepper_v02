from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
)

from gardeners.models import Following

from journal.models import Journal


class FollowingCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = [
            'title',
            'content',
            'draft',
            'publish',
        ]


class FollowingDetailSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'draft',
            'publish',
            'createTS',
            'updateTS',
            'comments',
            # 'update_url',
            # 'delete_url',
        ]

    # def get_user(self, obj):
    #     return str(obj.user.username)
    #
    # def get_comments(self, obj):
    #     comments_qs = Comment.objects.filter_by_instance(obj)
    #     comments = CommentSerializer(comments_qs, many=True).data
    #     return comments


class FollowingListSerializer(ModelSerializer):
    userName = SerializerMethodField()
    followingName = SerializerMethodField()
    class Meta:
        model = Following
        fields = [
            # 'url',
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


