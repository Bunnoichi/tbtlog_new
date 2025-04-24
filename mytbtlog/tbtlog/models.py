from django.db import models
from pathlib import Path
import uuid

class Page(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
   title = models.CharField(max_length=100, verbose_name='タイトル')
   visit_date = models.DateField(verbose_name='行った日')
   visit_name = models.CharField(max_length=100, verbose_name='行った店')
   visit_company = models.TextField(blank=True, verbose_name='行った人')
   visit_cost = models.IntegerField(verbose_name='かかった金額')
   visit_picture1 = models.ImageField(upload_to='tbtlog/picture/', blank=True, null=True, verbose_name='行った写真1')
   visit_picture2 = models.ImageField(upload_to='tbtlog/picture/', blank=True, null=True, verbose_name='行った写真2')
   visit_picture3 = models.ImageField(upload_to='tbtlog/picture/', blank=True, null=True, verbose_name='行った写真3')
   visit_picture4 = models.ImageField(upload_to='tbtlog/picture/', blank=True, null=True, verbose_name='行った写真4')
   visit_picture5 = models.ImageField(upload_to='tbtlog/picture/', blank=True, null=True, verbose_name='行った写真5')
   note = models.TextField(max_length=300, blank=True, null=True,  verbose_name='メモ')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
   updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

   def __str__(self):
      return self.title
   
   def delete(self, *args, **kwargs):
      picture = [self.visit_picture1,
                 self.visit_picture2,
                 self.visit_picture3,
                 self.visit_picture4,
                 self.visit_picture5]
      super().delete(*args, **kwargs)
      for pic_i in picture:
         if pic_i:
            print(pic_i)
            Path(pic_i.path).unlink(missing_ok=True)