from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace='web')),
    
    path('tinymce/', include('tinymce.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Sahid Cholayil Administration"
admin.site.site_title = "Sahid Cholayil Admin Portal"
admin.site.index_title = "Welcome to Sahid Cholayil Admin Portal"
