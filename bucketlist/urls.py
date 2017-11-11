from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import BucketListViewSet, UserView, BucketListItemViewSet
from .template_views import index, signedin, bucketlist_list

router = ExtendedSimpleRouter()
router.register(r'bucketlist', BucketListViewSet, base_name='bucketlist')\
    .register(r'items', BucketListItemViewSet, base_name='items', 
        parents_query_lookups=['bucketlist'])

urlpatterns = router.urls

urlpatterns += [
    url(r'^$', index, name='index'),
    url(r'^signedin$', signedin, name='signedin'),
    url(r'^bucketlist$', bucketlist_list, name='bucketlist_list'),
    url(r'users/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user-detail'),
]