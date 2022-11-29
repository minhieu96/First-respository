from django.shortcuts import render

from django.http import HttpResponse ,JsonResponse

def index_page(request):
    return render(request,'web/index.html')

def account_page(request):
    return render(request,'my-account.html')

def contact_page(request):
    return render(request,'contact.html')