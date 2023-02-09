from rest_framework import serializers
from viewer.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = '__all__'


