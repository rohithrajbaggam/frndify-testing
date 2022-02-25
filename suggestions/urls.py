from django.urls import path
from . import views 

urlpatterns = [ 
    # popular suggestions
    path('CSE/', views.cse, name='branch-cse'),
    path('AP/', views.AP, name='AP'),
    path('Zakir B/', views.zkb_hostel, name='zk-b'),
    path('telugu/', views.telugu, name='telugu'),
    # user suggestions
    path('<branch>/', views.branch_sug, name='branch-sug'),
    path('hostel/<hostel_name>/', views.hostel_sug, name='hostel-sug'),
    path('state/<state>/', views.State_sug, name='state-sug'),
    path('language/<Native_Language>/', views.native_language_sug, name='native-language-sug'),

]