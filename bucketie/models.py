from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

class AutoCreatedField(models.DateTimeField):
    """
    A DateTimeField that auto populates itself at object creation.
    By default, it sets editable to False, default=now
    """
    def __init__ (self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super(AutoCreatedField, self).__init__(*args, **kwargs)

class AutoLastModifiedField(AutoCreatedField):
    """
    A DateTimeField that updates itself on each save of the model.
    By Default, it sets editable=False, default=now
    """
    def pre_save(self, model_instance, add):
        value = now()
        setattr(model_instance, self.attname, value)
        return value

class DescribedModel(models.Model):
    """
    An abstract class model that provides fields for a name and description,
    and slug fields used in many scenerios. The description field of this class
    is indexed
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField(default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(unicode(self.name))
        super(DescribedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(_('created_at'))
    modified_at = AutoLastModifiedField(_('modified_at'))

    class Meta:
        abstract = True
        ordering = ['-created_at', '-modified_at']