from django.urls import path
from Concrete_View import views

urlpatterns = [
    path('create_notebook_create/',views.Concrete_Notebook_Create.as_view(),name="create_notebook_create"),
    path('create_notebook_list/',views.Concrete_Notebook_list.as_view(),name="create_notebook_list"),
    path('concrete_notebook_retrieve/<int:pk>/',views.Concrete_Notebook_Retrieve.as_view(),name="concrete_notebook_retrieve"),
    path('concrete_notebook_update/<int:pk>/',views.Concrete_Notebook_Update.as_view(),name="concrete_notebook_update"),
    path('concrete_notebook_destroy/<int:pk>/',views.Concrete_Notebook_Destroy.as_view(),name="concrete_notebook_destroy"),



    #shortcut function
    path('list_notebook_create/',views.Concrete_List_Create.as_view(),name="list_notebook_create"),
    path('reterive_notebook_update/<int:pk>/',views.Concrete_Retrive_Update.as_view(),name="reterive_notebook_update"),
    path('reterive_notebook_destroy/<int:pk>/',views.Concrete_Retrive_Destroy.as_view(),name="reterive_notebook_destroy"),




]