# Микросервис на Python🐍 для проекта PrettyPet 

Микросервис написан при помощи фреймворка Django.

Описание всех выполненных задач находится в папке [README_FILES](./README_FILES).

В папке ```autotests``` находятся интеграционные и сценарные автотесты. Распределены по папкам, в зависимости от названия django-приложения.

Unit-тесты находятся внутри папки каждого из приложений в файле ```tests.py``` и реализованы через TestCase. 

### Модели:
- Описание:
  -  Модели составлены на основании описания проекта и бизнес-моделей.
- Чертёж хранится по ссылке <br> 
https://dbdiagram.io/d/Pretty-Pet-66c894f4a346f9518ce84d0f <br> 
Редактировать чертёж может Александр (tg: chutzp4h, discord: ne_pedofil_a_beta_tester).
- Чертёж в виде svg: <br>
![Pretty Pet.svg](README_FILES%2FREADME_IMAGES%2FPretty%20Pet.svg)  
- Чертёж в виде DBML (Database Markup Language): <br>
```dbml
// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table custom_users {
  custom_user_id int [pk]
  profile_id int [
    ref: - profiles.profile_id
  ]
  username varchar
  password varchar
  email varchar
  phone_number varchar
  code_word varchar
}

Table profiles {
  profile_id int [pk, 
    ref: < profiles_subscriptions.subscriber_profile_id, 
    ref: < profiles_subscriptions.subscribed_profile_id,
    ref: < profile_awards.profile_id,
    ref: < favourite_materials.profile_id,
    ref: < news.autor_id,
    ref: < profile_social_links.profile_id,
    ref: < profile_roles.profile_id,
    ref: < profile_tools.profile_id,
    ref: < participants_in_project.profile_id,
    ref: < participants_in_hackathon.profile_id,
    ref: < project_participation_request.profile_id,
    ref: < hackathon_participation_request.profile_id
  ]
  public_name varchar
  description text
  hobbies varchar
  age int 
  city_id int
  photo_url varchar  
}

Table cities {
  city_id int [pk,
    ref: < profiles.city_id
  ]
  city_name varchar
}

Table profiles_subscriptions {
  subscriber_profile_id int [pk]
  subscribed_profile_id int [pk]
}

Table awards {
  award_id int [pk,
    ref: < profile_awards.award_id  
  ]
  name varchar
  description varchar
  image_url varchar
}

Table profile_awards {
  profile_id int [pk]
  award_id int [pk]
}

Table useful_materials {
  useful_material_id int [pk,
    ref: < favourite_materials.useful_material_id
  ]
  title varchar
  description varchar
  image_url varchar
  link_name varchar
  likes_count int
}

Table favourite_materials {
  profile_id int [pk]
  useful_material_id int [pk]
}

Table news {
  new_id int [pk,
  ref: < news_topics.new_id,
  ref: < tags_in_news.new_id
  ]
  autor_id int
  title varchar
  description varchar
  image_url varchar
  likes_count int
  is_open bool
}

Table topics {
  topic_id int [pk,
  ref: < news_topics.topic_id
  ]
  topic_name varchar
}

Table tags_in_news {
  new_id int [pk]
  tag_id int [pk]
}

Table news_topics {
  new_id int [pk]
  topic_id int [pk]
}

Table social_links {
  social_link_id int [pk,
    ref: < profile_social_links.social_link_id
  ]
  name varchar
  url varchar
}

Table profile_social_links {
  profile_id int [pk]
  social_link_id int [pk]
}

Table roles {
  roles_id int [pk,
    ref: < profile_roles.role_id,
    ref: < roles_in_project.role_id,
    ref: < roles_in_hackathon.role_id,
    ref: < participant_in_project_roles.role_id,
    ref: < participant_in_hackathon_roles.role_id
  ]
  role_name varchar
}

enum LEVEL {
  trainee
  intern
  junior
  middle
  senior
}

Table profile_roles {
  profile_id int [pk]
  role_id int [pk]
  is_main bool
  level LEVEL
}

Table tools {
  tool_id int [pk,
    ref: < profile_tools.tool_id,
    ref: < tools_in_project.tool_id,
    ref: < tools_in_hackathon.tool_id,
    ref: < participant_in_project_tools.tool_id,
    ref: < participant_in_hackathon_tools.tool_id
  ]
  tool_name varchar
}

Table profile_tools {
  profile_id int [pk]
  tool_id int [pk]
}

enum PROJECT_STATUS {
  not_started
  in_process
  not_finished
  finished
}

Table projects {
  project_id int [pk,
    ref: < roles_in_project.project_id,
    ref: < tools_in_project.project_id,
    ref: < groups_in_project.project_id,
    ref: < participants_in_project.project_id,
    ref: < tags_in_project.project_id,
    ref: < project_participation_request.project_id
  ]
  type_id int 
  name varchar
  core_idea varchar
  description text
  finish_date date [default: null]
  status PROJECT_STATUS
  image_url varchar
  stars_count int
}

Table tools_in_project {
  project_id int [pk]
  tool_id int [pk]
  participants_needed int [default: null]
}

Table tools_in_hackathon {
  hackathon_id int [pk]
  tool_id int [pk]
  participants_needed int [default: null]
}

Table roles_in_project {
  project_id int [pk]
  role_id int [pk]
  participants_needed int [default: null]
}

Table roles_in_hackathon {
  hackathon_id int [pk]
  role_id int [pk]
  participants_needed int [default: null]
}

Table groups_for_projects {
  group_id int [pk,
  ref: < groups_in_project.group_id,
  ref: < participant_in_project_groups.group_id
  ]
  group_name varchar
}

Table participants_in_project {
  participant_id int [pk,
    ref: < participant_in_project_roles.participant_id,
    ref: < participant_in_project_tools.participant_id,
    ref: < participant_in_project_groups.participant_id
  ]
  project_id int 
  profile_id int 
}

Table participant_in_project_roles {
  participant_id int [pk]
  role_id int [pk]
}

Table participant_in_project_tools {
  participant_id int [pk]
  tool_id int [pk]
}

Table participant_in_project_groups {
  participant_id int [pk]
  group_id int [pk]
}

Table participant_in_hackathon_groups {
  participant_id int [pk]
  group_id int [pk]
}

Table participant_in_hackathon_tools {
  participant_id int [pk]
  tool_id int [pk]
}

Table participant_in_hackathon_roles {
  participant_id int [pk]
  role_id int [pk]
}

Table project_types {
  type_id int [pk,
  ref: < projects.type_id
  ]
  type_name varchar
}

Table groups_in_project {
  project_id int [pk]
  group_id int [pk]
}

Table hackathons {
  hackathon_id int [pk,
    ref: < participants_in_hackathon.hackathon_id,
    ref: < hackathon_participation_request.hackathon_id,
    ref: < roles_in_hackathon.hackathon_id,
    ref: < tools_in_hackathon.hackathon_id,
    ref: < groups_in_hackathon.hackathon_id,
    ref: < tags_in_hackathon.hackathon_id
  ]
  type_id int 
  name varchar
  core_idea varchar
  task text
  start_date date
  finish_date date
  image_url varchar
  prize_id int [
    ref: < hackathon_prizes.prize_id
  ]
}
Table groups_for_hackathons {
  group_id int [pk,
  ref: < groups_in_hackathon.group_id,
  ref: < participant_in_hackathon_groups.group_id
  ]
  group_name varchar
}

Table groups_in_hackathon {
  group_id int [pk]
  hackathon_id int [pk]
}

Table participants_in_hackathon {
  participant_id int [pk,
    ref: < participant_in_hackathon_roles.participant_id,
    ref: < participant_in_hackathon_tools.participant_id,
    ref: < participant_in_hackathon_groups.participant_id
  ]
  hackathon_id int 
  profile_id int 
}

Table tags {
  tag_id int [pk,
    ref: < tags_in_project.tag_id,
    ref: < tags_in_hackathon.tag_id,
    ref: < tags_in_news.tag_id
  ]
  name varchar
}

Table tags_in_project {
  project_id int [pk]
  tag_id int [pk]
}

Table tags_in_hackathon {
  hackathon_id int [pk]
  tag_id int [pk]
}

enum REQUEST_STATUS {
  pending
  accepted
  declined
}

Table project_participation_request {
  profile_id int [pk]
  project_id int [pk]
  cover_letter text
  resume_url varchar [default: null]
  status REQUEST_STATUS
}

Table hackathon_participation_request {
  profile_id int [pk]
  hackathon_id int [pk]
  cover_letter text
  resume_url varchar [default: null]
  status REQUEST_STATUS
}

Table hackathon_prizes {
  prize_id int [pk]
  name varchar
  description varchar
  image_url varchar
}
```

