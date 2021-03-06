# Параметры поля
# https://djbook.ru/rel1.9/ref/models/fields.html#field-options

# Параметры, применимые для всех типов данных ::::::::::::::::::

null # default False
# Если True, поле может хранить значение NULL (соответствует 
# значению None Python) 

blank # dafault False
# Если True, поле может хранить пустое значение

choices # default None
# Указывает список значений, которые может хранить поле; 
# значения вне этого списка ввести в такое поле нельзя

dЬ_column # default None
# Задает имя поля таблицы, которое .будет соответствовать 
# данному полю модели 

dЬ_index # default False
# Если True, на основе этого поля будет создан индекс

default # deault None
# Задает значение поля по умолчанию

editable # default True
# Если False, данное поле не будет выводиться на страницах 
# добавления и правки записи встроенного административного сайта

error_messages
# позволяет переопределить сообщения ошибок возвращаемых полем. Используйте 
# словарь с ключами соответствующими необходимым ошибкам. Ключи ошибок такие: 
# null, blank, invalid, invalid_choice, unique и ``unique_for_date`. 

help_text # default "" 
# Задает текст дополнительного описания, которое будет выводиться 
# под соответствующим элементом управления 

primary_key # default False
# Если тrue, данное поле станет ключевым

unique # default False
# Если True, данное поле станет уникальным

unique_for_date # default None
# Задает имя поля класса DateField или DateTimeField, после чего 
# данное поле станет уникальным в пределах даты, чье значение 
# будет взято из указанного поля

unique_for_month # default None 
# Задает имя поля класса DateField или DateTimeField, после чего 
# данное поле станет уникальным в пределах определенного месяца 
# даты, чье значение будет взято из указанного поля

unique_for_year # default None
# Задает имя поля класса DateField или DateTimeField, после чего 
# данное поле станет уникальным в пределах определенного года даты, 
# чье значение будет взято из указанного поля

verbose_name # default None
# Задает имя поля, которое будет отображаться на страницах 
# встроенного административного сайта

validators
# Список проверок(“валидаторов”) выполняемых для этого поля. 


CATEGORIES = (
    (1, "Метлы"),
    ( 2, "Веники") ,
    (3, "Щетки")
)

class Good(models.Model):
    category = models.IntegerField(choices=CATEGORIES, 
                            default=1, db_index=True)
# Здесь мы создаем список категорий товаров и указываем его в 
# качестве перечня доступных значений для целочисленного поля 
# category модели Good.

# Иногда нам может понадобиться сделать так, чтобы какое-то поле имело 
# уникаль­ные значения в течение определенной даты, месяца или года. 
# Скажем, мы решим, что все статьи блога, опубликованные в течение 
# одного дня, должны иметь уни­кальные заголовки. В таких случаях нам 
# помогут параметры unique_for_date, unique_for_month и unique_for_year:

class BlogArticle(models.Model):
    title = models.CharField(unique_for_date='pubdate')
    pubdate = models.DateField()
# Фактически мы укажем, что комбинации значений полей title и pubdate, 
# т.е. заго­ловок статьи и дата ее публикации, должны быть уникальными. 
# И пользователь не сможет в один и тот же день опубликовать в блоге 
# статьи с одинаковыми заголов­ками - Django этого не допустит.



# Параметры, специфичные для классов попей DateField, DateTimeField и 
# TimeField :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

auto_now # default False 
# Если True, в поле будет автоматически заноситься значение 
# сегодняшних датыи (или) времени при добавлении и при каждом сохранении 
# записи

auto_now_add # default False 
# Если True, в поле будет автоматически заноситься значение сегодняшних 
# даты и (или) времени при добавлении записи

updated = models.DateTimeField(auto_now=True)
# Здесь мы создали в модели статьи блога поле, которое будет хранить 
# дату и время последнего изменения статьи.



# Классы полей EmailField, SlugField и URLField также подцерживают 
# параметр max_length. Но в первом случае его значение по умолчанию 
# равно 75 (что, надо ска­зать, маловато для иных почтовых адресов ... ), 
# во втором - 50, а в третьем - 200.
