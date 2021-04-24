from rest_framework.response import Response
from rest_framework import status
from books.models import Book, ISBN
from .serializers import BookSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
def index(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                "success": True,
                "message": "Book added successfully"
            }, status=status.HTTP_201_CREATED)

        return Response(data={
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={
        "success": False,
        "errors": "Internal server error"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def singleResourceRud(request, id):
    if request.method == "GET":
        try:
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(instance=book)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={
                "success": False,
                "errors": "Book not found   "
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        try:
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "success": True,
                    "message": "Book updated successfully"
                }, status=status.HTTP_202_ACCEPTED)

            return Response(data={
                "success": False,
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data={
                "success": False,
                "errors": "Book not found."
            }, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return Response(data={
                "success": True,
                "message": "Book deleted successfully"
            }, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(data={
                "success": False,
                "errors": "Book not found."
            }, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
