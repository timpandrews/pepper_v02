from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from journal.models import Journal
from journal.api.serializers import (
    JournalCreateUpdateSerializer,
    JournalDetailSerializer,
    JournalListSerializer,
)


class JournalCreateAPIView(CreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalCreateUpdateSerializer


class JournalDeleteAPIView_by_id(DestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer


class JournalDeleteAPIView_by_slug(DestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer
    lookup_field = 'slug'


class JournalDetailAPIView_by_id(RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer


class JournalDetailAPIView_by_slug(RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer
    lookup_field = 'slug'


class JournalListAPIView(ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalListSerializer


class JournalUpdateAPIView_by_id(UpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalCreateUpdateSerializer


class JournalUpdateAPIView_by_slug(UpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalCreateUpdateSerializer
    lookup_field = 'slug'





