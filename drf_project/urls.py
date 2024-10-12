
from django.contrib import admin
from django.urls import path, include
from myapp.views import index,details, person_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('<int:pk>/',details),
    path('person/', person_api, name = 'person'),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
