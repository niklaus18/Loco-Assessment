from rest_framework.decorators import action
from rest_framework import status, viewsets
from transaction.models import Transaction
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from transaction.serializers import TransactionListSerializer

class TransactionViews(viewsets.ViewSet):
    
    @action(methods=["GET"], detail=True, url_path='list')
    def transaction_list(self, request, pk):
        transaction_type = pk
        transaction_queryset = Transaction.objects.filter(type=transaction_type)
        serializer = TransactionListSerializer(transaction_queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)