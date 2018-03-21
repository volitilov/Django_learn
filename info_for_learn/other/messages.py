from django.contrib import messages

add_message() 
# добавляет в хранилище новое сообщение. Она принимает три параметра:
    
    # сведения о запросе в виде объекта класса HttpRequest
    
    # уровень сообщения в виде числа;

    # строка, представляющая само сообщение.


# Когда вы перебираете список сообщений в шаблоне, вы получаете экземпляры 
# класса Message. Это довольно простой объект с несколькими атрибутами:
message 
# текст сообщения

level 
# Целое число описывающий тип сообщения

tags
# Строка, объединяющая все теги сообщения (extra_tags и level_tag), 
# разделенные пробелами. 

extra_tags
# Строка, содержащая пользовательские теги для этого сообщения, разделенные 
# пробелами. По умолчанию он пуст.

level_tag
# Строковое представление уровня.



# ::::::::::::::::::::::::::::
# Django предлагает пять уровней сообщения. Соответствующие им числовые 
# иден­тификаторы хранятся в следующих переменных:

DEBUG
# отладочное сообщение (сообщения такого уровня будут игнорироваться 
# после запуска сайта в эксплуатацию);

INFO
# информационное сообщение общего назначения;

SUCCESS
# сообщение об успешном выполнении какой-либо операции;

WARNING
# предупреждение о какой-либо нештатной ситуации, которая, тем неменее, 
# не может нарушить работу сайта;

ERROR
# сообщение о критической ошибке.

Вот пример:
class GoodCreate(TemplateView):
    def post(self, request):
        if self.form.is_valid():
            self.form.save()
            messages.add_message(request, messages.SUCCESS, "Товар успешно добавлен в список")
            return redirect("index")
        else:
            return super().get(request)
# Здесь мы добавляем в класс-контроллер GoodCreate функцию отправки сообщения 
# об успешном добавлении товара в список.

# можно также изпользовать следующий ситаксис
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')


# Значения для встроенных уровней ошибок

DEBUG	    10
INFO	    20
SUCCESS	    25
WARNING	    30
ERROR	    40

# Так же мы можем создавать свои уровни например, главное чтобы они не совподали
# со значениями существующих 
CRITICAL = 50


# Такой код мы можем использовать для вывода сообщений на WеЬ-странице:
{% if messages %}
    <ul class = "message-list">
        {% for message in messages %}
            <li class="{{ message.tags }}">{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}

# Кстати, если мы используем высокоуровневые классы-контроллеры CreateView и 
# UpdateView, предназначенные для добавления и изменения записи соответственно, 
# то можем переложить работу по отправке сообщений об успехе на плечи 
# такого контроллера. Для этого мы добавим в его список родителей класс 
# SuccessMessageMixin, объявленный в модуле django.contrib.messages.views, и 
# зада­дим текст сообщения в унаследованном от этого класса свойстве 
# success_message.
# Оrметим, что класс successMessageMixin должен быть первым в списке родителей, 
# иначе сообщения формироваться не будут:

from django.contrib.messages.views import SuccessMessageMixin
class GoodCreate(SuccessMessageMixin, TemplateView):
    success_message = "Товар успешно добавлен в список"

# К сожалению, с классом-контроллером DeleteView, выполняющим удаление записи,
# такой номер не пройдет. Нам придется переопределять в его потомке метод post,
# в котором и выполнять оmравку сообщения.

