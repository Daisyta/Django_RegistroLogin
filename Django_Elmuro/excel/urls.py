from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/',views.export_users_csv,name='export_users_csv'),
]
