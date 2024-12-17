from django.db import models

# Create your models here.

class about(models.Model):
    name = models.CharField(
        max_length=500,
        default="Sir Name",
    )
    
    intro = models.CharField(
        max_length=2000,
        default="intro",
    )
    
    pointer1 = models.TextField(
        default="1st point",
    )
    
    pointer2 = models.TextField(
        default="2nd point",
    )
    
    pointer3 = models.TextField(
        default="3rd point",
    )
    
    pointer4 = models.TextField(
        default="4th point",
    )
    
    pointer5 = models.TextField(
        default="5th point",
    )
    
    pointer6 = models.TextField(
        default="6th point",
    )
    
    pointer7 = models.TextField(
        default="7th point",
    )
    
    def __str__(self):
        return self.name
    
class service(models.Model):
    service_name = models.CharField(
        max_length=200,
        default="Title of the Service",
    )
    
    icon_class = models.CharField(
        max_length=100,
        help_text="fa-solid fa-star"
    )
    
    def __str__(self):
        return self.service_name
    
class military_trans(models.Model):
    heading = models.CharField(
        max_length=500,
        default="heading",
    )
    
    sub_heading = models.TextField(
        default="sub_heading",
    )
    
    desc = models.TextField(
        default="description",
    )
    
    img = models.ImageField(
        upload_to='services',
        default="https://emifreecar.com/images-new/offcer-coming-soon.jpg",
    )
    
    def __str__(self):
        return self.heading
    
class keynote_speaker(models.Model):
    heading = models.CharField(
        max_length=1000,
        default="heading"
    )
    
    desc = models.TextField(
        default="description"
    )
    
    def __str__(self):
        return self.heading
    
class motivate_speaker(models.Model):
    heading = models.CharField(
        max_length=500,
        default="heading",
    )
    
    intro = models.TextField(
        default="intro",
    )
    
    why_choose = models.TextField(
        default="why choose me",
    )
    
    desc = models.TextField(
        default="description",
    )
    
    def __str__(self):
        return self.heading
    
class service_page(models.Model):
    service_name = models.CharField(
        max_length=200,
        default="Title of the Service",
    )
    
    icon_class = models.CharField(
        max_length=100,
        help_text="fa-solid fa-star"
    )

    desc = models.TextField(
        default="description"
    )

    def __str__(self):
        return self.service_name


class gallery_army(models.Model):
    image = models.ImageField(
        upload_to='gallery/army',
        default="https://emifreecar.com/images-new/offcer-coming-soon.jpg",
    )

    def __str__(self):
        return self.image.url
    

class gallery_seminar(models.Model):
    image = models.ImageField(
        upload_to='gallery/seminar',
        default="https://emifreecar.com/images-new/offcer-coming-soon.jpg",
    )

    def __str__(self):
        return self.image.url
    
class gallery_seminar2(models.Model):
    image = models.ImageField(
        upload_to='gallery/seminar',
        default="https://emifreecar.com/images-new/offcer-coming-soon.jpg",
    )

    def __str__(self):
        return self.image.url

class gallery_achievement(models.Model):
    image = models.ImageField(
        upload_to='gallery/achievements',
        default="https://emifreecar.com/images-new/offcer-coming-soon.jpg",
    )

    def __str__(self):
        return self.image.url
   

