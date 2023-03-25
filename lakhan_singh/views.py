from django.shortcuts import render
from service.models import contact
def show(request):
    if request.method=="POST":
     post=contact()
     post.name=request.POST['name']
     post.email=request.POST['email']
     post.Comments=request.POST['comment']
     post.save()
     return render(request,"index.html")
    else:
      return render(request,"index.html")