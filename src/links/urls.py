from django.urls import path
from links.api import views

urlpatterns = [
    path('shorten/', views.CreateLinkView.as_view(), name='shorten'),
    path('stats/<str:short_code>/', views.ListStatsView.as_view(), name='stats'),
    path('<str:short_code>/', views.LinkRedirectView.as_view(), name='redirect'),
]