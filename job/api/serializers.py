from rest_framework.serializers import ModelSerializer
from job.models import hydjobs,blorejobs,chennaijobs
class HydJobsSerializer(ModelSerializer):
    class Meta:
        model=hydjobs
        fields='__all__'

class BlorejobsSerializer(ModelSerializer):
    class Meta:
        model=blorejobs
        fields='__all__'

class chennaijobssSerializer(ModelSerializer):
    class Meta:
        model=chennaijobs
        fields='__all__'
