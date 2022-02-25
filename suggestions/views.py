from django.shortcuts import render
from users.models import UserProfile
from django.db.models import Q
# Create your views here.

# profile 

# user data suggestions
def branch_sug(request, branch):
    user_profile_data = UserProfile.objects.filter(Q(Branch__icontains=branch))
    context = { 
        'data' : branch,
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)


def State_sug(request, state):
    user_profile_data = UserProfile.objects.filter(Q(State__icontains=request.user.user_profile.State))
    context = {
        'data' : state,
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)


def hostel_sug(request, hostel_name):
    user_profile_data = UserProfile.objects.filter(Q(Hosteler_or_DayScholar__icontains=request.user.user_profile.Hosteler_or_DayScholar))
    context = {
        'data' : request.user.user_profile.Hosteler_or_DayScholar,
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)


def native_language_sug(request, Native_Language):
    user_profile_data = UserProfile.objects.filter(Q(Native_Language__icontains=request.user.user_profile.Native_Language))
    context = {
        'data' : Native_Language,
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)


# popular suggestions

def cse(request):
    user_profile_data = UserProfile.objects.filter(Q(Branch__icontains='Bachelor of Computer Science Engineering'))
    context = {
        'data' : 'CSE',
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context) 


def zkb_hostel(request):
    user_profile_data = UserProfile.objects.filter(Q(Hosteler_or_DayScholar__icontains="Zakir B"))
    context = {
        'data' : "Zakir B",
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)


def AP(request):
    user_profile_data = UserProfile.objects.filter(Q(State__icontains="Andhra Pradesh"))
    context = {
        'data' : "Andhra Pradesh",
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)


def telugu(request):
    user_profile_data = UserProfile.objects.filter(Q(Native_Language__icontains='Telugu'))
    context = {
        'data' : "Telugu",
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'user_sug/user_sugg.html', context)








