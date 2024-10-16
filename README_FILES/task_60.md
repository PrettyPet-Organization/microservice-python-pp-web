# Задача 60 Написать ApiView для главной страницы(Проекты)

## Нужно написать ApiView, которое бы отдавала на фронт динамический JSON. Он берет из БД 6 проектов. 

### Условия:
* 3 из них уже завершены. 3 в процессе. 
* Нельзя, чтобы все 6 проектов имели  одинаковый срок.
* Нельзя, чтобы стек повторялся(именно полная идентичность всех технологий).
* Нельзя, чтобы было 3+ проекта с одинаковым количеством участников.
* Добавить вывод поля “Свободных мест”. 
* Поставить фильтр на проекты со свободными местами(запрос для тех проектов, которые в процессе).

---
## Проблемы с Моделями
  Проблемы с ленивым импортом, просто добавлю импорты в нужные места. ПРоблемы с доступом к информации и ошибки в моделях, из за этого не добавляется в миграции и нет возможности связываться с данной моделью `projects\models\participants_in_project.py` <br>
  
  `ParticipantInProject` Теперь подхватывает миграция и модель видно в базе данных


    * django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:

    ERRORS:

    - projects.ParticipantInProject.roles: (fields.E300) Field defines a relation with model 'Role', which is either not installed, or is abstract. <br>

    - projects.ParticipantInProject.roles: (fields.E307) The field projects.ParticipantInProject.roles was declared with a lazy reference to 'projects.role', but app 'projects' doesn't provide model 'role'. <br>

    - projects.ParticipantInProject.tools: (fields.E300) Field defines a relation with model 'Tool', which is either not installed, or is abstract.<br>

    - projects.ParticipantInProject.tools: (fields.E307) The field projects.ParticipantInProject.tools was declared with a lazy reference to 'projects.tool', but app 'projects' doesn't provide model 'tool'.<br>

    - projects.RolesInProject: (fields.E336) The model is used as an intermediate model by 'projects.ParticipantInProject.roles', but it does not have a foreign key to 'ParticipantInProject' or 'projects.Role'. <br>

    - projects.ToolsInProject: (fields.E336) The model is used as an intermediate model by 'projects.ParticipantInProject.tools', but it does not have a foreign key to 'ParticipantInProject' or 'projects.Tool'. <br> 

### Изменения в моделях
Наличие поля `participant` позволяет легко выполнять запросы, которые связывают участников с их ролями и инструментами, можно четко определить, что конкретный участник имеет определенную роль или использует определенный инструмент в проекте.<br><br>

Модель `RolesInProject` и Модель `ToolsInProject` 
добавлен новый столбец:
  - `participant`: 
    - Тип: `ForeignKey` на модель `ParticipantInProject`.
    - Описание: Указывает на участника проекта, который использует этот инструмент.
    - Поведение: Удаление участника приводит к удалению записи из этой модели (`CASCADE`).


### Класс `ProjectsOverviewView`

 - ### Возвращает json с отфильтрованым списком проектов

#### 1. **Метод `query_to_json`**
   - **Описание**: Преобразует набор данных проектов в формат, который можно сериализовать в json.
   - **Логика**:
     - Вычисляет количество требуемых участников для каждого проекта.
     - Считает текущее количество участников в проекте.
     - Рассчитывает количество свободных мест для участников.
     - Возвращает список проектов с полями: ID проекта, название, статус, количество требуемых участников, свободные места, дата завершения, и используемые технологии.

#### 2. **Метод `filter_unique_dates`**
   - **Описание**: Фильтрует проекты, чтобы каждый проект имел уникальную дату завершения.
   - **Логика**:
     - Сохраняет уникальные проекты с уникальными датами завершения в новый список.
     - Возвращает список проектов с уникальными датами.

#### 3. **Метод `filter_unique_tools`**
   - **Описание**: Фильтрует проекты, чтобы каждый имел уникальный набор инструментов.
   - **Логика**:
     - Сравнивает набор инструментов каждого проекта и сохраняет только уникальные комбинации в список.
     - Возвращает проекты с уникальными наборами инструментов.

#### 4. **Метод `filter_participants_amount`**
   - **Описание**: Фильтрует проекты, чтобы в итоговом списке было не более трёх проектов с одинаковым количеством требуемых участников.
   - **Логика**:
     - Отслеживает количество проектов с одинаковым числом требуемых участников.
     - Ограничивает количество проектов с одинаковым числом участников до трёх.

#### 5. **Метод `filter_free_slots`**
   - **Описание**: Фильтрует проекты, в которых есть свободные места для участников.
   - **Логика**:
     - Считает разницу между требуемыми и фактическими участниками.
     - Возвращает проекты, где есть хотя бы одно свободное место.

#### 6. **Метод `get`**
   - **Описание**: Обрабатывает GET-запрос для получения проектов для главной страницы.
   - **Логика**:
     - Получает по 8 незавершённых и завершённых проектов, отсортированных по дате завершения.
     - Применяет фильтры для уникальности дат, инструментов, количества участников и наличия свободных мест.
     - Возвращает до 6 проектов в формате JSON, отфильтрованных по вышеописанным критериям.

### Общая логика
Методы предназначены для фильтрации и отображения проектов на главной странице, с учётом уникальных условий: уникальные даты завершения, уникальные инструменты, ограниченное количество проектов с одинаковым числом участников, и фильтрация по наличию свободных мест.

Это обновление позволяет более эффективно управлять списком проектов и отфильтровывать их по различным критериям перед выводом на главную страницу приложения.