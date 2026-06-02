from django.contrib import admin
from django.utils.html import mark_safe
from .models import Post, Service, CaseStudy

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'location', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'client_name', 'location', 'problem', 'solution')
    list_editable = ('is_featured',)
    readonly_fields = ('created_at', 'image_preview', 'before_preview', 'after_preview')
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;"/>')
        return "No image"
    image_preview.short_description = 'Main Image'
    
    def before_preview(self, obj):
        if obj.before_image:
            return mark_safe(f'<img src="{obj.before_image.url}" style="max-height: 100px;"/>')
        return "No image"
    before_preview.short_description = 'Before'
    
    def after_preview(self, obj):
        if obj.after_image:
            return mark_safe(f'<img src="{obj.after_image.url}" style="max-height: 100px;"/>')
        return "No image"
    after_preview.short_description = 'After'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'client_name', 'location', 'is_featured')
        }),
        ('Problem & Solution', {
            'fields': ('problem', 'solution', 'results'),
            'classes': ('wide',)
        }),
        ('Images', {
            'fields': ('image', 'image_preview', 'before_image', 'before_preview', 'after_image', 'after_preview'),
            'classes': ('wide',)
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )