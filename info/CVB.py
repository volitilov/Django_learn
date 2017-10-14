urlpatterns = [
    url(r'^list/$', GoodListView.as_view(template_name="index.html")),
    url(r'list/detail$', GoodDetailView.as_view(template_name="good.html")),
]
# Здесь мы привязываем классы-контроллеры GoodListView и 
# GoodDetailView, переда­вая им параметр template_name - имя файла шаблона, 
# с применением которого будут выводиться данные.


from django.views.generic.base import TemplateView

class AЬoutView(TemplateView):
    template_name = "/others/about.html"
# А здесь порождаем на основе класса Templateview потомок с 
# именем AЬoutView, в котором задаем имя файла шаблона.


try:
    page_num = self.request.GET["page"]
except KeyError:
    page_num = 1
# Здесь мы получаем значение GЕТ-параметра page - номер 
# страницы списка.


# Свойство args хранит список, представляющий все параметры, что 
# были указаны в привязке с применением обычных, «безымянных», 
# групп регулярных выражений. Эти параметры присутствуют в списке 
# в том порядке, в котором в привязке бьmи объявлены соответствующие 
# им группы:

url(r'^good/(\d+}/$', GoodDetailView.as_view(), name="good")
good_id = self.args[O]
# Здесь в методе класса GoodDetailView, порожденного от TemplateView, 
# мы получаем значение идентификатора товара.

# А свойство kwargs хранит список, представляющий все параметры, что 
# были указа­ны в привязке с применением именованных групп регулярных 
# выражений:
url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name="good")
good_id = self.kwargs["good_id"]


class GoodDetailView(TemplateView):
    template_name = "good.html"
    def get_context_data(self, **kwargs}:
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        context["good"] = Goods.objects.get(pk = good_id)
        return context

