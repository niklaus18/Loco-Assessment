
from django.test import TestCase
from transaction.models import Transaction

class TransactionTestCase(TestCase):
    def setUp(self):
        Transaction.objects.create(transaction_type="car", amount=2000)
        Transaction.objects.create(transaction_type="car", amount=500)

    def test_transaction(self):
        t1 = Transaction.objects.get(transaction_type="car", amount=2000)
        t2 = Transaction.objects.get(transaction_type="car", amount=500)
        self.assertEqual(t1.transaction_type, t2.transaction_type)