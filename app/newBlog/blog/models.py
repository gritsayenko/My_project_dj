from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

### Class for the category of the article
class Category(models.Model):
    title = models.CharField("Category name",max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

### Class for the tags of the article
class Tag(models.Model):
    title = models.CharField("Tag name",max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title

###Class of the new article
class Post(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name = "Author",
        on_delete=models.CASCADE,
        default = '')
    category = models.ForeignKey(
        Category,
        verbose_name = "Category",
        on_delete=models.SET_NULL,
        null=True)
    title = models.CharField("Headline",max_length=100)
    text_min = models.TextField("Short Descripton",max_length=350)
    text = models.TextField("Content")
    tags = models.ManyToManyField(Tag, verbose_name="Tags")
    created = models.DateTimeField ("Created date", auto_now_add=True)
    description = models.CharField("Description",max_length=100)
    keywords = models.CharField("Keywords",max_length=50)
    image = models.FileField(null=True, blank=True)
    visible = models.BooleanField(default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-id", "-timestamp"]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "post/%s/" %(self.id)

    class Meta:
        ordering = ["-id", "-timestamp"]

###Comments

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField ("Created date", auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
