from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import BucketListViewSet, UserView, BucketListItemViewSet

router = ExtendedSimpleRouter()
router.register(r'bucketlist', BucketListViewSet, base_name='bucketlist')\
    .register(r'items', BucketListItemViewSet, base_name='items', 
        parents_query_lookups=['bucketlist'])

# bucketlist_router = DefaultRouter()
# bucketlist_items_router = DefaultRouter()

# bucketlist_router.register('bucketlist', BucketListViewSet, base_name='bucketlist')
# bucketlist_items_router.register('items', BucketListItemViewSet, base_name='items')

# urlpatterns = [
#     url(r'users/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user-detail'),
#     url(r'bucketlist/(?P<bucketlist_pk>[0-9]+)/', include(bucketlist_items_router.urls)),
# ]
# urlpatterns += bucketlist_router.urls

urlpatterns = router.urls