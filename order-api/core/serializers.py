from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        order = Orders()
        order.user_id = validated_data.get("user_id")
        order.item_description = validated_data.get("item_description")
        order.item_quantity = validated_data.get("item_quantity")
        order.item_price = validated_data.get("item_price")
        order.save()

        return validated_data

    def update(self, instance: Orders, validated_data):
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.item_description = validated_data.get("item_description", instance.item_description)
        instance.item_quantity = validated_data.get("item_quantity", instance.item_quantity)
        instance.item_price = validated_data.get("item_price", instance.item_price)
        instance.save()

        return instance