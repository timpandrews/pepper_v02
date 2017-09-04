from src.api.pagination import PepperPageNumberPagination

from gardeners.api.serializers import (
    FollowingDetailSerializer,
    FollowingListSerializer,
)
from gardeners.models import Following
from rest_framework.filters import (
    OrderingFilter,
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)


class FollowingDetailAPIView(RetrieveAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingDetailSerializer
    lookup_field = 'id'


class FollowingListAPIView(ListAPIView):
    serializer_class = FollowingListSerializer
    filter_backends = [OrderingFilter]
    pagination_class = PepperPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        qs_list = Following.objects.all()
        return qs_list








