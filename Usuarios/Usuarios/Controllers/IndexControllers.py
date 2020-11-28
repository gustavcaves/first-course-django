from django.shortcuts import render,HttpResponse

class IndexController():
    def index(request):
        # return HttpResponse('<h1>Gustav Caves</h1>%s' %year)
        return render(request, 'views/index/index.html')
    def about(request):
        return render(request, 'views/index/about.html')