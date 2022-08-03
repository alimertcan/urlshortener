from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from .serializer import UrlSerializer
from .models import Url
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib, string, random


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'To Short Url': '/short_url',
        'List of short urls': '/short_url_list',
        'Call short url': 'Ex:\'/2Huotasdew3\''
    }
    return Response(api_urls)


@swagger_auto_schema(method='post', request_body=UrlSerializer)
@api_view(['POST'])
def add_url(request):
    item = UrlSerializer(data=request.data)
    # validating for already existing data
    get_data = Url.objects.filter(**request.data)
    if get_data.exists():
        serialzer = UrlSerializer(get_data, many=True)
        # raise UrlSerializer.ValidationError('This data already exists')
        return Response(serialzer.data,status=status.HTTP_409_CONFLICT)
    if item.is_valid():
        item.save()
        data = {"generated_url":f"http://{request.get_host()}/{item.data.get('generated_url')}"}
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_url(request):
    items = Url.objects.all()

    # if there is something in items else raise error
    if items:
        serialzer = UrlSerializer(items, many=True)
        # serialzer
        return Response(serialzer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def redirect_url(request, slug):
    item = get_object_or_404(Url, generated_url=slug)
    # if there is something in items else raise error
    if item:
        item.view_count += 1
        item.save()
        return redirect(item.real_url)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
