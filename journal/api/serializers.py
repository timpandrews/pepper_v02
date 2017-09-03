from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

journal_detail_url = HyperlinkedIdentityField(view_name='journal-api:detail')
journal_delete_url = HyperlinkedIdentityField(view_name='journal-api:delete')
journal_update_url = HyperlinkedIdentityField(view_name='journal-api:update')

from journal.models import Journal


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
            # 'update_url',
            # 'delete_url',
        ]


class JournalListSerializer(ModelSerializer):
    url = journal_detail_url
    # update_url = journal_update_url
    # delete_url = journal_delete_url
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


