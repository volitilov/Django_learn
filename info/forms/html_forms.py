# Контекст данных шаблона, где присутствует форма, включает в себя 
# переменную, хранящую эту форму. Эта переменная обычно носит имя 
# form. Но ее значение можно рассматривать и как список полей, 
# включенных в состав формы. Следовательно, мы можем обработать 
# этот список в теге шаблона for

<form action = "" rnethod = "post">
    {% for field in form %}
    {% endfor %}
    <p><input type="submit" vаluе="Сохранить"></p>
</form>

# Отдельные поля формы представляются объектами класса BoundField. 
# Этот класс поддерживает следующие свойства:
    label # текст надписи;
    
    label_tag # НТМL-код, создающий надпись;
    
    help_text # текст дополнительных сведений;
    
    is_hidden # True, если данное поле является скрытым;

    errors # НТМL-код, создающий неупорядоченный список, каждый пункт 
           # кото­рого представляет собой описание одной из возникших 
           # ошибок;
    
    name # имя поля.

# При обращении к самому объекту класса BoundField будет возвращен 
# НТМL-код, создающий элемент управления.
# Вот так может выглядеть код шаблона, создающего форму на основе 
# набора блоков:
<form action="" method="post">
    {% for field in form %}
        <div class="form-field">
            {% if field.errors|length > О %}
                <div class="error-list">
                    {{ field.errors }}
                </div>
            {% endif %}
            <div class="label">{{ field.label }}</div>
            <div class="control">{{ field }}</div>
            {% if field.help_text %)
                <div class="help">{{ field.help_text }}</div>
            {% endif %}
        </div>
    {% endfor %}
    <input type="submit" value="Coxpaнить">
</form>

# Свойство errors класса BoundField хранит список строк, каждая из 
# которых пред­ставляет собой описание ошибки. Мы можем воспользоваться 
# этим, чrобы сгене­рировать список ошибок на свой вкус:
{% if field.errors|length > О %}
    <div class="error-list">
        {% for error in field.errors %}
            <div class="error-description">{{ error }}</div>
        {% endfor %)
    </div>
{% endif %}

# Класс Form также поддерживает не принимающие параметров методы visible_fields
# и hidden_fields. Они возвращают списки всех видимых и невидимых полей формы 
# соответственно:
<form action="" method = "post">
    {% for field in form.hidden_fields %}{% endfor %}
    {% for field in form.visible_fields %}{% endfor %}
    <input type="submit" value="Coxpaнить">
</form>

# Класс Form поддерживает и набор свойств, чьи имена совпадают с именами полей
# формы. Эти свойства хранят соответствующие поля - мы можем использовать их,
# чrобы непосредственно сослаться на то или иное поле:
<form action="" method="post">
    {{ form.in_stock }}
    {{ form.category }}
    {{ form.name }}
    {{ form.description }}
    <input type="submit" value="Coxpaнить">
</form>


# класс Form поддерживает еще два полезных свойства:
    required_css_class
    # стилевой класс, который будет привязан к элементам управления, 
    # соответствующим обязательным полям формы;

    error_css_class
    # стилевой класс, который будет привязан к элементам управ­ления, в 
    # которых были введены некорректные данные.

Вот пример:
class GoodForm(forms.ModelForm):
    required_css_class = "required"
    error_css_class = "error"
