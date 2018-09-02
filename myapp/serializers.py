from myapp.models import Finance
from rest_framework import serializers

class FinanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finance
        fields = ('country', 'standard', 'change_dollar')
