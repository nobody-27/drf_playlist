from django.contrib import admin
from django.urls import path,include
from Model_View_Set_last import views
from rest_framework.routers import DefaultRouter

#creating Object
router = DefaultRouter()

#register 
router.register('classroom',views.ClassRoomViewSet,basename="classroom")
router.register('classromm_read_only',views.ClassRoomReadonlyViewset,basename="class_room_read_only")

urlpatterns = [
    path('',include(router.urls)),
]
