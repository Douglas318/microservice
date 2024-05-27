from django.db import models


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False)
    item_description = models.CharField(max_length=150)
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'orders'