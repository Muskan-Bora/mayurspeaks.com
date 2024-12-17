from django.contrib import admin
from mayurweb.models import about
from mayurweb.models import service
from mayurweb.models import military_trans
from mayurweb.models import keynote_speaker
from mayurweb.models import motivate_speaker
from mayurweb.models import service_page
from mayurweb.models import gallery_army
from mayurweb.models import gallery_seminar
from mayurweb.models import gallery_seminar2
from mayurweb.models import gallery_achievement

# Register your models here.

admin.site.register(about)
admin.site.register(service)
admin.site.register(military_trans)
admin.site.register(keynote_speaker)
admin.site.register(motivate_speaker)
admin.site.register(service_page)
admin.site.register(gallery_army)
admin.site.register(gallery_seminar)
admin.site.register(gallery_seminar2)
admin.site.register(gallery_achievement)
