from django.contrib import admin
from .models import Small, Manfor, Womanfor, Bigges, Watch, Komputer, Koylak
# Register your models here.
admin.site.register(Bigges)
admin.site.register(Manfor)

@admin.register(Small)
class SmallAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Komputer)
class KomputerAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio', 'date']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Koylak)
class KoylakAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio', 'date']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Womanfor)
class WomanforAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    prepopulated_fields = {'slug': ('name',)}