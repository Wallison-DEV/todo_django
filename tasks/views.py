from django.shortcuts import render
# Create your views here.
def taskList(request, name):
    return render(request,'tasks/list.html', {'name': name})
