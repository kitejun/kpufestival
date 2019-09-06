from django.db import models
from django.conf import settings # 외래키를 위한 라이브러리

'''
class Intro(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dename=models.TextField()
    
    img1 = models.FileField(upload_to="department", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    img2 = models.FileField(upload_to="department", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    img3 = models.FileField(upload_to="department", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    map_img = models.FileField(upload_to="department", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    
    pub_date=models.DateTimeField('date published')
    introduce=models.TextField()
    tag=models.TextField()

    intro_hits=models.PositiveIntegerField(default=0)
    intro_like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='intro_like_users')
    intro_hate_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='intro_hate_users')

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title

    def summary_title(self):
        return self.dename[:10]

    def summary(self):
        return self.context[:20]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[self.id])

    @property
    def update_counter_hit(self):
        self.intro_hits=self.intro_hits+1
        self.save()
        return ''
'''