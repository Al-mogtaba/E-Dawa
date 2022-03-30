from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),   
    path('Profile/', views.Profile , name='Profile'),   
    path('Profile/create', views.ProfileCreateView.as_view() , name='create_profile'),      
    path('Profile/update_profile/<int:pk>/', views.ProfileUpdateView.as_view() , name='update_profile'),      
    path('item_list/', views.MedicineListView.as_view() , name='item_list'),   
    path('add_item/', views.MedicineCreateView.as_view() , name='add_item'),   
    path('add/', views.add_item , name='add'),   
    path('edit_item/<int:pk>/', views.MedicineUpdateView.as_view() , name='edit_item'),   
    path('item/<int:pk>/delete/', views.DeleteView.as_view() , name='delete_item'),   
    path('update_admin_profile/', views.update_admin_profile , name='update_admin_profile'),   
]
