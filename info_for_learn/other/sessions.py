# Когда SessionMiddleware активный, каждый объект HttpRequest 
# – первый аргумент представления в Django – будет содержать 
# атрибут session, который является объектом с интерфейсом 
# словаря. Вы можете читать и менять request.session в любом 
# месте вашего представления множество раз.

Пример:

fav_color = request.session['fav_color']
# получение

request.session['fav_color'] = 'blue'
# назначение

del request.session['fav_color']. 
# Удаление. Вызовет KeyError, если key ещё не в сессии.

'fav_color' in request.session
# Получение, вернёт True или False

fav_color = request.session.get('fav_color', 'red')
# получение, но в случае отсутствия, получить значение по 
# умалчанию

fav_color = request.session.pop('fav_color', 'blue')
# удалить fav_color, а на её место всавить другое значение

keys()
# получить список ключей

items()
# получить список значений

setdefault()

clear()
# очистить сессии


# Также содержит следующие методы:

flush()
# Удаляет текущие данные сеанса из сеанса и удаляет файл cookie сеанса. 
# Это используется, если вы хотите, чтобы предыдущие данные сеанса не 
# могли быть снова доступны из браузера пользователя (например, функция 
# django.contrib.auth.logout() вызывает его).

set_test_cookie()
# Устанавливает тестовую куку, чтобы проверить, что браузер пользователя 
# поддерживает куки. Из-за особенностей работы кук вы не сможете проверить 
# тестовую куку, пока пользователь не запросит следующую страницу.

test_cookie_worked()
# Возвращает True или False, в зависимости от того, принял ли бразуер 
# пользователя тестовую куку. Из-за особенностей работы кук вам необходимо 
# вызывать в предыдущем запросе set_test_cookie().

delete_test_cookie()
# Удаляет тестовую куку. Используйте, чтобы убрать за собой.

set_expiry(value)
# Указывает время жизни сессии. Вы можете передать различные значения:

    # Если value целое число, сессия истечет после указанного количества 
    # секунд неактивности пользователя. Например, 
    # request.session.set_expiry(300) установит время жизни равное 
    # 5 минутам.

    # Если value это datetime или timedelta, сессия истечёт в указанное 
    # время. Обратите внимание, datetime и timedelta сериализуются только 
    # при использовании PickleSerializer.

    # Если value равно 0, сессионная кука удалится при закрытии браузера.

    # Если value равно None, сессия будет использовать глобальное поведение.

# Чтение сессии не обновляет время жизни сессии. Время жизни просчитывается 
# с момента последнего изменения.



get_expiry_age()
# Возвращает время в секундах до окончания действия сессии. Для сессий без 
# времени окончания (или для тех, что действуют пока работает браузер), 
# значение будет равно SESSION_COOKIE_AGE.
# Функция понимает два необязательных именованных аргумента:

    modification 
    # время последнего изменения сессии в виде объекта datetime. По умолчанию 
    # соответствует текущему времени.

    expiry
    # время окончания сессии в виде объекта datetime, количества секунд в виде 
    # int или None. По умолчанию используется значение, установленное методом 
    # set_expiry(), если оно есть, в противном случае будет None.


get_expiry_date()
# Возвращает дату окончания действия сессии. Для сессий, у которых дата 
# завершения не указана (или которые завершаются при закрытии браузера), 
# значением будет дата, отстоящая на SESSION_COOKIE_AGE секунд от текущего 
# момента.
# Функция принимает те же именованные аргументы, что и get_expiry_age().

get_expire_at_browser_close()
# Возвращает True или False, в зависимости от того, будет ли кука 
# пользовательской сессии сброшена когда пользователь закроет свой браузер.

clear_expired()
# Удаляет просроченные сессии из хранилища сессий. Этот метод класса 
# используется clearsessions.

cycle_key()
# Создает новый ключ сессии при сохранении текущих данных в ней. Функция 
# django.contrib.auth.login() вызывает этот метод, чтобы противодействовать 
# фиксации сессии.


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Рекомендации для объекта сессии

# Используйте обычные строки Python в качестве ключей словаря в 
# request.session. Это больше соглашение, чем правило.

# Ключи словаря сессии, которые начинаются с подчёркивания зарезервированы 
# для внутреннего использования Django.

