from django.http import HttpResponse ,JsonResponse

def http_res(request):
    return HttpResponse('<h1>Hello Mr.Reza </h1>')

def jsontest(request):
    return JsonResponse({'name':'reza'})

def color(request):
    return HttpResponse("<p style='color:blue;' >Hello World</p>")