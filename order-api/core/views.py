from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from core.serializers import *


@api_view(['GET'])
@permission_classes([AllowAny])
def list_orders(request: Request) -> Response:
    orders = Orders.objects
    return Response(OrdersSerializer(orders, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def display_order(request: Request) -> Response:
    order = get_object_or_404(Orders, id=request.query_params.get("order_id"))
    serializer = OrdersSerializer(order, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([AllowAny])
def update_order(request: Request) -> Response:
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.update(serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_order(request: Request) -> Response:
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_order(request: Request) -> Response:
    order = Orders.objects.filter(id=request.query_params.get("order_id"))
    if order.exists():
        order.delete()
        return Response({"message": "Pedido apagado com sucesso!"}, status=status.HTTP_200_OK)
    return Response({"message": "Pedido não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

