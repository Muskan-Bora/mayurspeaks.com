from django.shortcuts import render, get_object_or_404
from mayurweb.models import about, service, military_trans, keynote_speaker, motivate_speaker, service_page, gallery_army, gallery_seminar, gallery_seminar2, gallery_achievement

# Create your views here.

def index(request):
    
    ABOUT = about.objects.all()
    SERVICE = service.objects.all()
    seminar2photos = gallery_seminar2.objects.all()
    
    context = {
        'ABOUT':ABOUT,
        'SERVICE':SERVICE,
        'seminar2photos':seminar2photos,
    }
    
    return render(request, 'mayur_web/index.html', context)

def about_me(request):
    
    ABOUT = about.objects.all()
    
    context = {
        'ABOUT':ABOUT,
    }
    
    return render (request,'mayur_web/about.html', context)

def services(request, servicepage_id=None):
    services = service_page.objects.all()
    selected_service = None

    if servicepage_id:
        selected_service = get_object_or_404(service_page, id=servicepage_id)
    
    context = {
        'services':services,
        'selected_service':selected_service,
    }
    
    return render (request, 'mayur_web/services.html', context)

def coaching_service(request):
    
    MILITARY_TRANS = military_trans.objects.all()

    context={
        'MILITARY_TRANS':MILITARY_TRANS
    }

    return render(request, 'mayur_web/coaching_service.html', context)

def keynotespeak_service(request):
    
    KEYNOTE_SPEAKER = keynote_speaker.objects.all()

    context={
        'KEYNOTE_SPEAKER':KEYNOTE_SPEAKER
    }

    return render(request, 'mayur_web/keynotespeak_service.html', context)

def motivate_service(request):
    
    MOTIVATE_SPEAKER = motivate_speaker.objects.all()

    context={
        'MOTIVATE_SPEAKER':MOTIVATE_SPEAKER
    }

    return render(request, 'mayur_web/motivate_service.html', context)

def gallery(request):

    armyphotos = gallery_army.objects.all()
    seminarphotos = gallery_seminar.objects.all()
    seminar2photos = gallery_seminar2.objects.all()
    achievements = gallery_achievement.objects.all()
    
    context = {
        'armyphotos':armyphotos,
        'seminarphotos':seminarphotos,
        'seminar2photos':seminar2photos,
        'achievements':achievements,
    }
    
    return render (request, 'mayur_web/gallery.html', context)