
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ViewSet import views

#Creating Router Object
dummy_router = DefaultRouter()

#Register NoteBookViewSet with Router
dummy_router.register('notebook_viewset',views.NoteBookViewSet,basename='notebook_viewset'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('curd.urls')),
    path('model_serilizers/', include('model_serilizers.urls')),
    path('function/',include('function_based.urls')),
    path('class/',include('class_based_APIVIEW.urls')),
    
    path('generic/',include('GENERIC_API_VIEW.urls')),
    path('concrete_view/',include('Concrete_View.urls')),


    path('viewset/',include(dummy_router.urls)),
    path('model_view_set/',include('Model_View_Set_last.urls')),
    path('auth_api_all/',include('BasicAuthentication.urls')),
    
]   
