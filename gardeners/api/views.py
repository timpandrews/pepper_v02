from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from gardeners.models import Following
from gardeners.api.serializers import FollowingListSerializer

from journal.api.pagination import (
    JournalPageNumberPagination,
)
from journal.api.permissions import IsOwnerOrReadOnly
from journal.api.serializers import (
    JournalCreateUpdateSerializer,
    JournalDetailSerializer,
    JournalListSerializer,
)



class FollowingListAPIView(ListAPIView):
    serializer_class = FollowingListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'user',
        'folloiwng',
        'user__first_name',
        'user__last_name',
    ]
    pagination_class = JournalPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        qs_list = Following.objects.all()
        return qs_list








