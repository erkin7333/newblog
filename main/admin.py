from django.contrib import admin
from .models import *




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)



class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'title',
                    'photo', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'cat', 'title')
    search_fields = ('title', 'content  ')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = New
admin.site.register(New, NewAdmin)
