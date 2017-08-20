from rest_framework.generics import ListAPIView, RetrieveAPIView

from journal.models import Journal
from journal.api.serializers import (
    JournalListSerializer,
    JournalDetailSerializer
)


class JournalDetailAPIView_by_id(RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer


class JournalDetailAPIView_by_slug(RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer
    lookup_field = 'slug'


class JournalListAPIView(ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


