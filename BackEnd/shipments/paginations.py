from rest_framework.pagination import PageNumberPagination

class ShipmentsPagination(PageNumberPagination):
    page_size = 50
