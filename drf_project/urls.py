
from django.contrib import admin
from django.urls import path, include
from myapp.views import index,details, create_person
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('<int:pk>/',details),
    path('new/', create_person, name = 'new-person'),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
