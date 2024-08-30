from django_filters.rest_framework import DjangoFilterBackend
from .models import Voter, Plan, Category, Vote_log, Latest_vote
from django.db.models import Count
from rest_framework import viewsets, views, filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import VoterCheck_serializer, VoteLog_serializer, Category_serializer, Plan_serializer, Voter_serializer, LatestVote_serializer, Totalling_serializer

class VoterView(views.APIView):
    def get(self, request, *args, **kwargs):
        req = {"user_id":self.request.query_params.get('user_id')}
        return Response(VoterCheck_serializer(req).data)
    def post(self, request, *args, **kwargs):
        serializer = Voter_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result':True})
        else:
            return Response({'result':False})
    
class VoteView(views.APIView):
    def post(self, request, *args, **kwargs):
        response_data = {
            "succeed":False,
            "comment":"None",
            "valid_vote":False,
            "valid_plans":[]
        }
        if Voter.objects.filter(user_id=request.data["user_id"]).exists():
            response_data["valid_vote"] = True
            i=1
            for id in request.data["plans"]:
                log_serializer = VoteLog_serializer(data={
                    "user":request.data["user_id"],
                    "plan":id
                })
                if log_serializer.is_valid():
                    log_serializer.save()
                    new_log = Vote_log.objects.filter(user_id=request.data["user_id"],plan_id=id).order_by('-created_at')[0]
                    if Latest_vote.objects.filter(user_id=request.data["user_id"], number=i).exists():
                        latest_serializer = LatestVote_serializer(
                            Latest_vote.objects.filter(user_id=request.data["user_id"], number=i)[0],
                            data={
                                "user":request.data["user_id"],
                                "vote_log":new_log.pk,
                                "number":i
                            })
                    else:
                        latest_serializer = LatestVote_serializer(
                            data={
                                "user":request.data["user_id"],
                                "vote_log":new_log.pk,
                                "number":i
                            })
                    if latest_serializer.is_valid():
                        response_data["valid_plans"].append(True)
                        latest_serializer.save()
                    else:
                        print(latest_serializer.errors)
                        response_data["valid_plans"].append(False)
                else:
                    print(log_serializer.errors)
                    response_data["valid_plans"].append(False)
                i+=1
            if not all(response_data["valid_plans"]):
                response_data["comment"] = "unvalid_plan error"
            else:
                response_data["succeed"] = True
        else:
            response_data["comment"] = "unvalid_voter error"
        return Response(response_data)

class TotallingView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Totalling_serializer
        
class StaffCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = Category_serializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class StaffPlanViewSet(viewsets.ModelViewSet):
    serializer_class = Plan_serializer
    queryset = Plan.objects.all()
    permission_classes = [IsAuthenticated]

class StaffVoterViewSet(viewsets.ModelViewSet):
    serializer_class = Voter_serializer
    queryset = Voter.objects.all()
    permission_classes = [IsAuthenticated]

class StaffVoteLogViewSet(viewsets.ModelViewSet):
    serializer_class = VoteLog_serializer
    queryset = Vote_log.objects.all()
    permission_classes = [IsAuthenticated]

class StaffLatestVoteViewSet(viewsets.ModelViewSet):
    serializer_class = LatestVote_serializer
    queryset = Latest_vote.objects.all()
    permission_classes = [IsAuthenticated]
