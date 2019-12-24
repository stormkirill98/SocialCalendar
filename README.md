# SocialCalendar
Plan your life
Plan events, alone or with your friends

# API
Общие
-----------------------------------

### /login GET
    Запрос для авторизации

### /logout GET
    Запрос для деавторизации

### /user GET
    Возвращает текущего пользователя:
      {
        'id': id,
        'google_id': google_id,
        'name': name,
        'email': email,
        'profile_pic': profile_pic,
        'birthday': birthday,
        'event_id_list': [event_id_list],
        'friend_id_list': [friend_id_list],
        'chat_id_list': [chat_id_list],
        'invite_id_list': [invite_id_list]
      }


### /search/users?filtered_str=... GET
    Поиск пользователей по имени и email

    200 - OK
    204 - по данной строке не найдено пользователей
    400 - filtered_str отсутствует или пустая
    401 - пользователь не аутентифицирован

    Возвращает список подходящих пользователей:
    [
        список пользователей(как выглядит пользователь в /user)
    ]

### /load_icon/<iconname>
    Загрузить иконку события по имени иконки

    Возвращает тег img, в котором в src изображение, закодированное в byte64


События
-----------------------------------

### /events?year=y1&month=m1 GET
    Возвращает все события за месяц m1 года y1:
      {
        1: [
          {
            id: "124412",
            type: "group",
            name: "First Event",
            is_private: "true",
            datetime: "23.11.2019 19:00",
            address: "address",
            description: "desciption fasadsa",
            icon: "localhost:5000/load_icon/bell.svg"
          },
          {
            id: "12422412",
            type: "group",
            name: "Second Event",
            is_private: "true",
            datetime: "23.11.2019 19:00",
            address: "address",
            description: "desciption fasadsa",
            icon: "localhost:5000/load_icon/coctail.svg"
          }
        ],
        15: [
          {
            id: "1244126763",
            type: "group",
            name: "First Event",
            is_private: "true",
            datetime: "23.11.2019 19:00",
            address: "address",
            description: "desciption fasadsa",
            icon: "..."
          }
        ]
      }

### /event?id=... GET

    200 - OK
    400 - event_id не получен,
    401 - пользователь не аутентифицирован
    403 - пользователь не имеет доступа к этому событию
    404 - событе не найдено

    Возвращает событие по id:
      * SINGLE:
        {
          'id': id,
          'name': name,
          'is_private': is_private,
          'datetime': datetime,
          'address': address,
          'description': description,
        } 
      * GROUP:
        {
          'id': id,
          'name': name,
          'is_private': is_private,
          'datetime': datetime,
          'address': address,
          'description': description,
          'member_id_list': [member_id_list],
          'chat_id': chat_id
        }

### /event POST

    Создает и сохраняет событие в БД. Возвращет id созданного события.
    Если групповое событие, то созддать для него чат и добавить текущего 
    пользователя в событие, а событие и чат пользователю.
    
    200 - OK,
    400 - не валидный body,
    401 - пользователь не прошел авторизацию

    Тело вызова:
    {
      "type": "group", //или single
      "name": "event name",
      "is_private": "true", //или false
      "datetime": "23.11.2019 19:00",
      "address": "address",
      "description": "desciption fasadsa" // не обязательное поле
    }

### /event PUT

    Обновить событие
    
    204 - OK,
    400 - не валидный body,
    401 - пользователь не прошел авторизацию,
    403 - пользователь не имеет прав,
    404 - с полученным id не найдено событие(либо есть шанс, что перепутан тип)

    Тело вызова:
    {
      "id": "event_id"
      "type": "group", //или single
      "name": "event name",
      "is_private": "true", //или false
      "datetime": "23.11.2019 19:00",
      "address": "address",
      "description": "desciption fasadsa" // не обязательное поле
    }

### /event?id=... DELETE

    Удалить событие с заданным id

    204 - ОК
    400 - неправильный id
    401 - пользователь не аутентифицирован
    403 - пользователь не имеет прав на удаление события
    404 - событие или участник события не найден

### /event/group/leave?id=... DELETE

    Покинуть событие с заданным id
    Если участник последний, то событие будет удалено

    204 - ОК
    400 - неправильный id
    401 - пользователь не аутентифицирован
    403 - пользователь не имеет прав на удаление события
    404 - событие или участник события не найден

Чат
-----------------------------------

