def delete(self, *args, **kwargs):
    # Вьmолняем дополнительные действия перед удалением записи
    # Обязательно вызываем метод delete родителя,
    # иначе запись не будет удалена
    super(Good, self) .delete(*args, **kwargs)
    # Вьmолняем какие-либо действия после удаления записи