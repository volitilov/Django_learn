from django.db import models
from django.utils import timezone

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

class BlogCategory(models.Model):
    class Meta:
        db_table = 'blog_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(max_length=30, unique=True, verbose_name='название')

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
    
    title = models.CharField(max_length=50, db_index=True, 
                    unique=True, verbose_name='название')
    description = models.TextField(verbose_name='пост')
    pub_date = models.DateField(db_index=True, auto_now_add=True)
    likes = models.IntegerField(default=0, verbose_name='Кол. лайков:')
    previews = models.IntegerField(default=0, verbose_name='Кол-во просмотров:')
    thumbnail = models.ImageField(upload_to = "blog/img", null=True, blank=True)
    category = models.ForeignKey(BlogCategory, verbose_name='категория', 
            null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            this_record = Post.objects.get(id = self.id)
            if this_record.thumbnail != self.thumbnail:
                this_record.thumbnail.delete(save = False)
        except: pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.thumbnail.delete(save = False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
    