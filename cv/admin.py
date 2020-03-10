from django.contrib import admin
from cv.models import Cv, Technologies, Education, Experience, Points


class PointsAdmin(admin.ModelAdmin):
    list_filter = ('experience__title', )
    list_display = ('title', 'experience')


admin.site.register(Cv)
admin.site.register(Technologies)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Points, PointsAdmin)
