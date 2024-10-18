from django.contrib import admin
from django.urls import path, include
from myapp.views import PersonApi #personapi, person_details_api

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('personapi', PersonApi, basename='person')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('', personapi.as_view(),),
    #path('<int:pk>/', person_details_api.as_view()),
    #path('', personapi),
    #path('<int:pk>/',person_detail_api),
    #path('person/', person_api, name = 'person'),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
