from django.urls import path,include
from Serilizer_Relations import views
from rest_framework.routers import DefaultRouter



# creating object
# relation_serilizer = DefaultRouter()
# relation_serilizer.register('singer',views.SingerViewset,basename="singer")
# relation_serilizer.register('song',views.SongViewset,basename="song")


urlpatterns = [
    # path('',include(relation_serilizer.urls)),

    path('song/',views.SongApiView.as_view(),name="song"),
    path('singer/<int:singer_id>/',views.SingerApiView.as_view(),name="singer")

]