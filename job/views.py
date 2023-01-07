from django.shortcuts import render
from .models import Job
from django.shortcuts import redirect, render
from django.urls import reverse
# https://docs.djangoproject.com/en/4.1/topics/pagination/
from django.core.paginator import Paginator

# decorator login required
from django.contrib.auth.decorators import login_required

# Apply Form
from .form import ApplyForm , JobForm

# Model Queryset in Django
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

# Will Retrieve all jobs 
def job_list(request):
    job_list = Job.objects.all()
    
    # Pagination
    paginator = Paginator(job_list, 5) # Show 3 contacts per page.
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


@login_required
def add_job(request):
    if request.method=='POST':
        pass
        form = JobForm(request.POST , request.FILES) # request.FILES if theres any pic <form method="POST" enctype="multipart/form-data">
        if form.is_valid(): # to make sure the form is valid
            myform = form.save(commit=False) # save the form but not in the db because i need to add the person who added the job
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list')) # after saving redirect to the job list REVERSE takes the urls (project:app)

    else:
        form = JobForm()
    return render(request,'job/add_job.html', {'form': form})