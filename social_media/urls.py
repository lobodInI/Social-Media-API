from django.urls import path, include
from rest_framework.routers import DefaultRouter

from social_media.views import UserProfileViewSet

router = DefaultRouter()

router.register("user_profiles", UserProfileViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "social_media"
