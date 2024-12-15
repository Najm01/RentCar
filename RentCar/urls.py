from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('car-list/', views.car_list, name='car_list'),
    path('chats/', include('chat.urls')),
            ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)