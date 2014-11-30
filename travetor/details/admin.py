from django.contrib import admin
from details.models import Trek, TrekCategory, Provider, Trek_date,TrekStyle
# Register your models here.

class TrekAdmin(admin.ModelAdmin):
	list_display=('trek_name','trek_state','trek_city','is_active',)
	list_display_links=('trek_name',)
	list_per_page=50
	ordering=['-trek_created_at']
	search_fields=['trek_name','trek_rating','duration']
	exclude=['trek_created_at',]
	prepopulated_fields={'trek_slug': ('trek_name',)}

class TrekCategoryAdmin(admin.ModelAdmin):
	list_display=('category_name','is_active',)
	list_display_links=('category_name',)
	list_per_page=20
	ordering=['category_name']
	search_fields=['category_name']
	exclude=('category_created_at',)
	prepopulated_fields={'category_slug': ('category_name',)}

class ProviderAdmin(admin.ModelAdmin):
	list_display=('provider_name',)

class TrekDateAdmin(admin.ModelAdmin):
	list_display=('date',)

class StyleAdmin(admin.ModelAdmin):
	list_display=('style',)

admin.site.register(TrekCategory,TrekCategoryAdmin)
admin.site.register(Trek,TrekAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(Trek_date,TrekDateAdmin)
admin.site.register(TrekStyle,StyleAdmin)
