from django.contrib import admin
from .models import Post, Comment, Industry,Company, Role

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Industry)
admin.site.register(Company)
admin.site.register(Role)
