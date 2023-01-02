from . import views
from django.urls import path

urlpatterns = [
    path('types/<str:type>', views.TransactionTypes.as_view(),name='types'),
    path('sum/<int:pk>', views.TransactionSums.as_view(),name='sum'),
    path('transaction/<int:pk>', views.TransactionViews.as_view(),name='transaction')
]

