from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from interview.views import CategoryViewSet, QuestionAnswerViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('question', QuestionAnswerViewSet, basename='question')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

