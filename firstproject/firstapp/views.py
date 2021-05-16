from django.shortcuts import render

def welcome(request):
    return render(request,"welcome.html")

def hello(request):
    userName = request.GET['name'] #input box name= 값 가져오기
    return render(request,'hello.html', {'userName':userName})