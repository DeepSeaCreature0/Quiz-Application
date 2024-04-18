from django.urls import path
from .views import home_view, quiz_view, success_view

urlpatterns = [
    path('', home_view, name='home'),
    path('quiz/<str:user_id>/<str:user_name>/', quiz_view, name='quiz'),
    path('success/<str:favorite_game>/', success_view, name='success'),
]
