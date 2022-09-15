from django.urls import path
from .import views
app_name = 'main'
urlpatterns = [
    path('',views.homepage, name = 'homepage'),
    path('doctor/',views.doctor, name = 'doctor'),
    path('patient/',views.patient , name = 'patient')
]
