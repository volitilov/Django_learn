# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Получение сведений о пользователе

# Самого пользователя, точнее, представляющий его объект класса User, 
# мы можем получить из свойства user объекта сведений о запросе. Но 
# как получить сведения о нем? С помощью набора методов класса user, 
# перечисленных ниже. Все эти методы не принимают параметров, 
# поэтому могут быть использованы в шаблонах.

# Методы класса User :::::::::::::::::::::::::::::::
get_username 
# Возвращает имя, под которым пользователь был зарегистрирован на 
# сайте («логин»)

get_short_name # Возвращает реальную фамилию

get_full_name 
# Возвращает строку из реальных имени и фамилии, разделенных пробелом

is_anonymous # Возвращает True, если это гость

# Вот пример возвращения строки из реальных имени и фамилии:
{% if user.is_authenticated %}
    <р>Добро пожаловать, {{ user.get_full name }}!</р>
{% endif %}

# Помимо этих методов, класс User поддерживает четыре полезных 
# свойства:

is_active # True, если пользователь помечен как активный;

is_staff
# True, если пользователь помечен как входящий в состав персонала 
# сайта, т.е. имеет возможность входа на встроенный административный 
# сайт;

is_superuser
# True, если пользователь помечен как суперпользователь, т.е. имеющий 
# максимальные права без явного их указания;

email # адрес электронной почты пользователя.