# Не перекрывайте request.session новым объектом, не меняйте его атрибута. 
# Пользуйтесь им как обычным словарём Python.

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Параметры конфигурации

# Несколько параметров конфигурации Django представляют вам управление 
# поведением сессии:

    SESSION_CACHE_ALIAS
    # По умолчанию: default
    # При использовании кэширующего бэкенда для сессии, указывает какой кэш 
    # использовать.

    SESSION_COOKIE_AGE
    # По умолчанию: 1209600 (2 недели в секундах)
    # Время хранения сесионной куки в секундах.

    SESSION_COOKIE_DOMAIN
    # По умолчанию: None
    # Домен, используемый для сессионных кук. Используйте строку, например, 
    # ".example.com" (обратите внимание на точку в начале!), для кросдоменних 
    # кук, или используйте None для стандартного домена.
    # Осторожно меняйте эту настройку на боевом сайте. Если вы измените ее, 
    # чтобы разрешить кросс-доменные куки на сайте, старые куки будут 
    # использовать старое значение домена. Поэтому все пользователя не будут 
    # авторизованы.
    # Также влияет на работу кук django.contrib.messages.
    
    SESSION_COOKIE_HTTPONLY
    # По умолчанию: True
    # Если установлена в True, JavaScript в браузере не будет иметь доступ к 
    # сессионной куке.
    # Эта настройка усложнит использование XSS уязвимости для кражи сессии 
    # пользователя. Нет важных причин, чтобы не включать эту опцию.

    SESSION_COOKIE_NAME
    # По умолчанию: 'sessionid'
    # Название для сессионной куки. Может быть каким угодно (но не совпадать 
    # с другими куками проекта).
    
    SESSION_COOKIE_PATH
    # По умолчанию: '/'
    # Путь(пер. path), который будет использоваться при установке сессионной 
    # куки. Путь должен соответствовать URL-у к вашему проекту или быть 
    # родительским относительно него.
    # Эта настройка может быть полезна если вы используете несколько проектов 
    # на одном домене. Они могут использовать различные пути для сессионных 
    # кук и каждый проект будет видеть только свою сессионную куку.

    SESSION_COOKIE_SECURE
    # По умолчанию: False
    # Указывает использовать ли безопасные куки для сессии. Если равна True, 
    # куки будут помечены как “безопасные”, это означает что браузер будет 
    # проверять отослана ли кука через HTTPS подключение.
    # Т.к. для снифера пакетов (например Firesheep) очень легко украсть 
    # сессионную куку пользователя, если она отправляется в открытом виде, 
    # нет никаких важных причин выключать эту опцию. Эта опция отключит 
    # возможность использовать сессию для незащищенных запросов, что является 
    # хорошим подходом.
    
    SESSION_ENGINE
    # По умолчанию: django.contrib.sessions.backends.db
    # Указывает, где Django хранит сесионные данные. Возможные значения:
        'django.contrib.sessions.backends.db'
        'django.contrib.sessions.backends.file'
        'django.contrib.sessions.backends.cache'
        'django.contrib.sessions.backends.cached_db'
        'django.contrib.sessions.backends.signed_cookies'

    SESSION_EXPIRE_AT_BROWSER_CLOSE
    # По умолчанию: False
    # Истекает ли сессия после закрытия браузера.

    SESSION_FILE_PATH
    # По умолчанию: None
    # Если вы используете файловое хранилище сессионных данных, эта настройка 
    # укажет Django каталог, в котором хранить данные. Если используется 
    # значение по умолчанию (None), Django будет использовать стандартный каталог 
    # для временных файлов вашей операционной системы.

    SESSION_SAVE_EVERY_REQUEST
    # По умолчанию: False
    # Сохранять ли данные сессии при каждом запросе. При False, данные сохраняются 
    # только при изменении, то есть, если какое либо значение словаря было 
    # переназначено или удалено. Пустая сессия не будет создана, даже если эта 
    # настройка активна.

    SESSION_SERIALIZER
    # По умолчанию 'django.contrib.sessions.serializers.JSONSerializer'
    # Полный путь для импорта класса сериализатора сессионных данных. Есть несколько 
    # встроенных классов:
        'django.contrib.sessions.serializers.PickleSerializer'
        'django.contrib.sessions.serializers.JSONSerializer'