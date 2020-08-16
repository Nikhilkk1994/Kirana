from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    Model to create the category table
    """
    name = models.CharField(_('Category Name'), max_length=50, unique=True)
    description = models.CharField(_('Description'), max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='media/category/', null=True, max_length=255)
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


class ProductKeyword(models.Model):
    """
    Keywords for product
    """
    name = models.CharField(_('Product Keyword'), max_length=50, unique=True)

    class Meta:
        verbose_name = _('Product Keyword')
        verbose_name_plural = _('Product Keywords')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.lower()
        super(ProductKeyword, self).save(force_insert, force_update, using, update_fields)


class Product(models.Model):
    """
    Model to create the product table
    """
    name = models.CharField(_('Product Name'), max_length=50, unique=True)
    description = models.CharField(_('Description'), max_length=50, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='product')
    image = models.ImageField(upload_to='media/product/', null=True, max_length=255)
    keywords = models.ManyToManyField(ProductKeyword, related_name='products', blank=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.lower()
        super(Product, self).save(force_insert, force_update, using, update_fields)


class ProductPersonality(models.Model):
    """
    Model for the Product Config
    """
    ML, GRAM, PIECE = 1, 2, 3
    _UNITS = (
        (ML, _('Mil Liter')),
        (GRAM, _('Grams')),
        (PIECE, _('Pieces'))
    )
    quantity = models.IntegerField(_('Quantity of Product Item'), blank=True, null=True)
    unit = models.IntegerField(choices=_UNITS, default=ML, verbose_name=_('Units of Product'), db_index=True)

    class Meta:
        verbose_name = _('Product Personality')
        verbose_name_plural = _('Product Personality')

    def __str__(self):
        return 'Quantity:' + ' ' + str(self.quantity) + ' ' + 'Units: ' + str(self.get_unit_display())
