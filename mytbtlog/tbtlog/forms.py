from django.forms import ModelForm
from .models import Page

class PageForm(ModelForm):
   class Meta:
      model = Page
      fields = ['title', 'visit_date', 'visit_name', 'visit_company', 'visit_cost', 'visit_picture1','visit_picture2','visit_picture3','visit_picture4','visit_picture5', 'note']