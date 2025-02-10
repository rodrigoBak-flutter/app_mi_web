from django.shortcuts import render
from django.http import HttpResponse
from base.models import Articles
from base.forms import FormContact
from django.core.mail import send_mail
#from django.conf import settings

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

def contact(request):
    if request.method=="POST":
        contactForm=FormContact(request.POST)
        
        if contactForm.is_valid():
            infForm = contactForm.cleaned_data
            send_mail(infForm["issue"],infForm["message"],
            infForm.get('email',''),["test@test.com"],)
            
            return render(request, "thanks.html")
             
    else:
        contactForm=FormContact()
        return render(request, "contact_form.html" ,{"form": contactForm}) 
    
    
        ##LO SIGUIENTE ES DE MANERA MANUAL
        ##ANTES TENGO QUE CONFIGURAR EL CORREO PARA PODER RECIBIR ESTOS CORREOS
        #subject= request.POST["issue"]
        #message= request.POST["message"] + " " + request.POST["email"]
        #email_from=  settings.EMAIL_HOST_USER
        #recipient_list = ["DONDE_QUIERO_QUE_ME_LLEGUE_EL_MENSAJE"]
        #send_mail(subject, message, email_from, recipient_list)
      ##  return render(request, "thanks.html")

  ##  return render(request, "contact.html")
