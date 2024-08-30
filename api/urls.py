from django.urls import path, include
from . import apis
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stuff-category', apis.StuffCategoryViewSet)
router.register('stuff-plans', apis.StuffPlansViewSet)
router.register('stuff-voters', apis.StuffVotersViewSet)
router.register('stuff-votelogs', apis.StuffVoteLogsViewSet)
router.register('stuff-latestvotes', apis.StuffLatestVotesViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/voters/<int:pk>/", apis.VotersView.as_view(), name="voters"),
    path('api/vote/', apis.VoteView.as_view(), name="vote"),
]