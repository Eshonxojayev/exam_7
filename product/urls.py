from django.urls import path
from .views import ProductAPIView, CategoryAPIView, CommentAPIView, CartAPIView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView, ProductDetailView, CartView

router = DefaultRouter()
router.register('products', ProductAPIView)
router.register('categories', CategoryAPIView)
router.register('comments', CommentAPIView)
router.register('cart', CartAPIView)

urlpatterns = [
    path('product/', ProductListView.as_view(), name='shopping'),
    path('product/detail/<int:id>/', ProductDetailView.as_view(), name='shop-detail'),
    path('cart/<int:id>/detail', CartView.as_view(), name='cart'),
    path('', include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)