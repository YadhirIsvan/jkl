from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_view, login_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Autenticación básica con DRF Token (opcional si ya usas JWT)
    path('login/', obtain_auth_token, name='login'),

    # Autenticación personalizada con JWT
    path('login-app/', login_view, name='login-app'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # JWT tokens (más seguro y recomendado)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
