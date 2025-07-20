from django.contrib import admin
from .models import documentation , AITool , history , HomeData , DataFeedback , category
from Accounts.models import UserOTP

# Register your models here.

admin.site.register(category)
admin.site.register(documentation)
admin.site.register(AITool)
admin.site.register(history)
admin.site.register(HomeData)
admin.site.register(DataFeedback)
admin.site.register(UserOTP)


