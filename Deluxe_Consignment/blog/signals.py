from django.db.models.signals import post_save
from blog.models import Post
from django.template.defaultfilters import slugify

# don't forget to update apps.py. Otherwise, signals will not work.


def create_blog_slug(sender, created, instance, **kwargs):
    # instance.save() creates infinite recursive loop for some reason.
    # more details can be found here: https://medium.com/bilesanmiahmad/how-to-prevent-recursionerror-maximum-recursion-depth-exceeded-when-using-django-signals-dbfe1615eff1
    Post.objects.filter(title=instance.title, thumbnail=instance.thumbnail, body=instance.body,
                        date_created=instance.date_created).update(slug=slugify(instance.title)
    )

post_save.connect(create_blog_slug, sender=Post)