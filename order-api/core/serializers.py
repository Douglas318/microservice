from rest_framework import serializers
from .models import Orders

from core.client.users import get_data
from core.publisher.message_publisher import send_message_to_queue

class OrdersSerializer(serializers.ModelSerializer):
    total_value = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        item_quantity = validated_data.get("item_quantity")
        item_price = validated_data.get("item_price")
        total_value = item_quantity * item_price

        user_validate = get_data(f'/users/display?user_id={validated_data.get("user_id")}')

        if user_validate.status_code == 200:
            user_json = user_validate.json()
            data = user_json.get("data", {}).get("user")
            if not data:
                raise serializers.ValidationError("Invalid user data")

            order = Orders.objects.create(
                user_id=validated_data.get("user_id"),
                item_description=validated_data.get("item_description"),
                item_quantity=item_quantity,
                item_price=item_price,
                total_value=total_value
            )

            try:
                message = {
                    "name": data.get("name"),
                    "email": data.get("email"),
                    "phone_number": data.get("phone_number"),
                    "item_description": order.item_description,
                    "item_quantity": order.item_quantity,
                    "item_price": order.item_price,
                    "total_value": order.total_value
                }
                send_message_to_queue.delay(message=message)
            except Exception as error:
                print('Error sending message to queue:', error)
                raise serializers.ValidationError("Failed to process user data")

            return order
        else:
            raise serializers.ValidationError("User validation failed")

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.item_description = validated_data.get("item_description", instance.item_description)
        instance.item_quantity = validated_data.get("item_quantity", instance.item_quantity)
        instance.item_price = validated_data.get("item_price", instance.item_price)
        
        instance.total_value = instance.item_quantity * instance.item_price
        instance.save()

        return instance
