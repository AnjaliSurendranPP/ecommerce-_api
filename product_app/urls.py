from django.urls import path
from product_app.views import *

urlpatterns=[
    path('watch/',Watch.as_view(),name="watch"),
    path('dress/',Dress.as_view(),name="dress")
]