from django.contrib import admin
from base.models import Client, Articles, Orders

#Agregar un campo mas en la tabla
class ClientAdmin(admin.ModelAdmin):
    list_display=("name","address","email")
    #Agregar buscador
    search_fields=("name","email")
    
    

class ArticlesAdmin(admin.ModelAdmin):
    list_display=("name","section","price")
    search_fields=("name","section","price")
    #Agregar un filtro
    list_filter=("section",)
    
    

class OrdersAdmin(admin.ModelAdmin):
    list_display=("number","date","delivered")
    search_fields=("number","date","delivered")
    list_filter=("date",)
    date_hierarchy="date"

# Register your models here.

admin.site.register(Client, ClientAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Orders,OrdersAdmin)