### Микросервис использует следующие приложения:
- account(Авторизация/Аутентификация пользователя)
- core(Общие утилиты проекта)

### Документация:
[drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)

Почему именно DRF Spectacular?
drf-spectacular - единственный проект, который сейчас активно поддерживается. django-rest-swagger и drf-yasg устарели и не обновлялись уже несколько лет.

- `docs/` - скачать документацию .yml
- `docs/swagger-ui/` - документация swagger-ui
- `docs/redoc/` - документация redoc

drf-spectacular - подключен к классу drf_spectacular.openapi.AutoSchema, то есть Swagger-UI и ReDoc документации будут строиться сами. Для более гибкой настройки в основном нужно использовать декоратор [`@extend_schema`](https://drf-spectacular.readthedocs.io/en/latest/readme.html#customization-by-using-extend-schema).

### Логирование:
- В корне репозитория есть папка `/logs` (если её нет, она создастся автоматически), куда пишутся файлы логов.
- Файл, созданный в текущий день, называется `logs`. Файлы, созданные в предыдущие
дни имеют имя `logs.{дата создания файла}`. По окончании текущего дня (в 00:00) при попытке записать новый лог файл 
`logs` меняет имя на `logs.{дата только что минувшего дня, она же - дата создания файла}`, и создаётся новый пустой файл с именем
`logs`, куда и будет записан этот новый лог (и все следующие логи наступившего дня).
- Всего в `/logs` могут находиться 4 файла: `logs` и три файла, созданных в предыдущие три дня. Все файлы старше трёх 
дней уничтожаются.
- В файл `logs` пишутся все логи текущего дня уровня `WARNING` и выше в формате 
`{levelname} - {asctime} - {module} - {message}`.
- В консоль выводятся логи всех уровней в формате `{levelname} - {asctime} - {module} - {message}`.
- В `/settings/logging.py` находится всё, что связано с логами. В частности, там находится функция `example_logs()` (а 
также её вызов), которая производит тестовые логи. При первичном старте сервера она выполняется два раза, но далее всё 
работает как нужно.
- **Примечание** <br>
Предположим, что у нас есть файл `logs` и запущен сервер. Если при этом сменится день (неважно, естественным путём или 
ручной сменой даты), после чего произойдёт перезапуск сервера путём `autoreload`, то файл `logs` не будет переименован
ввиду ошибки по типу:
`PermissionError: [WinError 32] Процесс не может получить доступ к файлу, так как этот файл занят другим процессом: 
'C:\\work\\microservice-python-pp-web\\logs\\logs' -> 'C:\\work\\microservice-python-pp-web\\logs\\logs.2024-08-27'.`, а
также логи перестанут записываться в файл. Скорее всего, это связано с работой файловой системы Windows. При ручном 
перезапуске сервера ошибок не возникает.
  
## <p align="center" >Всем добра!</p>
<p align="center">
  <img width="300" height="300" src="https://media.tenor.com/67iB7B7g59YAAAAM/siu-ronaldo-siu.gif">
</p>
