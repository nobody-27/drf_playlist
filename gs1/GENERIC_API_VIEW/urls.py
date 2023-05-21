from GENERIC_API_VIEW import views
from django.urls import path


urlpatterns = [
    path('generic_api_view/',views.NoteBook_API.as_view(),name="generic_api_view"),
    path('generic_api_create/',views.NoteBook_CREATE.as_view(),name="generic_api_create"),
    path('generic_api_reterive/<int:pk>/',views.NoteBook_Retrieve.as_view(),name="generic_api_reterive"),
    path('generic_api_update/<int:pk>/',views.NoteBook_UPDATE.as_view(),name="generic_api_update"),
    path('generic_api_delete/<int:pk>/',views.NoteBook_Destroy.as_view(),name="generic_api_destpry")
]