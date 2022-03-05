
from django.urls import path,include
from . import views

urlpatterns = [

   path('',views.home,name = 'home'),
   path('addInForum/',views.addInForum, name="addInForum"),
   path('addInDiscussion/',views.addInDiscussion, name="addInDiscussion"),
   path('delete/<int:id>/',views.delete, name="delete"),
	path('', views.ForumListView.as_view(), name='forum-list'),
   path('<int:id>/',views.get, name="getById"),
   # path('add-comment/<int:pk>', views.CommentCreateView.as_view(), name='add-comment'),
   path('addcomment/',views.commentadd, name="addcomment"),

   
   

]