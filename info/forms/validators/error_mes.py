# Коды ошибок, поддерживаемые различными классами полей, и их описания

  Код ошибки     : Описание ошибки                        : Классы полей
# ------------------------------------------------------------------------
# required       : В обязательное поле не было введено    : Все
#                : значение                               :
# ------------------------------------------------------------------------
# min_length     : Введенная строка имеет длину меньшую,  : CharField
#                : чем указана в параметре min_lenght     :
# --------------------------------------------------------
# max_length     : Введенная строка имеет длину большую,  :
#                : чем указана в параметре max _ lenght   :
# -------------------------------------------------------------------------
# invalid_choice : Введено значение, отсутствующее в      : ChoiceField,
#                : списке                                 : ModelChoiceField
# -------------------------------------------------------------------------
# invalid        : Введенное значение имеет неверный      : DateField,
#                : формат                                 : DateTimeField,
#                                                         : EmailField,
#                                                         : FloatField,
#                                                         : IntegerField,
#                                                         : IPAddressField,
#                                                         : GenericIPAddressField,
#                                                         : SlugField,
#                                                         : TimeField,
#                                                         : URLField
# -------------------------------------------------------------------------
# min_value      : Введено значение меньшее, чем указано  : FloatField,
#                : в параметре min_value                  : IntegerField
# ---------------------------------------------------------
# max_value      : Введено значение большее, чем указано  :
#                : в параметре max_value                  :
# -------------------------------------------------------------------------

Вот примеры:
class GoodForm(ModelForm):
    class Meta:
        model = Good
        error_messages = {"name": {"required": "Укажите название товара", 
                                   "min_length": "Слишком короткое название", 
                                   "max_length": "Слишком длинное название"}}
# Здесь мы задаем список сообщений об ошибках для поля name формы, созданной 
# простым способом.

NAМE_ERROR_LIST = {"required": "Укажите название товара",
                   "min_length": "Слишком короткое название",
                   "max_length": "Слишком длинное название"}
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        name = forms.CharField(label="Название",
            help_text="Должно быть уникальным", 
            error_messages=NAМE_ERROR_LIST)
# А здесь делаем то же самое для формы, созданной сложным способом.