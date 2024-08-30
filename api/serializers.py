from rest_framework import serializers
from .models import Voter, Plan, Category, Vote_log, Latest_vote

class VoterCheck_serializer(serializers.Serializer):
    valied_vote = serializers.SerializerMethodField()
    voted = serializers.SerializerMethodField()
    voted_plans = serializers.SerializerMethodField()

    def get_valied_vote(self, obj):
        if Voter.objects.filter(user_id=obj["user_id"]).exists():
            return True
        else:
            return False
        
    def get_voted(self, obj):
        if Latest_vote.objects.filter(user_id=obj["user_id"]).count()>=3:
            return True
        else:
            return False
        
    def get_voted_plans(self, obj):
        latest_votes = Latest_vote.objects.filter(user_id=obj["user_id"]).order_by('number')
        rslt = []
        for latest_vote in latest_votes:
            rslt.append(latest_vote.vote_log.plan.pk)
        return rslt
    
class Totalling_serializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Latest_vote
        fields = '__all__'
    
class Voter_serializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'
    
class VoteLog_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vote_log
        fields = '__all__'

class LatestVote_serializer(serializers.ModelSerializer):
    class Meta:
        model = Latest_vote
        fields = '__all__'

class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Plan_serializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class PlanVote_serializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField()

    class Meta:
        model = Plan
        fields = ['plan_id', 'title', 'vote_count']

class Totalling_serializer(serializers.ModelSerializer):
    plans = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['category_id', 'title', 'plans']

    def get_plans(self, obj):
        plans = Plan.objects.filter(category=obj)
        serialized_plans = []

        for plan in plans:
            vote_count = Latest_vote.objects.filter(vote_log__plan=plan).count()
            serialized_plans.append({
                'plan_id': plan.plan_id,
                'title': plan.title,
                'vote_count': vote_count
            })

        return PlanVote_serializer(serialized_plans, many=True).data
