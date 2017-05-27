import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import generics

from todos.models import Todo
from todos.serializers import TodoSerializer


@csrf_exempt
@require_http_methods(['PATCH'])
def update(request, id):
    # Get the params from the payload.
    data = json.loads(request.body.decode('utf-8'))

    print('Received update API request for todo id: ', id)
    print('Completed: ', data['completed'])

    # Update the model
    todo = Todo.objects.get(pk=id)
    todo.completed = data['completed']
    todo.save()

    print('Todo item updated')

    return JsonResponse({})


class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
