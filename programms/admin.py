from django.contrib import admin
from programms.models import Programms, TypeProgramms
# Register your models here.
# admin.site.register(Programms)
# admin.site.register(TypeProgramms)

@admin.register(Programms)
class ProgrammsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameProgramm', Programms.bodyProg, 'typeProgramm', 'is_checked')
    list_display_links = ('id', Programms.bodyProg, 'typeProgramm')
    search_fields = ('nameProgramm',)
    list_filter = ('typeProgramm',)
    ordering = ('id',)
    list_per_page = 10
    list_editable = ('nameProgramm', 'is_checked')
    actions = ['set_checked', 'unset_checked']

    @admin.action(description='Пометить как проверенное')
    def set_checked(self, request, queryset):
        update_count = queryset.update(is_checked=Programms.Status.CHECKED)
        self.message_user(request, f'{update_count} программы помечены как проверенные', 'success')

    @admin.action(description='Отметить как непроверенные')
    def unset_checked(self, request, queryset):
        update_count = queryset.update(is_checked=Programms.Status.UNCHECKED)
        self.message_user(request, f'{update_count} программы отмечены как непроверенные')
        