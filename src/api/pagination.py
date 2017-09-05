from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


class PepperLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class PepperPageNumberPagination(PageNumberPagination):
    page_size = 5