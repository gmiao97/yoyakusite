from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserViewSet, EventViewSet, SubjectListByTeacher, TeacherListBySubject, ValidateToken, \
    SubscriptionPlan, StripePrice, StripeProduct, StripeSubscription, StripeCustomerPortal, StripeWebhook, \
    LogoutAndBlacklistRefreshTokenForUserView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('subjects-by-teacher/', SubjectListByTeacher.as_view()),
    path('teachers-by-subject/', TeacherListBySubject.as_view()),
    path('validate-token/', ValidateToken.as_view()),
    path('subscription-plan/', SubscriptionPlan.as_view()),
    path('stripe-prices/', StripePrice.as_view()),
    path('stripe-products/', StripeProduct.as_view()),
    path('stripe-subscription/', StripeSubscription.as_view()),
    path('stripe-customer-portal/', StripeCustomerPortal.as_view()),
    path('stripe-webhook/', StripeWebhook.as_view()),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
]
