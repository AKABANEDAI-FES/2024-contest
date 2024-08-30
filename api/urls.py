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
    path("api/v1/", include(router.urls)),
    path("api/v1/voter/", apis.VoterView.as_view(), name="voter"),
    path('api/v1/vote/', apis.VoteView.as_view(), name="vote"),
    path('api/v1/total/', apis.TotallingView.as_view(), name="total")
]
