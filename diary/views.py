from django.shortcuts import render
from .models import Page

def page_list(request):
    posts = Page.objects.all()
    context = {"posts":posts}
    
    return render(request, 'diary/page_list.html', context = context)

def page_detail(request, pg_id):
    post = Page.objects.get(id=pg_id)
    context = {"post":post}
    
    return render(request, "diary/page_detail.html", context = context)



