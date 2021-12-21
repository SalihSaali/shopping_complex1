from django.urls import path
from.import views

urlpatterns=[
    path('reg',views.register,name='reg'),
    path('ab',views.ab,name='ab')


]