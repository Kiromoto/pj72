from django_filters import FilterSet, ModelChoiceFilter, CharFilter, NumberFilter
from .models import Product, Category


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains', label='Поиск в названии товара')
    category = ModelChoiceFilter(queryset=Category.objects.all(), lookup_expr='exact', label='Категория',
                                 empty_label='Все категории')
    quantity = NumberFilter(field_name='quantity', lookup_expr='gt', label='Товара в наличии более')
    price_lt = NumberFilter(field_name='price', lookup_expr='lt', label='Товары стоимостью менее')
    price_gt = NumberFilter(field_name='price', lookup_expr='gt', label='Товары стоимостью более')

    class Meta:
        model = Product
        fields = {'name', 'category', 'quantity', }
        #
        #
        # fields = {'name': ['icontains'],
        #           'quantity': ['gt'],
        #           'price': ['lt', 'gt', ],
        #           'category': ['exact'],
        #           }
