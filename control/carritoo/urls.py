from django.conf.urls import url,include
from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.product_list),
    url(r'^productos/detalle/(?P<pk>[0-9]+)/$', views.product_detalle),
    url(r'^productos/nuevo/$',views.product_nuevo,''),
    url(r'^productos/editar/(?P<pk>[0-9]+)$',views.product_editar,''),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)