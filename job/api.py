# its  just like the views but specific for the API

from .models import Job
from .serializers import JobSerializer

# rest_framework libraries
from rest_framework.response import Response
from rest_framework.decorators import api_view # decorator to tell that im using a function
from rest_framework import generics

# Function based views
@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all() # return all the data
    data = JobSerializer(all_jobs, many=True).data # pass the data to the serializer | many= true because i have many data
    return Response({'data':data}) # return a json data as a response 

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})

# ------------------------------------------------------------------

# generic-views: https://www.django-rest-framework.org/api-guide/generic-views/
# Class based views

# List & create at the same time 
# https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# retrieve & update & delete at the same time 
# https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    
# ------------------------------------------------------------------


'''
- Function based views:
    simple 
    easy to customize 
    for complex thing 
    
- Class based views:
    fast for who understand it very good 
    not complex

- Viewset: 
api --- [url+ model] i'll find that the [CRUD] operation is ready
the most easiest way 
not easy to customize 
'''



