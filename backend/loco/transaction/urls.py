from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('types/<str:type>', views.TransactionTypes.as_view(),name='types'),
    path('sum/<int:pk>', views.TransactionSums.as_view(),name='sum'),
    path('transaction/<int:pk>', views.TransactionViews.as_view(),name='transaction'),
    path('transaction/all', views.Transactions.as_view(),name='transections'),
    path('transaction/parents_list', views.TransactionsParent.as_view(),name='transections'),
    
]

