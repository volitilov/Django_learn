# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ContextMixin
# реализующий создание контекста данных. Oт него наследу­ется класс 
# TemplateView;

MultipleObjectMixin
# реализующий выборку из модели и помещение в контекст данных списка 
# выводимых записей. Является потомком класса ContextMixin. От него 
# наследуется класс ListView;

SingleObjectMixin
# реализующий выборку записи с указанным идентифи­катором или коротким 
# заголовком и помещение ее в контекст данных. Также является потомком 
# класса contextMixin. Oт него наследуется класс DetailView.