### /chats?count_getting=...&count=... GET

    Получить count чатов начиная с count_getting. 
    То есть count_getting - это кол-во уже полученных чатов,
    а count - это сколько нужно еще догрузить

    200 - все ОК
    400 - некорректные аргументы

    Возвращаемый результат:
    [
      список чатов ( как выглядят чаты ниже)
    ]

### /chat?id=... GET
    Получить чат по id. 
    Чат содержит все сообщения, отсортированные в порядке написания

    200 - OK
    400 - некорректный id
    401 - пользователь не аутентифицирован
    403 - чат не доступен для этого пользователя
    404 - чат не найден

    Чат между пользователями: 
    {
      "id": id,
      "msg_id_list": [
        {
          "id": id,
          "chat_id": chat_id,
          "user_id": user_id,
          "datetime": 1574625273441,
          "text": "text of msg"
        },
        {
          "id": id,
          "chat_id": chat_id,
          "user_id": user_id,
          "datetime": 1574625273441,
          "text": "text of msg"
        }
      ],
      "user_id_1": "5dd0330f9a5ef7791b641fff",
      "user_id_2": "5dd136061c9d44000040a6b6"
    }

    Чат события: 
    {
      "id": id,
      "msg_id_list": [
        {
          "id": id,
          "chat_id": chat_id,
          "user_id": user_id,
          "datetime": 1574625273441,
          "text": "text of msg"
        },
        {
          "id": id,
          "chat_id": chat_id,
          "user_id": user_id,
          "datetime": 1574625273441,
          "text": "text of msg"
        }
      ],
      'event_id': event_id
    }

### /chat/msg POST
    Отправить сообщение.
    
    Тело запроса:
    {
      "chat_id": "5dd15fb705b75899b9af57b0",
      "text": "new message on http request"
    }

    204 - ОК
    400 - некорректный chat id
    401 - пользователь не аутентифицирован
    403 - чат не доступен для этого пользователя
    404 - чат не найден

### /chat/msg PUT
    Изменить сообщение.
    
    Тело запроса:
    {
      "id": "5dd15fb705b75899b9af57b0",
      "text": "new message on http request"
    }

    204 - ОК
    400 - некорректный id
    401 - пользователь не аутентифицирован
    404 - сообщение не найдено

### /chat/msg?id=... DELETE
    Удалить сообщение.

    204 - ОК
    400 - некорректный id
    401 - пользователь не аутентифицирован
    404 - сообщение не найден

Друзья
-----------------------------------

### /friends GET
    Получить список друзей текущего пользователя

    200 - ОК
    204 - все ок, но друзей нет, хотя не ок...

    Возвращает список друзей:
    [
      {
        'id': id,
        'name': name,
        'email': email,
        'profile_pic': profile_pic,
        'birthday': birthday
      },
      {
        'id': id,
        'name': name,
        'email': email,
        'profile_pic': profile_pic,
        'birthday': birthday
      }
    ]

### /friend?id=... GET
    Получить друга по id

    200 - все ОК
    400 - некорректный id
    401 - пользователь не аутентифицирован
    404 - пользователь не найден

    Возвращает пользователя:
    {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'profile_pic': self.profile_pic,
      'birthday': self.birthday,
      'event_id_list': self.event_id_list,
      'friend_id_list': self.friend_id_list,
    }

### /friend?id=... DELETE
    Удалить пользователя из друзей по id

    204 - все ОК
    400 - некорректный id
    401 - пользователь не аутентифицирован
    404 - пользователь не найден

Приглашения
-----------------------------------

### /invites GET
    Получить все приглашения текущего пользователя

    200 - OK
    204 - нет приглашений
    401 - пользователь не аутентифицирован

    Возвращает:
    [
      {
        'id': id,
        'sender_id': sender_id,
        'receiver_id': receiver_id,
        'type': type,
        'event_id': event_id
      },
      {
        'id': id,
        'sender_id': sender_id,
        'receiver_id': receiver_id,
        'type': type,
        'event_id': event_id
      }
    ]

### /invite POST
    Отправить приглашение в друзья или событие

    204 - все ОК
    400 - некорректный body
    403 - пользователь не имеет прав на приглашение в событие
    404 - не найден участник события, который отправляет приглашение

    Тело запроса:
    {
      "type": friend, // or event
      "receiver_id": "id",
      "event_id" : "id" // не обязательное для типа friend
    }

### /invite?id=...&action=... DELETE
    Принять или отклонить приглашение. 
    id - id приглашения
    action - действие accept или decline

    204 - все ок
    400 - не правильные аргументы
    403 - этот инвайт отправлен не этому пользователю
    404 - инвайт не найден
