from django.conf.urls import include, url

from rest_framework import routers

from .api import UserViewSet
from .views import HomeTemplateView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [

	url(r'^home/$', HomeTemplateView.as_view()),


    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
