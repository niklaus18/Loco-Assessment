from rest_framework import serializers
from transaction.models import Transaction

class TransactionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ('id','deleted_at','created_at','updated_at','transaction_id', )