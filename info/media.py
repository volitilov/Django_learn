# Нам доступны два класса полей модели, предназначенных для хранения 
# файлов.
    FileField # хранит файл любого типа;

    ImageField # хранит графический файл.

# Чтобы успешно использовать в моделях поля класса ImageFile, следует 
# установить стороннюю библиотеку Pillow.

# Конструкторы классов FileField и ImageField принимают обязательный 
# именован­ный параметр upload_to. Он задает папку, где физически 
# размещаются хранящиеся в данном поле файлы, - эта папка должна быть 
# вложена в папку, указанную нами в переменной МEDIA_RООТ в настройках 
# проекта

thumbnail = models.ImageField(upload_to = "goods/thumbnails")

# Мы можем использовать в путях к таким папкам литералы, с помощью 
# которых указываются форматы значений даты и времени, их следует 
# предварить символом процента(%):

class Good(models.Model):
    thumbnail = models.ImageField(upload_to = "goods/thumbnails/%Y/%m/%d")
# В этом случае файл изображения, загруженный, скажем, 14 марта 2014 года, 
# будет сохранен в папке goods\thumbnails\2014\3\14.

# Конструктор класса ImageField дополнительно поддерживает еще два 
# необязатель­ных параметра:
    width_field
    # имя поля модели, где будет храниться ширина изображения;
    
    height_field
    # имя поля модели, где будет храниться высота изображения.

# Эти значения будут заноситься при каждом сохранении записи. Оба этих 
# поля уже должны присутствовать в модели:
class Good(models.Model):
    thumbnail_width = PositiveSmallintegerField()
    thumbnail_height = PositiveSmallintegerField()
    thumbnail = models.ImageField(uploaded_to ="goods/thumbnails",
        width_field = "thumbnail_width", height_field = "thumbnail_height")

# Классы полей FileField и ImageField поддерживают также необязательный 
# пара­метр max_length. В этом случае значение по умол­чанию указанного 
# параметра равно 100.


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Получение сведений о файлах, хранящихся в модели

# Значение, хранящееся в полях классов FileField или ImageField, 
# представляет со­бой объект особого класса FieldFile. Перечисленные далее 
# свойства этого класса позволят нам получить различные сведения о 
# хранящемся в поле файле:
    name
    # путь к файлу относительно папки, чей путь указан в переменной 
    # МEDIA_ROOT;

    size # paзмep файла в байтах;
    
    url # интернет-адрес файла;

    width # ширина графического изображения в пикселах;

    height # высота графического изображения в пикселах.

# Последние два свойства поддерживаются лишь классом ImageField.

good = Good.objects.get(pk = kwargs["good_id"])
file_url = good.thumbnail.url
# В этом примере мы получаем интернет-адрес файла, хранящего изображение 
# товара.

<td>{% if good.thumbnail %}
    <img src="{{ good.thumbnail.url }}">
{% endif %}</td>
# А здесь выводим изображение товара на WеЬ-странице, предварительно 
# проверив, указано ли оно.

# Кроме того, класс ImageField поддерживает не возвращающий результата 
# метод delete, который выполняет удаление выбранного файла. Этот метод 
# принимает единственный необязательный параметр save:
    # если значение параметра save равно True (значение по умолчанию), 
    # то после удаления файла значение поля будет очищено, а сама 
    # запись - сохранена;

    # если же его значение равно False, то после удаления файла значение 
    # поля также будет очищено, но запись сохранена не будет. Нам придется 
    # самим вызвать у записи метод save, чтобы сохранить ее.

# Вот пример удаления файла с параметром save равным False:
good = Good.objects.get(pk = kwargs["good_id"])
good.thumbnail.delete(save = False)
good.save()

# УДАЛЕНИЕ СВЯЗАННОГО ФАЙЛА
# При удалении записи, включающей в свой состав поле класса FileField 
# или ImageField, связанный с этим полем файл не будет удален. Нам 
# придется удалить его самим - вызовом метода delete. В противном случае 
# этот файл станет «мусор­ным»
good = Good.objects.get(pk = kwargs["good_id"])
good.thumbnail.delete(save = False)
good.delete()



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Выгрузка файлов через формы

# В процессе валидации классы FileField и ImageField могут генерировать 
# сообще­ния об ошибках с кодами required, invalid и max_length.
# Также могут быть сгенерированы ошибки с кодами.

missing 
# Файл почему-то не был выгружен (например, произошла ошибка чтения с 
# диска)

empty 
# Выгружаемый файл пуст

invalid_image 
# Формат графического файла не поддерживается библиотекой Pillow. 
# Генерируется лишь классом ImageField

Вот пример:
class GoodForm(forms.ModelForm):
    thumbnail = forms.ImageField(label = "Изображение", 
        error_messages = {'required': "Укажите файл изображения", 
        'invalid_image': "Изображение должно быть сохранено в формате, поддерживаемом сайтом"})


# Чтобы форма могла успешно отправить файл, нам следует явно указать для 
# нее ме­тод кодирования данных multipart/form-data:
<form action = "" method="post" enctype="multipart/form-data"></form>

# Класс Form поддерживает свойство is_multipart. Оно возвращает True, если 
# форма включает в себя поля для хранения файлов и, следовательно, требует 
# указания метода кодирования данных multipart/form-data:
<form action="" method="post" {% if form.is_multipart %} enctype="multipart/form-data" {% endif %}>
</form>


# Вот так будет выглядеть фрагмент кода метода POST в классе-контроллере 
# для создания новой записи:
self.form = GoodForm(request.POST, request.FILES)
if self.form.is_valid():
    self.form.save()

# А вот так - в классе-контроллере для правки записи:
self.form = GoodForm(request.POST, request.FILES, instance=good)
if self.form.is_valid():
    self.form.save()



# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Проверка типа вь1груженных файлов

# Каждый файл, перечисленный в словаре, что хранится в свойстве FILES 
# объекта сведений о запросе, является объектом класса UploadedFile. Этот 
# класс поддержи­вает свойство content_type, хранящее МIМЕ-тип файла в виде 
# строки.
# Далее приведен фрагмент кода класса-контроллера, реализующий такую 
# проверку. Он удостоверяется, что посетитель выгрузил через форму 
# архивный файл формата ZIP.

self.form = SomeForm(request.POST, request.FILES)
if self.form.is_valid():
    filetype = request.FILES["somefile"].content_type
    if filetype == "application/zip":
        self.form.save()
        messages.success(request, "Позиция добавлена")
        return redirect("index")
    else:
        messages.error(request, "Допускаются только архивы ZIP!")
        return super().get(request, *args, **kwargs)
else:
    return super().get(request, *args, **kwargs)

Вот список MIME-types:

application/javascript
application/json
application/x-www-form-urlencoded
application/xml
application/zip
application/pdf
application/sql
application/msword (.doc)
application/vnd.openxmlformats-officedocument.wordprocessingml.document(.docx)
application/vnd.ms-excel (.xls)
application/vnd.openxmlformats-officedocument.spreadsheetml.sheet (.xlsx)
application/vnd.ms-powerpoint (.ppt)
application/vnd.openxmlformats-officedocument.presentationml.presentation (.pptx)
audio/mpeg
audio/vorbis
multipart/form-data
text/css
text/html
text/csv
text/plain
image/png
image/jpeg
image/gif


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Проблема «мусорных» файлов и ее решение

# Все модели поддерживают унаследованные от класса­ родителя Model методы 
# save и delete. Переопределив эти методы в классах моде­лей, мы можем 
# поместить в них код, который будет выполнять какие-либо дейст­вия при 
# сохранении и удалении записи.
# И в самом деле: методы save и delete класса модели - просто идеальное 
# место для вставки кода, который будет удалять «мусорные» файлы!
# Вот такой код переопределенного метода save мы можем использовать для 
# удале­ния файла, который хранился в поле класса FileField или ImageField 
# ранее, до правки:

class Good(models.Model):
    thumbnail = models.ImageField(upload_to="goods/thumbnails")
    def save(self, *args, **kwargs):
        try:
            this_record = Good.objects.get(id = self.id)
            if this_record.thumbnail != self.thumbnail:
                this_record.thumbnail.delete(save = False)
        except: pass
        super().save(*args, **kwargs)
# Здесь мы ищем в модели Good запись, чей идентификатор совпадает с 
# идентифика­тором текущей записи, т.е. ту же самую запись. Если хранящийся 
# в ее поле thumbnail файл не совпадает с тем, что хранится в том же поле 
# текущей записи, т.е. если в это поле было занесено новое значение - 
# другой файл, - то старый файл (который в этом случае станет «мусорным») 
# удаляется.

# А этот код переопределенного метода delete мы можем использовать, чтобы 
# при удалении записи удалялся и хранящийся в поле файл:
class Good(models.Model):
    thumbnail = models.ImageField(upload_to = "goods/thumbnails")
    def delete(self,, *args, **kwargs):
        self.thumbnail.delete(save = False)
        super().delete(*args, **kwargs)
# Отметим, что в качестве значения параметра save метода delete мы указали 
# False. В противном случае запись будет удалена раньше времени, и в работе 
# модели мо­жет возникнуть ошибка.