from django.urls import path
from .views import index,delete,deleteAll
urlpatterns = [
    path("",index,name='home'),
    path("delete/<int:id>",delete,name='delete'),
    path("destroy/",deleteAll,name='destroy'),
]