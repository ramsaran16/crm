from django.urls import path
from . import views


urlpatterns = [
    path('',views.example),
    path('add/',views.add_formView),
    path('std/',views.view_data),
    path('place/',views.addProduct),
    path('placement/',views.index),
]