from django.db import models

class Voter(models.Model):
    user_id = models.IntegerField(primary_key=True)

class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50) # example 食品部門

class Plan(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    # 3~4 digit xxyy
    # xx = 1~2digit page number
    # yy = 2digit Plan number 
    # example leaflet 3page 15th Plan ==> 315
    # example leaflet 30page 5th Plan ==> 3005
    title = models.CharField(max_length=50) # example ARイニャー
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Vote_log(models.Model):
    user = models.ForeignKey(Voter, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Latest_vote(models.Model):
    user = models.ForeignKey(Voter, on_delete=models.CASCADE)
    vote_log = models.ForeignKey(Vote_log, on_delete=models.CASCADE)
    number = models.IntegerField() # votes_max=3 ==> number=1~3

# Create your models here.
