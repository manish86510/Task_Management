from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Task


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user': token.user_id},
                    status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
def profile(request):
    id = request.data.get("user_id")
    if id is None :
        return Response({'error': 'Please provide user id'},
                        status=HTTP_400_BAD_REQUEST)
    userInfo = User.objects.get(id=id)
    if not userInfo:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    return Response({'email': userInfo.email, 'name': userInfo.username},
                    status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
def task_assign(request):
    assign_by = request.data.get("assign_by")
    assign_to = request.data.get("assign_to")
    project_id = request.data.get("project_id")
    task = request.data.get("task")
    priority = request.data.get("priority")
    timeline = request.data.get("timeline")
    remark = request.data.get("remark")
    assign_date = request.data.get("assign_date")

    if assign_by is None or assign_to is None:
        return Response({'error': 'Please provide all fields'},
                        status=HTTP_400_BAD_REQUEST)
    taskAssign = Task(project = project_id, assign_by = assign_by, assign_to = assign_to, task = task, priority = priority, remarks = remark, status = "", assign_date = assign_date, time_line = timeline)
    taskAssign.save()
    if not taskAssign:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    return Response({'message': "Task assign to {}".format(assign_to)},
                    status=HTTP_200_OK)


"""
@permission_classes((AllowAny,))
class UserViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows users to be viewed or edited.
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@permission_classes((AllowAny,))
class GroupViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows groups to be viewed or edited.
   
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""


def index(request):
    return HttpResponse("No views found")