from django.contrib import admin
from second_app.models import Topic, Webpage, AccessRecord, UserProfileInfo#, User

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
#admin.site.register(User)
admin.site.register(UserProfileInfo)
