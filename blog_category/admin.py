from django.contrib import admin
from blog_category.models import Blogs, Category, Comment



# to modify and show the columns in the list_display
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','created_at','updated_at']
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','category','blog_image','is_featured')
    prepopulated_fields = {'slug':('title',)}
    search_fields=('id','title','category__category_name')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Comment)
