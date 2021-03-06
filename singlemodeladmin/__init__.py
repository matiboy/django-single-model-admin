from django.core.exceptions import MultipleObjectsReturned
from django.core.urlresolvers import reverse
from django.contrib import admin, messages
from django.shortcuts import redirect


class SingleModelAdmin(admin.ModelAdmin):

    """
    Django ModelAdmin for models that are only meant to have one record.
    This is useful for a site-wide settings model, among other things.

    If there is only one object, the changelist will redirect to that object.
    If there are no objects, the changelist will redirect to the add form.
    If there are multiple objects, the changelist is displayed with a warning.

    Attempting to add a new record when there is already one will result in a
    warning and a redirect away from the add form.
    """

    def changelist_view(self, request, extra_context=None):
        info = "%s_%s" % (self.model._meta.app_label, self.model._meta.module_name)

        try:
            instance = self.model.objects.get()

        except self.model.DoesNotExist:
            return redirect(reverse("admin:%s_add" % info))

        except MultipleObjectsReturned:
            messages.warning(request, "There are multiple instances of %s. There should only be one." % self.model._meta.module_name, fail_silently=True)
            return super(SingleModelAdmin, self).changelist_view(request, extra_context=extra_context)

        else:
            return redirect(reverse("admin:%s_change" % info, args=[instance.pk]))

    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count():
            messages.warning(request, "Do not add additional instances of %s. Only one is needed." % self.model._meta.module_name, fail_silently=True)
            return redirect(reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name)))

        return super(SingleModelAdmin, self).add_view(request, form_url=form_url, extra_context=extra_context)
