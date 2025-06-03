from django.urls import path
from .views import thank_you, dashboard, contact_view, feedback_view


urlpatterns = [
    path('', contact_view, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('feedback/', feedback_view, name='feedback'),
    path('thank-you/', thank_you, name='thank_you'),
]
