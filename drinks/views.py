from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# View function for handling GET and POST requests for drink list
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        # Retrieve all drinks from the database
        drinks = Drink.objects.all()
        # Serialize the queryset
        serializer = DrinkSerializer(drinks, many=True)
        # Return the serialized data
        return Response(serializer.data)
    elif request.method == 'POST':
        # Deserialize the incoming data
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            # Save the deserialized data
            serializer.save()
            # Return the serialized data with status 201 CREATED
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return error response if data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View function for handling GET, PUT, and DELETE requests for a specific drink
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    try:
        # Retrieve a specific drink by its primary key
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        # Return 404 NOT FOUND response if drink does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Serialize the drink object
        serializer = DrinkSerializer(drink)
        # Return the serialized data
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Deserialize the incoming data with the existing drink object
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            # Save the updated data
            serializer.save()
            # Return the serialized data
            return Response(serializer.data)
        # Return error response if data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete the drink object from the database
        drink.delete()
        # Return 204 NO CONTENT response
        return Response(status=status.HTTP_204_NO_CONTENT)