# Типы полей
# https://djbook.ru/rel1.9/ref/models/fields.html#field-types

# Справочник по полям модели
# https://djbook.ru/rel1.9/ref/models/fields.html#field-api-reference

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Классы полей для простых типов данных 

AutoField # Счетчик

BigintegerField 
# 64-разрядное (длинное) целое число; позволяет хранить значения от 
# -9223372036854775808 до 9223372036854775807

BinaryField
# Поля для хранения бинарных данных. Принимает значение типа bytes. Это поле 
# имеет ограниченный функционал. Например, QuerySet нельзя фильтровать по 
# значению BinaryField.

BooleanField 
# Логический
# Виджет по умолчанию для этого поля CheckboxInput.

CharField 
# Строковый
# Виджет по умолчанию для этого поля TextInput.

CommaSeparatedIntegerField
# Поле, содержащее целые числа разделенные запятыми. Как и в CharField, 
# необходим параметр max_length.

DateField # Дата
DateTimeField # Дата и время

DecimalField
# Виджет по умолчанию в форме для этого поля - NumberInput, если 
# localize равен False, иначе TextInput.
# Десятичное число с фиксированной точностью, представленное объектом 
# Decimal Python. Принимает два обязательных параметра:
    DecimalField.max_digits
    # Максимальное количество цифр в числе. Заметим, что это число 
    # должно быть больше или равно decimal_places.
    DecimalField.decimal_places
    # Количество знаков после запятой.

DurationField
# Поля для хранения периодов времени - используется объект Python timedelta. 
# Для PostgreSQL используется тип interval, а в 
# Oracle – INTERVAL DAY(9) TO SECOND(6). Иначе используется bigint, в 
# котором хранится количество микросекунд.

FloatField # Число с плавающей точкой

IntegerField 
# 32-разрядное (обычное) целое число; позволяет хранить значения от 
# -2147483648 до 2147483647

PositiveintegerField 
# 32-разрядное положительное целое число; позволяет хранить значения 
# от О до 2147483647

PositiveSmallIntegerField 
# 16-разрядное (короткое) положительное целое число; позволяет хранить 
# значения от О до 32767

SlugField 
# Короткий заголовок или название, включающее только символы латиницы, 
# цифры, дефисы и символы подчеркивания. Обычно применяются в так 
# называемых SЕО-дружественных интернет-адресах

SmallintegerField 
# 16-разрядное (короткое) целое число; позволяет хранить значения от 
# -32768 до 32767

TextField # Memo
TimeField # Время

NullBooleanField
# Как и BooleanField, но принимает значение NULL. Используете его вместо 
# BooleanField с null=True. Форма использует виджет NullBooleanSelect.

URLField
# Поле CharField для URL.
# Виджет по умолчанию для этого поля TextInput.
# Как подкласс CharField URLField принимает необязательный аргумент 
# max_length. Если вы не укажите max_length, будет использовано 
# значение – 200.

UUIDField
# Поля для сохранения UUID. Использует класс Python UUID. Для PostgreSQL 
# используется тип uuid, иначе char(32).

# Классы полей для производных типов данных :::::::::::::::::::::::::::

EmailField 
# Адрес электронной почты. Использует EmailValidator для проверки 
# значения.

FileField
# Поле для загрузки файла.
# Виджет форма для этого поля - ClearableFileInput.
    upload_to
    # Этот атрибут позволяет указать каталог и название файла при его 
    # сохранении.
    storage
    # отвечает за хранение и получение файлов

ImageField
# Наследует все атрибуты и методы поля FileField, но также проверяет 
# является ли загруженный файл изображением.
# Виджет форма для этого поля - ClearableFileInput.

IPAddressField # IР-адрес протокола IPv4
GenericIPAddressField # IР-адрес протокола IPv4 или IPv6
URLField # Интернет-адрес
