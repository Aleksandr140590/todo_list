from django.contrib import admin


class TodoAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'
