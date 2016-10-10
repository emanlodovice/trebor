from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'trebor/home.html'


class Detail(TemplateView):
    template_name = 'trebor/detail.html'

    def get_context_data(self):
        context = super(Detail, self).get_context_data()
        context['url'] = self.request.build_absolute_uri()
        return context
