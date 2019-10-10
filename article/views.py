from django.shortcuts import render, HttpResponse


sozluk = {
    "liste" : [1,2,3,4,5,6,7,8]

}
# Create your views here.
def index(request):
    return render(request, "index.html", sozluk)

def about(request):
    return render(request, "about.html")

