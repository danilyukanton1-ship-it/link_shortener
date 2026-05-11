from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from links.models import Link
from links.api.serializers import LinkSerializer
from links.services import generate_short_code
from rest_framework import status


class CreateLinkView(APIView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        original_url = request.data.get('original_url')

        if not original_url:
            return Response(
                {'error': 'original_url is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        existing_link = Link.objects.filter(original_url=original_url).first()
        if existing_link:
            serializer = LinkSerializer(existing_link, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        short_code = generate_short_code()
        link = Link.objects.create(original_url=original_url, short_code=short_code)
        serializer = LinkSerializer(link, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LinkRedirectView(APIView):

    def get(self, request, short_code):
        link = get_object_or_404(Link, short_code=short_code)
        link.clicks += 1
        link.save()
        return redirect(link.original_url)

class ListStatsView(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'short_code'
