from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from gardeners.models import Following
from gardeners.api.serializers import (
    FollowingDetailSerializer,
    FollowingListSerializer,
)

from journal.api.pagination import (
    JournalPageNumberPagination,
)
from journal.api.permissions import IsOwnerOrReadOnly



class FollowingDetailAPIView(RetrieveAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingDetailSerializer
    lookup_field = 'id'


class FollowingListAPIView(ListAPIView):
    serializer_class = FollowingListSerializer
    filter_backends = [OrderingFilter]
    pagination_class = JournalPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        qs_list = Following.objects.all()
        return qs_list








