from django.db import models
from django.utils.text import slugify


'''
 django model field : 
    - html widget
    - validation 
    - db size 
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

#https://docs.djangoproject.com/en/4.1/ref/models/fields/
class Job(models.Model):  
    title        = models.CharField(max_length=100)  
    job_type     = models.CharField(max_length=15 , choices=JOB_TYPE)
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy      = models.IntegerField(default=1)
    salary       = models.IntegerField(default=0)
    experience   = models.IntegerField(default=1) 
    image = models.ImageField(upload_to= image_upload)
    
    # https://docs.djangoproject.com/en/4.1/ref/forms/fields/ 
    # short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    slug = models.SlugField(blank=True, null=True) # https://www.jobboard.com/add-the-slug-field-inside-django-model/
    
    # Relations
    category     = models.ForeignKey('Category',on_delete=models.CASCADE, default=1) # one to many
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title) # slugify will take the title and replace the space with underscore (job-board-software-engineer)
        super(Job,self).save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
