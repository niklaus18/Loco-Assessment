from transaction.models import Transaction
from django.db.models import Sum


def get_sum(ids, checked_id=None):
    checked_id = [] if checked_id is None else checked_id
    if len(ids) == 0:
        return 0
    total_sum = 0
    query_set = Transaction.objects.filter(
        parent_id__in=ids).exclude(parent_id__in=checked_id)
    checked_id.extend(ids)
    if len(query_set) > 0:
        total_sum += query_set.aggregate(Sum('amount')).get('amount__sum')
        vals = query_set.values_list('parent_id', flat=True).distinct()
        total_sum += get_sum(vals, checked_id)
    return total_sum
