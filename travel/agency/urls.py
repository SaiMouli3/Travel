from django.urls import path,include
from . import views

app_name = 'agency'
urlpatterns = [
    path('details/', views.travel_details, name='travel_detail'),
    path('packages/',views.packages,name='packages'),
    path('selection/', views.select_package,name='package_selection'),
]

