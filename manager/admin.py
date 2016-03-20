from manager.models import *
from import_export import resources
from django.contrib.gis import admin
from import_export.admin import ExportMixin


class EventoLAdmin(admin.ModelAdmin):

    def filter_event(self, event, queryset):
        return queryset.filter(event=event)

    def queryset(self, request):
        queryset = super(EventoLAdmin, self).queryset(request)
        if request.user.is_superuser:
            return queryset
        collaborator = Collaborator.objects.get(user=request.user)
        return self.filter_event(collaborator.eventUser.event, queryset)


class TalkProposalResource(resources.ModelResource):
    class Meta:
        model = TalkProposal


class TalkProposalAdmin(ExportMixin, EventoLAdmin):
    resource_class = TalkProposalResource

    def filter_event(self, event, queryset):
        return queryset.filter(activity__event=event)


class EventAdmin(EventoLAdmin):

    def filter_event(self, event, queryset):
        return queryset.filter(name=event.name)


class CommentAdmin(EventoLAdmin):
    display_fields = ["activity", "created", "user"]

    def filter_event(self, event, queryset):
        return queryset.filter(activity__event=event)


class InstallerResource(resources.ModelResource):
    class Meta:
        model = Installer
        fields = ('eventUser__user__first_name', 'eventUser__user__last_name', 'eventUser__user__username',
                  'eventUser__user__email', 'eventUser__user__date_joined',
                  'eventUser__assisted', 'level')
        export_order = fields


class InstallerAdmin(ExportMixin, EventoLAdmin):
    resource_class = InstallerResource

    def filter_event(self, event, queryset):
        return queryset.filter(eventUser__event=event)


class InstallationResource(resources.ModelResource):
    class Meta:
        model = Installation
        fields = (
            'hardware__type', 'hardware__manufacturer__name', 'hardware__model', 'hardware__serial', 'software__type',
            'software__name', 'software__version', 'attendee__eventUser__user__email', 'installer__eventUser__user__username',
            'notes')
        export_order = fields


class InstallationAdmin(ExportMixin, EventoLAdmin):
    resource_class = InstallationResource

    def filter_event(self, event, queryset):
        return queryset.filter(installer__eventUser__event=event)


class AttendeeResource(resources.ModelResource):
    class Meta:
        model = Attendee
        fields = ('eventUser__user__first_name', 'eventUser__user__last_name', 'eventUser__user__username',
                  'eventUser__user__email', 'eventUser__assisted', 'additional_info')
        export_order = fields


class AttendeeAdmin(ExportMixin, EventoLAdmin):
    resource_class = AttendeeResource
    pass


class CollaboratorResource(resources.ModelResource):
    class Meta:
        model = Collaborator
        fields = (
            'eventUser__user__first_name', 'eventUser__user__last_name', 'eventUser__user__username',
            'eventUser__user__email', 'eventUser__user__date_joined', 'phone',
            'address',
            'eventUser__assisted', 'assignation', 'time_availability', 'additional_info')

        export_order = fields


class CollaboratorAdmin(ExportMixin, EventoLAdmin):
    resource_class = CollaboratorResource
    pass


admin.site.register(Comment, CommentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TalkProposal, TalkProposalAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Organizer)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(HardwareManufacturer)
admin.site.register(Hardware)
admin.site.register(Software)
admin.site.register(Installer, InstallerAdmin)
admin.site.register(Installation, InstallationAdmin)
admin.site.register(TalkType)
admin.site.register(Room, EventoLAdmin)
admin.site.register(ContactType)
admin.site.register(Contact, EventoLAdmin)
admin.site.register(Activity)
admin.site.register(ContactMessage)
admin.site.register(EventUser)
admin.site.register(Image)
admin.site.register(InstalationAttendee)
admin.site.register(Speaker)
