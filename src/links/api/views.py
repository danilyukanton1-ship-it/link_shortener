from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from links.models import Link
from links.api.serializers import LinkSerializer
from links.services import generate_short_code

class CreateLinkView(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        short_code = generate_short_code()
        serializer.save(short_code=short_code)

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
