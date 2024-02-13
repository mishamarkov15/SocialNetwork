from django.urls import path

from home.views import ProfileView

app_name = 'home'

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
]
