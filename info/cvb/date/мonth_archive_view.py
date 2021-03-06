from django.views.generic.dates import MonthArchiveView

MonthArchiveView 
# формирует список записей, относящихся к ука­занным нами году и месяцу 
# (вывод по месяцам). Этот класс является потомком классов DateMixin и 
# YearMixin и поддерживает все их свойства. Также он наследуется от 
# класса MonthМixin и получает от него два следующих свойства:

    month
    # задает месяц в виде строки. Значение по умолчанию - None;

    month_format
    # задает строку с форматом, согласно которому будет распозна­ваться 
    # значение месяца. Формат, используемый по умолчанию, - %b, т.е. 
    # трех­-буквенное обозначение месяца на английском языке 
    # (что не всегда удобно). 

# Значение месяца, за который следует отобрать записи для включения в 
# список, будет извлекаться:
    
    # либо из свойства month;

    # либо, если оно не указано, из группы регулярного выражения с 
    # именем month, созданной в интернет-адресе привязки;

    # либо, если такой группы нет, из GЕТ-параметра с именем month.

# Вот пример:

class MonthNewsArchiveView(MonthArchiveView):
    date_field = "pub_date"
    make_object_list = True
    month_format = "%m"
# Здесь мы объявляем класс-контроллер для вывода новостей, датированных 
# указан­ным месяцем указанного года. Задаем для распознавания значения 
# месяца формат %m - номер месяца из двух цифр с начальным нулем.

url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', 
    MonthNewsArchiveView.as_view(), 
    name="month_archive")
# Здесь в интернет-адресе мы создали две группы регу­лярных выражений: 
# year, которая будет извлекать значение года, и month, полу­чающая 
# номер месяца. Тогда, чтобы получить все новости за апрель 2014 года, 
# мы обратимся по интернет-адресу /news/2014/4/.

# MonthArchiveView создаст в контекcте данных шаблона следую­щие 
# дополнительные переменные:

    date_list
    # список всех чисел указанных месяца и года, взятых из поля модели, 
    # что задано в свойстве date_field. Они представлены в виде значений 
    # даты, в ко­торых нас интересует лишь собственно число;

    month # указанные месяц и год в виде значения даты;

    next_month # первый день следующего месяца в виде значения даты;

    previous_month # первый день предыдущего месяца в виде значения даты.

# Вот пример:

<h2>Архив новостей {{ month|date:"E" }} {{ month|date:"Y" }} года</h2>
# Здесь мы выводим указанные месяц и год.

<ul>
{% for date in date_list %}
    <li>{{ date|date:"j" }}</li>
{% endfor %}
</ul>
# А здесь - список чисел заданного месяца, в которые была создана хотя 
# бы одна новость.
