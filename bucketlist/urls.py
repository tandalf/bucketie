from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import BucketListViewSet, UserView

router = DefaultRouter()
router.register('bucketlist', BucketListViewSet, base_name='bucketlist')

urlpatterns = [
    url(r'users/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user-detail'),
]
urlpatterns += router.urls
