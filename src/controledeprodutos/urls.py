from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from apps.produtos import views


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("produtos/", include("apps.produtos.urls")),
    path("users/", include("apps.users.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


handler403 = 'django.views.defaults.permission_denied'