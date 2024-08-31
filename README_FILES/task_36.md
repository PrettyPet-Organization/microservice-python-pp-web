# Задача #36: Создание моделей

### Описание
Модели составлены на основании описания проекта и бизнес-моделей.

### Хранилище чертежа моделей
Чертёж хранится по ссылке <br>
https://dbdiagram.io/d/Copy-of-PrettyPet-66c5e43ea346f9518caee2e2 <br>
Редактировать чертёж может Александр (tg: chutzp4h, discord: ne_pedofil_a_beta_tester).

### Чертёж в виде svg
![Pretty Pet.svg](README_IMAGES%2FPretty%20Pet.svg)

### Чертёж в виде DBML (Database Markup Language)
```dbml
// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table CustomUser {
  id integer [pk]
  username varchar
  password varchar
  email varchar
  phone_number varchar
  code_word varchar
  profile_id integer [ref: > Profile.id, note: 'One-to-one']
}

Table ProfileAwards {
  profile_id integer [pk, ref: > Profile.id]
  award_id integer [pk, ref: > Award.id]
}

Table ProfileFavouriteMaterials {
  id integer [pk]
  profile_id integer [ref: > Profile.id]
  material_id integer [ref: > Material.id]
}

Table ProfileSubscription {
  subscriber_profile_id integer [pk, ref: > Profile.id, note: 'Подписчик']
  subscribed_profile_id integer [pk, ref: > Profile.id, note: 'Подписуемый или я хз как назвать)']
}

Table Profile {
  id integer [pk]
  city_name varchar
  public_name varchar
  age integer
  photo_url varchar
  description text
  hobbies varchar
}

Table SocialLinksToProfile {
  profile_id integer [ref: > Profile.id] 
  social_links_id integer [ref: > SocialLinks.id]
}

Table SocialLinks {
  id integer [pk]
  name varchar
  url varchar
}

Table ProfileToRole {
  id integer [pk]
  profile_id integer [ref: > Profile.id]
  role_id integer [ref: > Role.id]
  is_main bool
  level Level
  Note: 'Конкретно роль пользователя'
}

Table Role {
  id integer [pk]
  role_name varchar
  Note: 'Таблица для нормализации ролей'
}

Table ProfileToTool {
  profile_id integer [ref: > Profile.id]
  tool_id integer [ref: > Tool.id]
  level Level
}

Table Tool {
  id integer [pk]
  tool_name varchar
}

enum Level {
  trainee
  intern
  junior
  middle
  senior
}

Table Material {
  id integer [pk]
  image_url varchar
  title varchar
  description varchar
  link varchar
}

// Новости скип

Table Project {
  id integer [pk]
  name varchar
  core_idea varchar
  description text
  finish_date date [null]
  type_id integer [ref: > ProjectType.id]
  status ProjectStatus
}

enum ProjectStatus {
  not_started
  in_process
  not_finished
  finished
}

Table ProjectToTool {
  id integer [pk]
  tool_id integer [ref: > Tool.id]
  project_id integer [ref: > Project.id]
}

Table ProjectParticipants {
  id integer [pk]
  project_id integer [ref: > Project.id]
  profile_id integer [ref: > Profile.id]
  participant_info_id integer [ref: > ParticipantInfo.id, note: 'one-to-one']
}

Table ParticipantInfo {
  id integer [pk]
  participant_type ParticipantType [Note: 'Отвачает за уровень доступа к проекту']
  role_id integer [ref: > Role.id]
  Note: 'Хранит информацию об участнике в контексте проекта'
}

enum ParticipantType {
  creator
  admin
  participant
}

Table ProjectType {
  id integer [pk]
  type_name varchar
}

Table ProjectToRole {
  id integer [pk]
  project_id integer [ref: > Project.id]
  role_id integer [ref: > Role.id]
  amount integer [note: 'Количество требуемых людей с этой ролью']
}

Table ProjectToTag {
  id integer [pk]
  project_id integer [ref: > Project.id]
  tag_id integer [ref: > Tag.id]
}

Table Tag {
  id integer [pk]
  tag_name varchar
}

Table ProjectParticipationRequest {
  id integer [pk]
  profile_id integer [ref: > Profile.id]
  project_id integer [ref: > Project.id]
  cover_letter text
  resume_url varchar [null]
  status RequestStatus
}

enum RequestStatus {
  pending
  accepted
  declined
}

Table Award {
  id integer [pk]
  name varchar
  description varchar
  image_url varchar
}
```