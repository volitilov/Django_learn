from django.views.generic.dates import TodayArchiveView

TodayArchiveView 
# отбирает записи, относящиеся к текущей дате. Он аналогичен 
# рассмотренному нами ранее классу DayArchiveView, но по понятным
# причинам не требует передачи ему значений числа, месяца и дня:

url(r'^today/$', TodayArchiveView.as_view(model=New, 
        template_name='day_archive.html', date_field='pub_date'),
    name = "today_archive")
# Здесь мы привязываем вызов класса-контроллера TodayArchiveView 
# к интернет­-адресу /today/.

# В остальном этот класс используется так же, как и подобный ему класс
# DayArchiveView.
