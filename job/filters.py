import django_filters
from .models import Job

# steps from here to use the filter library: https://github.com/carltongibson/django-filter
# https://django-filter.readthedocs.io/en/main/

class JobFilter(django_filters.FilterSet):
    
    # to search if the title & the description contain a specific word
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner','published_at','image','salary','Vacancy','slug']