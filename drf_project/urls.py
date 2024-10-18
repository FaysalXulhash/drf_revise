
from django.contrib import admin
from django.urls import path, include
from myapp.views import personapi, person_detail_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', personapi),
    path('<int:pk>/',person_detail_api),
    #path('person/', person_api, name = 'person'),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
