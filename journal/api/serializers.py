from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
)

from comments.api.serializers import CommentSerializer
from comments.models import Comment

from profiles.api.serializers import UserDetailSerializer

from journal.models import Journal


journal_detail_url = HyperlinkedIdentityField(view_name='journal-api:detail')
journal_delete_url = HyperlinkedIdentityField(view_name='journal-api:delete')
journal_update_url = HyperlinkedIdentityField(view_name='journal-api:update')


class JournalCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = [
            'title',
            'content',
            'draft',
            'publish',
        ]


class JournalDetailSerializer(ModelSerializer):
    # update_url = journal_update_url
    # delete_url = journal_delete_url
    comments = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
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

    def get_comments(self, obj):
        content_type = obj.get_content_type

        comments_qs = Comment.objects.filter_by_instance(obj)
        comments = 'test'


class JournalListSerializer(ModelSerializer):
    url = journal_detail_url
    # update_url = journal_update_url
    # delete_url = journal_delete_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Journal
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'draft',
            'publish',
            'createTS',
            'updateTS',
            # 'update_url',
            # 'delete_url',
        ]



