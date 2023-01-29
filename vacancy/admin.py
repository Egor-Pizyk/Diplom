from django.contrib import admin

from vacancy.models import Vacancy, Chat, ChatMessage


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass
