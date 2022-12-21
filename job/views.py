from django.shortcuts import render
from .models import Job

# Model Queryset in Django
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

# Will Retrieve all jobs 
def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs': job_list} # template name
    return render(request, 'job/job_list.html', context)

# Will Retrieve one jobs details
def job_detail(request, id):
    job_detail = Job.objects.get(id=id) # will retrieve on job
    # job_detail = Job.object.filter() # will retrieve on job from a list according to some filtration
    context = {'job': job_detail}
    return render(request,'job/job_detail.html', context)