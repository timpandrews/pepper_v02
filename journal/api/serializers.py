from rest_framework.serializers import ModelSerializer

from journal.models import Journal


class JournalListSerializer(ModelSerializer):
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
        ]


class JournalDetailSerializer(ModelSerializer):
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
        ]