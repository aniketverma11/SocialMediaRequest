from django.urls import path
from users.api.views import UserSignupView, UserLoginView, SearchUserView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('search/', SearchUserView.as_view(), name='search')
]