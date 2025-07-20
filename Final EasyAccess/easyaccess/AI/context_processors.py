# context_processors.py
from .models import history

def user_history(request):
    if request.user.is_authenticated:
        user_history = history.objects.filter(user=request.user).order_by('-accessed_at')[:10]
    else:
        user_history = []
    return {'user_history': user_history}
