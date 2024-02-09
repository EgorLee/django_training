from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Title')
    cms_text = models.CharField(max_length=200, verbose_name='Text')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS class')


    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'


class MetaTags(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.CharField(max_length=200, verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'MetaTag'
        verbose_name_plural = 'MetaTags'



