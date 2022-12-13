from django.db import models


class ChatMessage(models.Model):
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE, related_name="messages")
    username = models.CharField(max_length=221)
    text = models.TextField()

    def __str__(self):
        return f"{self.chat.room_name}-{self.username}"
