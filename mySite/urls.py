from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('minotes/', include('minotes.urls')),
    path('', include('user_auth.urls'))
]
