from rest_framework import serializers
from viewer.models import Portfolio_assets


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio_assets
        fields = '__all__'


