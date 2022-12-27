from django.shortcuts import render
from .models import Job

# https://docs.djangoproject.com/en/4.1/topics/pagination/
from django.core.paginator import Paginator

# Apply Form
from .form import ApplyForm 

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
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug) # will retrieve on job
    # job_detail = Job.object.filter() # will retrieve on job from a list according to some filtration
    
    # Django bootstrap:  https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
                    myform = form.save(commit=False)
                    myform.job = job_detail
                    myform.save()
                    print('Done')

    else:
        form = ApplyForm()


    context = {'job' : job_detail , 'form' : form}
    return render(request,'job/job_detail.html', context)