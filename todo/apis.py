from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class TodoCreateAPI(APIView):
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)

class TodoListAPI(APIView):
    
    def get(self, reuqest):
        todos = Todo.objects.all()  # QuerySet = Object list
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodoRetrieveAPI(APIView):
    
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

class TodoUpdateAPI(APIView):
    
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoexNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
        
    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoexNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
class TodoDeleteAPI(APIView):
    
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoexNotExist:
            return Response({"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(data={"data": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoSerializer
    
    
class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsDeleteAPI(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
    authentication_classed = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    # 본인의 todo만 조회
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        return queryset.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
