from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import datetime

class IndexView(View):
   def get(self, request):
         datetime_now = datetime.now()
         return render(request, 'tbtlog/index.html',
                       {'datetime_now': datetime_now})
   
class PageCreateView(View):
      def get(self, request):
          form = PageForm()
          return render(request, 'tbtlog/page_form.html', {'form': form})
     
      def post(self, request):
          form = PageForm(request.POST, request.FILES)
          if form.is_valid():
            form.save()
            return redirect('tbtlog:index')
          return render(request, 'tbtlog/page_form.html', {'form': form})
      
class PageListView(View):
    def get(self, request):
        page_list = Page.objects.order_by('visit_date')
        return render(request, 'tbtlog/page_list.html', {'page_list': page_list})

class PageDetailView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, 'tbtlog/page_detail.html', {'page': page})
    
class PageUpdateView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render(request, 'tbtlog/page_update.html', {'form': form})
    
    def post(self, request, id):
      page = get_object_or_404(Page, id=id)
      form = PageForm(request.POST, request.FILES, instance=page)
      if form.is_valid():
            form.save()
            return redirect('tbtlog:page_detail', id=id)
      return render(request, 'tbtlog/page_detail.html', {'form': form})
    
class PageDeleteView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, 'tbtlog/page_confirm_delete.html', {'page': page})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect('tbtlog:page_list')

index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()