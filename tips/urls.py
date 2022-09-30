from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from interview.views import CategoryViewSet, QuestionAnswerDetailView, QuestionAnswerListView

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/question/', QuestionAnswerListView.as_view()),
    path('api/question/<int:pk>/', QuestionAnswerDetailView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

