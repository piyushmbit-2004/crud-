from django.urls import path
from .import views
 
urlpatterns=[
    path('',views.crude,name='crude'),
    path('crude/',views.crude,name='crude'),
    path('add_data/',views.add_data,name='add_data'),
    path('views_records/',views.views_records,name='views_records'),
    path('registation/',views.registation,name='registation'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('edite/<int:id>',views.edite,name='edite'),
    path('report/',views.report,name='report'),



]