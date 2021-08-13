"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include,re_path
from django.conf.urls.static import static
from rest_framework import routers
from core import views
from Blog import settings
from django.views.static import serve


router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    #   path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
     re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }),
]

