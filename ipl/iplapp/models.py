# Create your models here.
from django.db import models
# import django
# import  os
# Create your models here.
# from django.db import models
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','ipl.settings')
# django.setup()

# Create your models here.
class matches(models.Model):

    id=models.IntegerField(primary_key=True)
    season=models.IntegerField(null=True)
    city=models.CharField(null=True,max_length=150)
    date=models.DateField(null=True,blank=True)
    team1=models.CharField(null=True,max_length=150)
    team2=models.CharField(null=True,max_length=150)
    toss_winner=models.CharField(null=True,max_length=150)
    toss_decision=models.CharField(null=True,max_length=150)
    result=models.CharField(null=True,max_length=150)
    dl_applied=models.IntegerField(null=True,default=0)
    winner=models.CharField(null=True,max_length=150)
    win_by_run=models.IntegerField(null=True,default=0)
    win_by_wicket=models.IntegerField(null=True,default=0)
    player_of_match=models.CharField(null=True,max_length=150)
    venue=models.CharField(null=True,max_length=150)
    umpire1=models.CharField(null=True,max_length=150)
    umpire2=models.CharField(null=True,max_length=150)
    umpire3=models.CharField(null=True,max_length=150)

    def __str__(self):
        return self.team1 +" vs " +self.team2

class deliveries(models.Model):

    match_id=models.ForeignKey(matches, on_delete=models.CASCADE)
    inning=models.IntegerField(null=True)
    batting_team=models.CharField(null=True,max_length=150)
    bowling_team=models.CharField(null=True,max_length=150)
    over=models.IntegerField(null=True,default=0)
    ball=models.IntegerField(null=True,default=0)
    batsman=models.CharField(null=True,max_length=150)
    non_striker=models.CharField(null=True,max_length=150)
    bowler=models.CharField(null=True,max_length=150)

    is_super_over=models.IntegerField(null=True,default=0)
    wide_runs=models.IntegerField(null=True,default=0)
    bye_runs=models.IntegerField(null=True,default=0)
    legbye_runs=models.IntegerField(null=True,default=0)
    noball_runs=models.IntegerField(null=True,default=0)
    penalty_runs=models.IntegerField(null=True,default=0)
    batsman_runs=models.IntegerField(null=True,default=0)
    extra_runs=models.IntegerField(null=True,default=0)
    total_runs=models.IntegerField(null=True,default=0)

    player_dismissed=models.CharField(null=True,max_length=150)
    dismissal_kind=models.CharField(null=True,max_length=150)
    fielder=models.CharField(null=True,max_length=150)




