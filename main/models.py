from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        ordering = ['id']


class New(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='news/photo', verbose_name='Rasm')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kritilgan vaqti")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    is_published = models.BooleanField(default=True, verbose_name='Nashr etilgan')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'New'
        ordering = ['-created_at']

