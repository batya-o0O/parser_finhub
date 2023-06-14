from rest_framework.serializers import ModelSerializer
from parser.models import Quote

class QuoteSerializaer(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'