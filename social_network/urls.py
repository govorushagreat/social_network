from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', include('posts.urls')),
    path('', include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
