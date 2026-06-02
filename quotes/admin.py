from .models import Quote, Message, ContactInquiry
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Quote
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'receiver', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('subject', 'message', 'sender__username')
    readonly_fields = ('created_at',)
    
@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_replied')
    list_filter = ('is_replied', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_replied',)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'project_title', 'service_type', 'location', 'get_status', 'get_contact_buttons', 'created_at')
    list_filter = ('status', 'service_type', 'created_at')
    search_fields = ('project_title', 'user__username', 'user__email', 'location', 'description')
    readonly_fields = ('user', 'created_at')
    list_per_page = 20
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Client'
    
    def get_status(self, obj):
        status_colors = {
            'pending': '#f39c12',
            'reviewed': '#3498db',
            'approved': '#27ae60',
            'rejected': '#e74c3c'
        }
        color = status_colors.get(obj.status, '#95a5a6')
        return mark_safe(f'<span style="background: {color}; color: white; padding: 5px 10px; border-radius: 5px; font-size: 12px;">{obj.get_status_display().upper()}</span>')
    get_status.short_description = 'Status'
    
    def get_contact_buttons(self, obj):
        phone = ''
        email = ''
        
        # Try to get phone from profile
        if hasattr(obj.user, 'profile') and obj.user.profile.phone:
            phone = obj.user.profile.phone
        
        email = obj.user.email if obj.user.email else ''
        
        buttons_html = ''
        
        # WhatsApp button
        if phone:
            clean_phone = ''.join(filter(str.isdigit, phone))
            if clean_phone.startswith('0'):
                clean_phone = '255' + clean_phone[1:]
            buttons_html += f'<a href="https://wa.me/{clean_phone}" target="_blank" style="background: #25D366; color: white; padding: 4px 10px; margin: 2px; border-radius: 3px; text-decoration: none; display: inline-block; font-size: 11px;">💬 WhatsApp</a>'
            buttons_html += f'<a href="tel:{phone}" style="background: #3498db; color: white; padding: 4px 10px; margin: 2px; border-radius: 3px; text-decoration: none; display: inline-block; font-size: 11px;">📞 Call</a>'
        
        # Email button
        if email:
            buttons_html += f'<a href="mailto:{email}" style="background: #e94560; color: white; padding: 4px 10px; margin: 2px; border-radius: 3px; text-decoration: none; display: inline-block; font-size: 11px;">✉️ Email</a>'
        
        if buttons_html:
            return mark_safe(f'<div style="display: flex; flex-wrap: wrap; gap: 5px;">{buttons_html}</div>')
        return mark_safe('<span style="color: gray;">No contact info</span>')
    
    get_contact_buttons.short_description = 'Contact'

admin.site.register(Quote, QuoteAdmin)