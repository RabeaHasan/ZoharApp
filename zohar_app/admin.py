import imp
from django.contrib import admin

# Register your models here.
from .models import survey
from .models import statuses
from .models import manufacturers
from .models import mainsites
from .models import mainitems
from .models import items
from .models import guides


admin.site.register(survey)
admin.site.register(statuses)
admin.site.register(manufacturers)
admin.site.register(mainsites)
admin.site.register(mainitems)
admin.site.register(items)
admin.site.register(guides)