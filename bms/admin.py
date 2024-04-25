from django.contrib import admin
from .models import Stadium, Booking, Pitch


class PitchAdminInline(admin.TabularInline):
    model = Pitch


class StadiumAdmin(admin.ModelAdmin):
    inlines = [PitchAdminInline]
    exclude = ['slug']
    class Meta:
        model = Stadium


admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Pitch)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["user", "stadium", "pitch", "date", "time", "price", "paid"]
