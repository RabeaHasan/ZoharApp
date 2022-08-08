import imp
from django.contrib import admin

# Register your models here.
from .models import Survey
from .models import Statuses
from .models import Manufacturers
from .models import Mainsites
from .models import Mainitems
from .models import Items
from .models import Guides


admin.site.register(Survey)
admin.site.register(Statuses)
admin.site.register(Manufacturers)
admin.site.register(Mainsites)
admin.site.register(Mainitems)
admin.site.register(Items)
admin.site.register(Guides)