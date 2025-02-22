from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/quotes/author/<str:author_name>/', QuoteViewSet.as_view({'get': 'list'}), name='quote-by-author'),
]