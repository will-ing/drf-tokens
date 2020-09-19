from .views import HelloView
from django.contrib import admin
from django.urls import include, path
from .views import PostList, PostDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('<int:pk>/', PostList.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='hello'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
