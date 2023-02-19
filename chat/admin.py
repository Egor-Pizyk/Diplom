from django.contrib import admin

from chat.models import Chat, ChatMessage


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass
