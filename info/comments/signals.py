# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Сигналы, отправленные приложением комментариев

django_comments.signals.comment_will_be_posted
# Отправляется до сохранения комментария.
# Это можно использовать для изменения комментария (на месте) с информацией 
# о проводнике или другими подобными действиями.

# Если какой-либо приемник возвращает False, комментарий будет отброшен и 
# будет возвращен ответ 400.

# Аргументы, отправленные с помощью этого сигнала:
sender # Отправитель
comment 
# Экземпляр комментария должен быть опубликован. Обратите внимание, что он 
# еще не был сохранен в базе данных, поэтому у него не будет первичного 
# ключа, и любые отношения могут работать некорректно.
request
# HttpRequest, разместивший комментарий.




django_comments.signals.comment_was_posted
# Отправляется сразу после сохранения комментария.

# Аргументы, отправленные с помощью этого сигнала:
sender
comment 
# Экземпляр комментария, который был опубликован. Обратите внимание, что 
# он уже будет сохранен, поэтому, если вы его измените, вам нужно снова 
# вызвать save().
request




django_comments.signals.comment_was_flagged
# Отправлено после того, как комментарий был каким-то образом «помечен». 
# Проверьте флаг, чтобы узнать, был ли это запрос пользователя на удаление 
# комментария, модератор, одобряющий / удаляющий комментарий, или другой 
# пользовательский флаг пользователя.

# Аргументы, отправленные с помощью этого сигнала:
sender
comment 
flag
# Файл django_comments.models.CommentFlag, прикрепленный к комментарию.
created
# True, если это новый флаг; False, если это дубликат.
request