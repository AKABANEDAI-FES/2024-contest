from django.urls import path, include
from . import apis
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stuff-category', apis.StaffCategoryViewSet)
router.register('stuff-plan', apis.StaffPlanViewSet)
router.register('stuff-voter', apis.StaffVoterViewSet)
router.register('stuff-votelog', apis.StaffVoteLogViewSet)
router.register('stuff-latestvote', apis.StaffLatestVoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("voter/", apis.VoterView.as_view(), name="voter"),
    path('vote/', apis.VoteView.as_view(), name="vote"),
    path('total/', apis.TotallingView.as_view(), name="total")
]
