from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


class JournalLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class JournalPageNumberPagination(PageNumberPagination):
    page_size = 2