from django.urls import path,include
from rest_framework import routers
from job.api.views import HydJobsCRUDCBV,BloreJobsCRUDCBV,ChennaiJobsCRUDCBV
router=routers.DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUDCBV)
router.register('blorejobsinfo',BloreJobsCRUDCBV)
router.register('chennaijobsinfo',ChennaiJobsCRUDCBV)

urlpatterns = [
 path('', include(router.urls)),
 ]
