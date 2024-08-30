from django.db import models

class Voters(models.Model):
    user_id = models.IntegerField(primary_key=True)

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50) # example 食品部門

class Plans(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    # 3~4 digit xxyy
    # xx = 1~2digit page number
    # yy = 2digit Plan number 
    # example leaflet 3page 15th Plan ==> 315
    # example leaflet 30page 5th Plan ==> 3005
    title = models.CharField(max_length=50) # example ARイニャー
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Vote_logs(models.Model):
    user_id = models.ForeignKey(Voters, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plans, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Latest_votes(models.Model):
    user_id = models.ForeignKey(Voters, on_delete=models.CASCADE)
    vote_logs_id = models.ForeignKey(Vote_logs, on_delete=models.CASCADE)
    number = models.IntegerField() # votes_max=3 ==> number=1~3

# Create your models here.
