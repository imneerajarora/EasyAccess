from django.shortcuts import render  , get_object_or_404 , redirect
from .models import documentation , AITool , history  , DataFeedback , category
from .forms import   FeedForm , SearchForm , CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    feed = DataFeedback.objects.all().order_by('-created_at')
    return render(request,'home.html',{'feed':feed})




# @login_required(login_url='loginview')
def AIToolview(request):
    AITools_list = AITool.objects.all()
    paginator = Paginator(AITools_list,8)  #show 8 Tools per page

    page_number = request.GET.get('page')
    AITools = paginator.get_page(page_number)
    
    if request.method == 'GET' and 'slug' in request.GET:
        slug = request.GET['slug']
        tool = get_object_or_404(AITool,slug=slug)
        history.objects.create(user=request.user, title=tool.title,item_type = 'AITool')
    return render(request,'AITool.html',{'AITools':AITools,'model':'AITool'})




def Documentation(request):
    documents = documentation.objects.all()

    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(category,slug=category_slug)
        documents = documents.filter(category=category)
    if request.method == 'GET' and 'slug' in request.GET:
        slug = request.GET['slug']
        doc = get_object_or_404(documentation,slug=slug)
        history.objects.create(user=request.user,title=doc.title,item_type='doucmentation')
    return render(request,'documentation.html',{'documents':documents,'model':'documentation'})





def Aboutview(request):
    return render(request,'about.html')






#This is feedback views operations.

def Feedback_view(request):
    feedback = DataFeedback.objects.all().order_by('-created_at')
    return render(request,'feedbackview.html',{'feedback':feedback})

@login_required(login_url='loginview')
def feedback_create(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        # print(form)
        if form.is_valid:
            form.save()
            return redirect('feedback_view')
    else:
        form = FeedForm()
    return render(request,'basic.html',{'form':form})


#this is user history showing operations

@login_required(login_url='loginview')
def history_create(request):
    if request.user.is_authenticated:
        title_link = request.GET.get('link')
        title_name = request.GET.get('title')
        if title_link:
            history.objects.create(user=request.user, title_link=title_link, title_name=title_name,accessed_at=now())
        return redirect(title_link)
    else:
        return redirect('login_view')

def history_view(request):
    if request.user.is_authenticated:
        user_history = history.objects.filter(user=request.user).order_by('-accessed_at')[:20]
        return render(request,'basic.html',{'user_history':user_history})
    else:
        return redirect('login_view')  #redirect to login if not authenticated
    

def clear_history_view(request):
    if request.user.is_authenticated:
        history.objects.filter(user=request.user).delete()
    return redirect('home')



#search option

def search_results(request):
    query = request.GET.get('query', '').strip()
    message = None
    aitools = documentation_results = None  # Default to 'AITool'
    if not query:
        message  = "please enter a search term."
    # Filter based on the query
    else:
            aitools = AITool.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            documentation_results = documentation.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            if not aitools and not documentation_results:
                message = f'No results found for "{query}".'

    context = { 'query': query,'AITools': aitools,'documents': documentation_results,'message':message}

    return render(request, 'search_results.html', context)



def tutorial(request):
    return render(request,'tutorial.html')