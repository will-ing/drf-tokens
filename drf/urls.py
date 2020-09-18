from .views import HelloView
from django.contrib import admin
from django.urls import include, path
from django.urls import path
from .views import PostList, PostDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', HelloView.as_view(), name='hello'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
