# get data from model ---> & turned it back to json
# steps to add DFR: https://www.django-rest-framework.org/

from rest_framework import serializers
from .models import Job



class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'