from django.contrib import admin
from django.utils.html import format_html
from miceservice.models import *
from django.core.serializers.json import DjangoJSONEncoder
import json

# Заголовки админ.сайта
admin.site.index_title = 'SomeProject'
admin.site.site_header = 'SomeProject'
admin.site.site_title = 'Административная панель'
# Register your models here.


# Метод получения всех полей модели(столбцов таблицы)
def get_model_fields(model):
    return [field.name for field in model._meta.get_fields()][1:]


@admin.register(PassengerTraffic)
class PassengerTrafficAdmin(admin.ModelAdmin):
    change_list_template = 'custom_admin/miceservice/passenger_traffic_change_list.html'
    list_per_page = 30
    list_filter = ('year', )
    list_display = ('year', 'traffic', 'report')

    def report(self, obj):
        return format_html('<button class="button">PDF/Excel</button>')

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        # chart_data = [{'year': obj.year, 'traffic': obj.traffic} for obj in PassengerTraffic.objects.all()]
        years = [obj.year for obj in PassengerTraffic.objects.all()]
        traffic = [obj.traffic for obj in PassengerTraffic.objects.all()]

        # Serialize and attach the chart data to the template context
        years_json = json.dumps(years, cls=DjangoJSONEncoder)
        traffic_json = json.dumps(traffic, cls=DjangoJSONEncoder)
        extra_context = extra_context or {'label': years_json, 'data': traffic_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(AttractionType)
class AttractionTypeAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name',)


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_filter = ('type',)
    list_display = ('name', 'type', 'address', 'operating_mode', 'ticket_price', 'site')
    search_fields = ('name', 'type', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_per_page = 30
    # list_filter = ('MICE', )
    list_display = ('name', 'date', 'place')
    search_fields = ('name', 'date', 'place')


@admin.register(Hotel)
class PassengerTrafficAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_filter = ('district',)
    list_display = ('name', 'address', 'phone_number', 'number_of_rooms', 'district')
    search_fields = ('name', 'address', 'phone_number', 'district')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'address', 'contacts', 'site', 'operating_mode', 'type_of_cuisine', 'number_of_seats')
    search_fields = ('name', 'address', 'type_of_cuisine')


@admin.register(TourismStatistic)
class TourismStatisticAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_filter = ('name',)
    list_display = ('name', 'year', 'quantity', 'report')
    search_fields = ('name', 'year')

    def report(self, obj):
        return format_html('<button class="button">PDF/Excel</button>')


@admin.register(Monument)
class MonumentAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_filter = ('district',)
    list_display = ('name', 'address', 'district')
    search_fields = ('name', 'address')
