# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.http import HttpResponseRedirect
# from .models import Product
# from .filters import ProductFilter
# from .forms import ProductForm
#
#
# class ProductsList(ListView):
#     model = Product  # Указываем модель, объекты которой мы будем выводить
#     ordering = 'name'  # Поле, которое будет использоваться для сортировки объектов
#     # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
#     template_name = 'products.html'
#     # Это имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'products'
#     paginate_by = 5
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = ProductFilter(self.request.GET, queryset)
#         return self.filterset.qs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context
#
# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'product.html'
#     context_object_name = 'product'
#
# class ProductCreate(CreateView):
#     form_class = ProductForm
#     model = Product
#     template_name = 'product_edit.html'
#
# class ProductUpdate(UpdateView):
#     form_class = ProductForm
#     model = Product
#     template_name = 'product_edit.html'
#
# class ProductDelete(DeleteView):
#     model = Product
#     template_name = 'product_delete.html'
#     success_url = reverse_lazy('product_list')


# def create_product(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/products/')
#
#     return render(request, 'product_edit.html', {'form': form})

from django.http import HttpResponse
from django.views import View
from .tasks import hello, printer

class IndexView(View):
    def get(self, request):
        printer.delay(10)
        hello.delay()
        return HttpResponse('Hello!')