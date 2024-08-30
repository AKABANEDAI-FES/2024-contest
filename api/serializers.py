from rest_framework import serializers
from .models import Voters, Plans, Category, Vote_logs, Latest_votes

class VotersCheck_serializer(serializers.Serializer):
    valied_vote = serializers.SerializerMethodField()
    voted = serializers.SerializerMethodField()
    voted_plans = serializers.SerializerMethodField()

    def get_valied_vote(self, obj):
        if Voters.objects.filter(user_id=obj["user_id"]).exists():
            return True
        else:
            return False
        
    def get_voted(self, obj):
        if Latest_votes.objects.filter(user_id=obj["user_id"]).count()>=3:
            return True
        else:
            return False
        
    def get_voted_plans(self, obj):
        latest_votes = Latest_votes.objects.filter(user_id=obj["user_id"]).order_by('number')
        rslt = []
        for latest_vote in latest_votes:
            rslt.append(latest_vote.vote_logs_id.plan_id.plan_id)
        return rslt
    
class Voters_serializer(serializers.ModelSerializer):
    class Meta:
        model = Voters
        fields = '__all__'
    
class VoteLogs_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vote_logs
        fields = '__all__'

class LatestVotes_serializer(serializers.ModelSerializer):
    class Meta:
        model = Latest_votes
        fields = '__all__'

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Plans_serializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'