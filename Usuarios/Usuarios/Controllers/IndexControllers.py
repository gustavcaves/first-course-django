from django.shortcuts import render,HttpResponse

class IndexController():
    def index(request):
        # return HttpResponse('<h1>Gustav Caves</h1>%s' %year)
        return render(request, 'templates/views/index.html')