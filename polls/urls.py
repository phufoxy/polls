from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.index_details,name='index_details'),
    path('a/',views.index_newdata,name='newdata'),
    path('create_view/',views.create_view,name='create_view'),
    path('update/<int:id>/',views.index_update,name='update'),
    path('updateview/<int:id>/',views.update_view,name='update_view'),
    path('delete/<int:id>/',views.delete_view,name='delete_view')
]