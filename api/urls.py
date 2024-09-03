from django.urls import path, include
from . import apis
from rest_framework import routers

router = routers.DefaultRouter()
router.register('staff-category', apis.StaffCategoryViewSet)
router.register('staff-plan', apis.StaffPlanViewSet)
router.register('staff-voter', apis.StaffVoterViewSet)
router.register('staff-votelog', apis.StaffVoteLogViewSet)
router.register('staff-latestvote', apis.StaffLatestVoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("voter/", apis.VoterView.as_view(), name="voter"),
    path('vote/', apis.VoteView.as_view(), name="vote"),
    path('total/', apis.TotallingView.as_view(), name="total")
]
