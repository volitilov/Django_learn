def save(self, *args, **kwargs):
    # Вьmолняем дополнительные действия перед сохранением записи
    # Обязательно вызываем метод save родителя,
    # который, собственно, вьmолняет сохранение записи.
    # Если мы этого не сделаем, запись не будет сохранена
    super(Good, self) .save(*args, **kwargs)
    # Вьmолняем какие-либо действия после сохранения записи