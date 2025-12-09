from django.shortcuts import render

def home(request):
    return render(request,'map.html')
def mar(request):
    return render(request,'marry.html')
def place(request):
    return render(request,'palace.html')
def sil(request):
    return render(request,'silk.html')
def temp(request):
    return render(request,'temple.html')

