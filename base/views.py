from django.shortcuts import render
from django.http import HttpResponse
from base.models import Articles

# Create your views here.

def search_article(request):
    return render(request, "search_article.html")

def search(request):
    art = request.GET.get("article", "").strip() 

    if not art:  
        return HttpResponse("You haven't entered anything")

    if len(art) > 20:  
        return HttpResponse("Search text too long")  

    
    articles = Articles.objects.filter(name__icontains=art)
    return render(request, "result_search.html", {"articles": articles, "query": art})
