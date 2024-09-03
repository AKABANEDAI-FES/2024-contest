from django.contrib import admin
from .models import Voter, Category, Plan, Vote_log, Latest_vote

class VoterAdmin(admin.ModelAdmin):
    list_display = ('user_id',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'plan_id')
    list_filter = ('category',)
    search_fields = ('title',)
    ordering = ("plan_id", )

class VoteLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'created_at')
    ordering = ("-created_at", )

class LatestVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'number', 'updated_at')
    def updated_at(self, obj):
        return obj.vote_log.created_at

admin.site.register(Voter, VoterAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Vote_log, VoteLogAdmin)
admin.site.register(Latest_vote, LatestVoteAdmin)
