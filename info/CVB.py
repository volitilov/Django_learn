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


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
from django.views.generic.list import ListView

ListView
# предназначен для вывода списков каких-либо позиций - например, товаров. 
# По сравнению со своим родителем Templateview он предоставляет 
# следующую допол­нительную функциональность: 
# - формирование в контексте данных переменной, хранящей список записей 
#   из указанной модели;
# - встроенную поддержку пагинации. 

# Свойства класса ListView :::::::::::::::::::::::
model 
# Класс модели, из которой будут браться записи для вывода 

queryset 
# Список записей для вывода в виде объекта класса QuerySet. 
# Значение этого свойства имеет приоритет перед значением свойства 
# model 

context_object_name 
# Имя переменной контекста данных, в которой будет храниться список 
# записей. Если не указано, будет создана переменная object_list

paginate_by 
# Количество позиций на странице при задействованной пагинации. 
# Значение по умолчанию - None (т. е. пагинация не выполняется)

paginate_orphans 
# Минимальное количество позиций, допустимое на последней странице 
# Значение по умолчанию - О

allow_empty 
# Имеет смысл лишь в том случае, когда список записей пуст. Если 
# значение этого свойства равно True, будет выведена одна пустая 
# страница, в противном случае будет выполнен переход на страницу 
# «ошибки 404». Значение по умолчанию - True

page_kwarg 
# Строка с именем параметра, которым в интернет-адресе передается 
# номер страницы. Значение по умолчанию - page

# ::::::::::::::::::::::::::::::::::::::::::::::::::


get_context_data
# форми­рует контекст данных со следующими переменными:
    # переменная, хранящая список записей для вывода. Ее имя задается 
    # в свойстве context_object_name (по умолчанию - object_list);

    # <имя класса модели, набранное прописными буквами>_list - то же 
    # самое, что предыдущая;

    # is_paginated - True, если пагинация задействована, и False в 
    # противном случае;

    # paginator- объект класса Paginator, с применением которого 
    # вы­полняется пагинация;

    # page_obj - объект класса Page, представляющий текущую страницу;

    # и, разумеется, переменные, хранящие значения всех полученных 
    # контроллером параметров, для которых были созданы именованные 
    # группы регулярных выра­жений.

get
# присваивает переменной контекста данных, в которой должен 
# храниться список записей, этот самый список. Он вы­полняется 
# раньше перечисленных ранее методов и сам вызывает сначала метод 
# get_context_data, а потом - метод get_queryset.
# Метод get принимает следующие параметры:
    # объект класса HttpRequest, хранящий сведения о запросе
    
    # список со всеми неименованными параметрами, соответствующими 
    # переданным контроллеру данным;

    # словарь со всеми именованными параметрами.


class GoodListView(ListView):
    template_name = "index.html"
    paginate_by = 10
    cat = None

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] == None:
            self.cat = Category.objects.first()
        else:
            self.cat = Category.objects.get(pk=self.kwargs["cat_id"])
        return super(GoodListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("name")
        context["category"] = self.cat
        return context

    def get_queryset(self):
        return Good.objects.filter(category=self.cat).order_by("name")


# Мы объявили в классе GoodListView свойство cat, в котором будет 
# храниться вы­бранная категория, присвоили ему значение в теле 
# переопределенного метода get, а потом использовали это значение 
# в методах get_context_data и get_queryset.