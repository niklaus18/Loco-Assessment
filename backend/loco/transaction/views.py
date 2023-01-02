from rest_framework.decorators import action
from rest_framework import status, viewsets
from transaction.models import Transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from transaction.serializers import TransactionListSerializer,TransactionPostSerializer
from django.db.models import Sum

class TransactionViews(APIView):
    
    def get(self, request,pk):
        transaction_queryset = Transaction.objects.filter(transaction_id=pk)
        serializer = TransactionListSerializer(transaction_queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, pk):
        request_data = request.data
        request.data['transaction_id'] = pk
        serializer = TransactionPostSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data, status=HTTP_200_OK)

class TransactionSums(APIView):
    def get(self,request,pk):
        total_sum = Transaction.objects.filter(parent_id=pk).aggregate(Sum('amount'))
        return Response({"sum":total_sum.get('amount__sum')}, status=HTTP_200_OK)

class TransactionTypes(APIView):
    def get(self,type):
        transaction_queryset = Transaction.objects.filter(type= type)
        serializer = TransactionListSerializer(transaction_queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)
