from django.shortcuts import render
from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from job.models import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'job/home.html',)
def about(request):
    return render(request, 'job/about.html', {'title': 'About'})

@login_required
def jobportal(request):
    return render(request,'job/index.html')

def hjobs1(request):
    jobs_list=hydjobs.objects.order_by('-date')
    paginator=Paginator(jobs_list,10)
    page_number=request.GET.get('page')
    try:
       jobs_list=paginator.page(page_number)
    except PageNotAnInteger:
       jobs_list=paginator.page(1)
    except EmptyPage:
       jobs_list=paginator.page(paginator.num_pages)
    return render(request,'job/hydjobs.html',{'jobs_list':jobs_list})

def bjobs(request):
    blore_jobs=blorejobs.objects.order_by('-date')
    paginator=Paginator(blore_jobs,20)
    page_number=request.GET.get('page')
    try:
       blore_jobs=paginator.page(page_number)
    except PageNotAnInteger:
       blore_jobs=paginator.page(1)
    except EmptyPage:
       blore_jobs=paginator.page(paginator.num_pages)
    return render(request,'job/blorejobs.html',{'blore_jobs':blore_jobs})

def cjobs(request):
    chennai_jobs=chennaijobs.objects.order_by('-date')
    paginator=Paginator(chennai_jobs,20)
    page_number=request.GET.get('page')
    try:
      chennai_jobs=paginator.page(page_number)
    except PageNotAnInteger:
       chennai_jobs=paginator.page(1)
    except EmptyPage:
      chennai_jobs=paginator.page(paginator.num_pages)
    return render(request,'job/chennaijobs.html',{'chennai_jobs':chennai_jobs})
