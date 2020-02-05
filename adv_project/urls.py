from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from adventure import views

router = routers.DefaultRouter()
router.register(r'rooms', views.RoomView, 'adventure_room')
router.register(r'players', views.PlayerView, 'adventure_player')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('api/adv/', include(router.urls)),
]
