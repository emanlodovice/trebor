from django.views.generic import DetailView, ListView

from product.models import Product


class Home(ListView):
    template_name = 'trebor/home.html'
    model = Product


class Detail(DetailView):
    template_name = 'trebor/detail.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(Detail, self).get_context_data(*args, **kwargs)
        context['url'] = self.request.build_absolute_uri()
        return context
