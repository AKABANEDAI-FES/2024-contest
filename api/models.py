from django.db import models

class Voter(models.Model):
    user_id = models.IntegerField(primary_key=True)
    class Meta:
       verbose_name_plural = "有権者"
    def __str__(self):
        return str(self.user_id)

class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50) # example 食品部門
    class Meta:
       verbose_name_plural = "カテゴリ"
    def __str__(self):
        return self.title

class Plan(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    # 3~4 digit xxyy
    # xx = 1~2digit page number
    # yy = 2digit Plan number 
    # example leaflet 3page 15th Plan ==> 315
    # example leaflet 30page 5th Plan ==> 3005
    title = models.CharField(max_length=50) # example ARイニャー
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
       verbose_name_plural = "企画"
    def __str__(self):
        return self.title

class Vote_log(models.Model):
    user = models.ForeignKey(Voter, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
       verbose_name_plural = "投票履歴"
    def __str__(self):
        return f'{self.user}, {self.plan}'

class Latest_vote(models.Model):
    user = models.ForeignKey(Voter, on_delete=models.CASCADE)
    vote_log = models.ForeignKey(Vote_log, on_delete=models.CASCADE)
    number = models.IntegerField() # votes_max=3 ==> number=1~3
    class Meta:
       verbose_name_plural = "最新投票"
    def __str__(self):
        return f'{self.vote_log}'
