from django.urls import path
from . import views
 
urlpatterns = [
    path ('first',views.user,name="firstpage"),
    path('second',views.sec,name='Secondpage'),
    path('image/<str:imagename>',views.image,name='My image Page')
]