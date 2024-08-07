from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('c/', include('campaigns.urls'))
]
