from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from journal.models import Journal
from journal.api.permissions import IsOwnerOrReadOnly
from journal.api.serializers import (
    JournalCreateUpdateSerializer,
    JournalDetailSerializer,
    JournalListSerializer,
)


class JournalCreateAPIView(CreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
    serializer_class = JournalDetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'title',
        'content',
        'user__first_name',
        'user__last_name',
    ]

    def get_queryset(self, *args, **kwargs):
        qs_list = Journal.objects.all()
        query = self.request.GET.get("q")
        if query:
            qs_list = qs_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()
        return qs_list


class JournalUpdateAPIView_by_id(RetrieveUpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalCreateUpdateSerializer


class JournalUpdateAPIView_by_slug(RetrieveUpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalCreateUpdateSerializer
    lookup_field = 'slug'





