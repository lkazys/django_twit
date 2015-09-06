from django.contrib import admin

# Register your models here.
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['user', 'text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

admin.site.register(Tweet, TweetAdmin)
