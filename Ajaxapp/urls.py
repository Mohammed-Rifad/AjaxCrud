from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load-students',views.load_students),
    path('add-student',views.add_student,name='add_student'),
    path('del-student',views.delete_student,name='del_student'),
    path('update-student',views.update_student,name='upd_student')
]