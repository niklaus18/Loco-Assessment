from rest_framework.decorators import action
from rest_framework import status, viewsets
from transaction.models import Transaction
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from transaction.serializers import TransactionListSerializer

class TransactionViews(viewsets.ViewSet):
    
    @action(methods=["GET"], detail=True, url_path='list')
    def transaction_list(self, request, pk):
        transaction_type = pk
        transaction_queryset = Transaction.objects.filter(transaction_type=transaction_type)
        serializer = TransactionListSerializer(transaction_queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    @action(methods=["POST"], detail=False, url_path="create")
    def create_transaction(self, request):
        request_data = request.data
        serializer = TransactionListSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(data="Transaction created successfully", status=HTTP_200_OK)
