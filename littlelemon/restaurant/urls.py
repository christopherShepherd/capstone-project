from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('', index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
]