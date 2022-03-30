from . import views as main_views
from django.urls import path


urlpatterns = [
    path('', main_views.index , name='home'),
    path('search/', main_views.search , name='search'),
    path('custom_search/', main_views.custom_search , name='custom_search'),
    path('medicin_request/', main_views.medicin_request , name='medicin_request'),
   
    path('login/', main_views.login , name='login'),
    path('topics/', main_views.topics , name='topics'),
]