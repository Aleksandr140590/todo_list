from django.contrib import admin


class ToDoAdmin(admin.ModelAdmin):
    """Регистрация модели в админке."""
    list_display = '__all__'
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'
