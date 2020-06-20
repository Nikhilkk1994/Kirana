from django.db import models
from django.utils.translation import ugettext_lazy as _


# TODO have to add the Image field
class Category(models.Model):
    """
    Model to create the category table
    """
    name = models.CharField(_('Category Name'), max_length=50, unique=True)
    url = models.URLField(_('Url for Category'), null=True, blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.lower()
        super(Category, self).save(force_insert, force_update, using, update_fields)


# TODO have to add the Image field
class Product(models.Model):
    """
    Model to create the product table
    """
    name = models.CharField(_('Product Name'), max_length=50, unique=True)
    description = models.CharField(_('Description'), max_length=50, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='product')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name + ' ' + str(self.id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.lower()
        super(Product, self).save(force_insert, force_update, using, update_fields)
