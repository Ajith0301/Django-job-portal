from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from job.models import hydjobs,blorejobs,chennaijobs
from job.api.serializers import HydJobsSerializer,BlorejobsSerializer,chennaijobssSerializer
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=HydJobsSerializer
    queryset=hydjobs.objects.all()
    pagination_class = PageNumberPagination
    search_fields=('company','title','eligibility')

class BloreJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=BlorejobsSerializer
    queryset=blorejobs.objects.all()
    pagination_class = PageNumberPagination
    search_fields=('company','title','eligibility')

class ChennaiJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class=chennaijobssSerializer
    queryset=chennaijobs.objects.all()
    pagination_class = PageNumberPagination
    search_fields=('company','title','eligibility')
