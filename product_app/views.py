from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.
class Watch(View):
    def get(self,request):
        product={
            "name":"Titan Watch",
            "price":500,
            "catagory":"watch",
            "company":"Titan"
        }
        return JsonResponse(product)


class Dress(View):
    def get(self,request):
        product={
            "name":"Kurthi",
            "price":555,
            "catagory":"dress_women",
            "company":"Trends"
        }
        return JsonResponse(product)
