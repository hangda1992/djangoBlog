from django.contrib import admin
from blog.models import Article
from blog.models import BlogAccountManagement
# Register your models here.


@admin.register(BlogAccountManagement)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('nid', 'account_name', 'account_number', 'account_email', 'account_url')
    list_display_links = ('nid', 'account_name')
    list_filter = ('account_name',)
    list_per_page = 50


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_time_c', 'article_time_u', 'article_label', 'article_title', 'article_img',
                    'article_content')