from django.shortcuts import render
from .models import Job

# https://docs.djangoproject.com/en/4.1/topics/pagination/
from django.core.paginator import Paginator


# Model Queryset in Django
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

# Will Retrieve all jobs 
def job_list(request):
    job_list = Job.objects.all()
    
    # Pagination
    paginator = Paginator(job_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs': page_obj} # template name
    return render(request, 'job/job_list.html', context)

# Will Retrieve one jobs details
def job_detail(request, id):
    job_detail = Job.objects.get(id=id) # will retrieve on job
    # job_detail = Job.object.filter() # will retrieve on job from a list according to some filtration
    context = {'job': job_detail}
    return render(request,'job/job_detail.html', context)