from django.urls import path
from .views import SendCodeView, VerifyCodeView, UserProfileView, ActivateInviteView

urlpatterns = [
    path('auth/send-code/', SendCodeView.as_view(), name='send-code'),
    path('auth/verify-code/', VerifyCodeView.as_view(), name='verify-code'),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<int:user_id>/activate-invite/', ActivateInviteView.as_view(), name='activate-invite'),
]
