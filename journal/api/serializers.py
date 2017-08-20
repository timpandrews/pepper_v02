from rest_framework.serializers import ModelSerializer

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


