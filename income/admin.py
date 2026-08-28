from django.contrib import admin
from django.utils.html import format_html
from .models import IncomeCategory, Income


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    """
    Highly customized Admin dashboard for IncomeCategory
    """
    save_on_top = True
    list_per_page = 50
    date_hierarchy = 'created_at' if hasattr(IncomeCategory, 'created_at') else None
    
    # Introspect fields to build realistic list_display
    def get_list_display(self, request):
        fields = [f.name for f in self.model._meta.fields if f.name != 'password']
        # Add a custom action column
        return fields + ['admin_actions']
        
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">View</a>&nbsp;'
            '<a class="button" href="{}">Edit</a>',
            f"/admin/income/incomecategory/{obj.pk}/change/",
            f"/admin/income/incomecategory/{obj.pk}/change/"
        )
    admin_actions.short_description = 'Actions'
    admin_actions.allow_tags = True
    
    def get_list_filter(self, request):
        filters = []
        for f in self.model._meta.fields:
            if f.get_internal_type() in ['BooleanField', 'CharField', 'DateField', 'DateTimeField'] and not f.unique:
                filters.append(f.name)
        return filters[:5]  # Top 5 filters
        
    def get_search_fields(self, request):
        searchable = []
        for f in self.model._meta.fields:
            if f.get_internal_type() in ['CharField', 'TextField', 'EmailField']:
                searchable.append(f.name)
        return searchable
        
    def get_readonly_fields(self, request, obj=None):
        if obj: # Editing an existing object
            return ['created_at', 'updated_at'] if hasattr(self.model, 'created_at') else []
        return []
        
    actions = ['export_as_csv', 'mark_as_active', 'mark_as_inactive']
    
    @admin.action(description="Export selected items as CSV")
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta.model_name}s.csv'
        writer = csv.writer(response)
        
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
            
        return response
        
    @admin.action(description="Mark selected as Active")
    def mark_as_active(self, request, queryset):
        if hasattr(self.model, 'is_active'):
            updated = queryset.update(is_active=True)
            self.message_user(request, f"Successfully activated {updated} records.")
        else:
            self.message_user(request, "This model does not have an is_active field.", level='ERROR')
            
    @admin.action(description="Mark selected as Inactive")
    def mark_as_inactive(self, request, queryset):
        if hasattr(self.model, 'is_active'):
            updated = queryset.update(is_active=False)
            self.message_user(request, f"Successfully deactivated {updated} records.")
        else:
            self.message_user(request, "This model does not have an is_active field.", level='ERROR')

    def get_fieldsets(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields if f.name not in ['id', 'created_at', 'updated_at']]
        
        # Split fields into logical groupings based on type
        basic_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['CharField', 'EmailField']]
        number_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['IntegerField', 'DecimalField', 'FloatField']]
        date_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['DateField', 'DateTimeField']]
        rel_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['ForeignKey', 'OneToOneField', 'ManyToManyField']]
        other_fields = [f for f in fields if f not in basic_fields + number_fields + date_fields + rel_fields]
        
        fieldsets = []
        if basic_fields:
            fieldsets.append(('Basic Information', {'fields': basic_fields}))
        if number_fields:
            fieldsets.append(('Metrics & Values', {'fields': number_fields}))
        if date_fields:
            fieldsets.append(('Dates & Timestamps', {'fields': date_fields}))
        if rel_fields:
            fieldsets.append(('Relationships', {'fields': rel_fields}))
        if other_fields:
            fieldsets.append(('Additional Details', {'fields': other_fields}))
            
        if not fieldsets:
            fieldsets = [(None, {'fields': fields})]
            
        return fieldsets

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    """
    Highly customized Admin dashboard for Income
    """
    save_on_top = True
    list_per_page = 50
    date_hierarchy = 'created_at' if hasattr(Income, 'created_at') else None
    
    # Introspect fields to build realistic list_display
    def get_list_display(self, request):
        fields = [f.name for f in self.model._meta.fields if f.name != 'password']
        # Add a custom action column
        return fields + ['admin_actions']
        
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">View</a>&nbsp;'
            '<a class="button" href="{}">Edit</a>',
            f"/admin/income/income/{obj.pk}/change/",
            f"/admin/income/income/{obj.pk}/change/"
        )
    admin_actions.short_description = 'Actions'
    admin_actions.allow_tags = True
    
    def get_list_filter(self, request):
        filters = []
        for f in self.model._meta.fields:
            if f.get_internal_type() in ['BooleanField', 'CharField', 'DateField', 'DateTimeField'] and not f.unique:
                filters.append(f.name)
        return filters[:5]  # Top 5 filters
        
    def get_search_fields(self, request):
        searchable = []
        for f in self.model._meta.fields:
            if f.get_internal_type() in ['CharField', 'TextField', 'EmailField']:
                searchable.append(f.name)
        return searchable
        
    def get_readonly_fields(self, request, obj=None):
        if obj: # Editing an existing object
            return ['created_at', 'updated_at'] if hasattr(self.model, 'created_at') else []
        return []
        
    actions = ['export_as_csv', 'mark_as_active', 'mark_as_inactive']
    
    @admin.action(description="Export selected items as CSV")
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta.model_name}s.csv'
        writer = csv.writer(response)
        
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
            
        return response
        
    @admin.action(description="Mark selected as Active")
    def mark_as_active(self, request, queryset):
        if hasattr(self.model, 'is_active'):
            updated = queryset.update(is_active=True)
            self.message_user(request, f"Successfully activated {updated} records.")
        else:
            self.message_user(request, "This model does not have an is_active field.", level='ERROR')
            
    @admin.action(description="Mark selected as Inactive")
    def mark_as_inactive(self, request, queryset):
        if hasattr(self.model, 'is_active'):
            updated = queryset.update(is_active=False)
            self.message_user(request, f"Successfully deactivated {updated} records.")
        else:
            self.message_user(request, "This model does not have an is_active field.", level='ERROR')

    def get_fieldsets(self, request, obj=None):
        fields = [f.name for f in self.model._meta.fields if f.name not in ['id', 'created_at', 'updated_at']]
        
        # Split fields into logical groupings based on type
        basic_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['CharField', 'EmailField']]
        number_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['IntegerField', 'DecimalField', 'FloatField']]
        date_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['DateField', 'DateTimeField']]
        rel_fields = [f for f in fields if self.model._meta.get_field(f).get_internal_type() in ['ForeignKey', 'OneToOneField', 'ManyToManyField']]
        other_fields = [f for f in fields if f not in basic_fields + number_fields + date_fields + rel_fields]
        
        fieldsets = []
        if basic_fields:
            fieldsets.append(('Basic Information', {'fields': basic_fields}))
        if number_fields:
            fieldsets.append(('Metrics & Values', {'fields': number_fields}))
        if date_fields:
            fieldsets.append(('Dates & Timestamps', {'fields': date_fields}))
        if rel_fields:
            fieldsets.append(('Relationships', {'fields': rel_fields}))
        if other_fields:
            fieldsets.append(('Additional Details', {'fields': other_fields}))
            
        if not fieldsets:
            fieldsets = [(None, {'fields': fields})]
            
        return fieldsets
