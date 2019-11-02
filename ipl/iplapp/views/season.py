from django.http import HttpResponse
from django.views import View
from iplapp.models import *
from django.shortcuts import render,redirect
from django.urls import resolve
from django.contrib.auth.mixins import LoginRequiredMixin


class displaySeasonPage(View):
    login_url=''

    def get(self,request):
        seasonsDetails = matches.objects.filter(season=2019).all()
        # print(seasonsDetails.values())
        # print(seasonsDetails[1].season)
        return render(
            request,
            template_name='iplapp/seasonPage.html',
            context={'seasonsDetails': seasonsDetails,}
        )
    def post(self,request):
        year = request.POST['season_year']

        yearDetails = matches.objects.filter(season=year).all()



        return render(request,template_name='iplapp/seasonPage.html',context={'seasonsDetails':yearDetails})

class displayMatchDetails(View):
    login_url=''

    def get(self,request,*args,**kwargs):
        match_id=kwargs["pk"]
        seasonsDetails = matches.objects.filter(id=match_id).all()
        matchDetails = deliveries.objects.filter(match_id=match_id).all()
        return render(
            request,
            template_name='iplapp/matchPage.html',
            context={'seasonsDetails': seasonsDetails,
                     'matchDetails':matchDetails,
                     }
        )


    # def post(self,request):
    #     image_name = request.POST['pic']
    #     image_name = '/Users/manasasingh/Desktop/Images/Input_Image/'+image_name
    #     n_share = request.POST['n_shares']
    #     k_share = request.POST['k_shares']
    #     encrypt_key = request.POST['user_key']
    #     email_id = request.POST['mail_ids']
    #     email_id_list=email_id.split("\r\n")
    #     divideToNShare(image_name, n_share, k_share, encrypt_key,email_id_list)
    #
    #     return HttpResponse("<h1> SHARES SEND TO YOUR EMAIL")


