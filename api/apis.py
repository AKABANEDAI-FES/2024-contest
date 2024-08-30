from .models import Voters, Plans, Category, Vote_logs, Latest_votes
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import VotersCheck_serializer, VoteLogs_serializer, Category_serializer, Plans_serializer, Voters_serializer, LatestVotes_serializer

class VotersView(views.APIView):
    def get(self, request, *args, **kwargs):
        req = {"user_id":self.kwargs["pk"]}
        return Response(VotersCheck_serializer(req).data)
    def post(self, request, *args, **kwargs):
        serializer = Voters_serializer(data=request.data)
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
        if Voters.objects.filter(user_id=request.data["user_id"]).exists():
            response_data["valid_vote"] = True
            i=1
            for id in request.data["plans"]:
                log_serializer = VoteLogs_serializer(data={
                    "user_id":request.data["user_id"],
                    "plan_id":id
                })
                if log_serializer.is_valid():
                    log_serializer.save()
                    new_log = Vote_logs.objects.filter(user_id=request.data["user_id"],plan_id=id).order_by('-created_at')[0]
                    if Latest_votes.objects.filter(user_id=request.data["user_id"], number=i).exists():
                        latest_serializer = LatestVotes_serializer(
                            Latest_votes.objects.filter(user_id=request.data["user_id"], number=i)[0],
                            data={
                                "user_id":request.data["user_id"],
                                "vote_logs_id":new_log.pk,
                                "number":i
                            })
                    else:
                        latest_serializer = LatestVotes_serializer(
                            data={
                                "user_id":request.data["user_id"],
                                "vote_logs_id":new_log.pk,
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
        
class StuffCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = Category_serializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class StuffPlansViewSet(viewsets.ModelViewSet):
    serializer_class = Plans_serializer
    queryset = Plans.objects.all()
    permission_classes = [IsAuthenticated]

class StuffVotersViewSet(viewsets.ModelViewSet):
    serializer_class = Voters_serializer
    queryset = Voters.objects.all()
    permission_classes = [IsAuthenticated]

class StuffVoteLogsViewSet(viewsets.ModelViewSet):
    serializer_class = VoteLogs_serializer
    queryset = Vote_logs.objects.all()
    permission_classes = [IsAuthenticated]

class StuffLatestVotesViewSet(viewsets.ModelViewSet):
    serializer_class = LatestVotes_serializer
    queryset = Latest_votes.objects.all()
    permission_classes = [IsAuthenticated]