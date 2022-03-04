from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [

   path('',views.home,name = 'home'),
   path('addInForum/',views.addInForum, name="addInForum"),
   path('addInDiscussion/',views.addInDiscussion, name="addInDiscussion"),
   path('delete/<int:id>/',views.delete, name="delete"),
   

]