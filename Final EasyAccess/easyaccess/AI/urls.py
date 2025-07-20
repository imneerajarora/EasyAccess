from django.urls import path 
from . import views
# from Accounts import views
from Accounts.views import register , loginview  , logoutview , verify_otp

urlpatterns = [
    path('',views.home , name='home'),
    path('register/',register , name='register'),
    path('verify_otp/<int:user_id>/',verify_otp , name='verify_otp'),
    path('AITool/',views.AIToolview,name='AIToolview'),
    path('Documentation/',views.Documentation,name='Documentation'),
    path('About/',views.Aboutview,name='About'),
    path('tutorial/',views.tutorial,name='tutorial'),
    path('feedbacks/',views.Feedback_view,name='feedback_view'),
    path('feedback-create/',views.feedback_create,name='feedback_create'),
    path('history/', views.history_create, name='history_create'),
    path('clearhistory/', views.clear_history_view, name='ClearHistory'),
    path('search/', views.search_results, name='search_results'),
    path('login/',loginview,name='loginview'),
    path('logout/',logoutview,name='logout'),
   
    # path('search/',views.search_detail,name='search'),




]