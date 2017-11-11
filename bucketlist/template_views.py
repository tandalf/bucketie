from django.shortcuts import render

def index(request):
    return render(request, 'bucketlist/index.html')

def signedin(request):
    return render(request, 'bucketlist/signedin.html')

def bucketlist_list(request):
    return render(request, 'bucketlist/bucketlist_list.html')