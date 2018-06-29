from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import renderers
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.generics import get_object_or_404

from split.models import Profile, Relationship
from split.serializers import AuthUserSerializer, ProfileSerializer


def root(request):
    return HttpResponse("Welcome")


@csrf_exempt
@api_view(['POST'])
@permission_classes([])
@renderer_classes([renderers.JSONRenderer])
def register(request):
    if request.method == 'POST':
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=500)


@csrf_exempt
@api_view(['GET'])
@renderer_classes([renderers.JSONRenderer])
def get_profile(request):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, username=request.user.username)
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)


@csrf_exempt
@api_view(['POST'])
@renderer_classes([renderers.JSONRenderer])
def add_friend(request):
    if request.method == 'POST':
        source_user = get_object_or_404(Profile, username=request.user.username)
        user_to_add = get_object_or_404(Profile, username=request.POST.get('username'))

        if source_user.username != user_to_add.username:
            if source_user.friends.filter(friend=user_to_add).exists():
                return JsonResponse({'message': "Don't repeat add friend!"}, status=500)
        else:
            return JsonResponse({'message': 'You cannot add yourself'}, status=500)

        is_pending = True
        if source_user.requests_from.filter(user=user_to_add).exists():
            is_pending = False
            existed_relation = Relationship.objects.get(user=user_to_add, friend=source_user)
            existed_relation.is_pending = is_pending
            existed_relation.save()

        relationship = Relationship(user=source_user, friend=user_to_add, is_pending=is_pending)
        relationship.save()
        return JsonResponse({'message': 'Add successfully!'})
