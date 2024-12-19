from django.urls import path
from .views import AccessLogListView, AccessLogDetailView

app_name = 'access_logs'

urlpatterns = [
    path('', AccessLogListView.as_view(), name='log_list'),
    path('<int:pk>/', AccessLogDetailView.as_view(), name='log_detail'),
]
