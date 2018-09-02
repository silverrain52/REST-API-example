from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializers import FinanceSerializer
from myapp.models import Finance

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
