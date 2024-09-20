# Описание проделанной работы Задача #54: Создать модели приложения “Hackathons”

## Модели приложения “Hackathons” согласно плану БД.
1. groups_for_hackathons
2. groups_in_hackathon
3. hackathon_participation_request
4. hackathon_prizes
5. hackathons
6. participant_in_hackathon_groups
7. participant_in_hackathon_roles
8. participant_in_hackathon_tools
9. participants_in_hackathon
10. roles_in_hackathon
11. tags_in_hackathon
12. tools_in_hackathon

#### Так же были созданны серилиазаторы для всех моделей “Hackathons”.

#### Внесены все модели в __init__.py

####  Внесены были правки по комментариям с Гитхаба.

## Сделаны самые простые тесты для *Hackathons*.
>HackathonsTest

Где были выполненны следующие тесты:  
- [x] test_success_create_hackathon: Создается ли модель Hackathon
- [x] test_bad_name_max_length: Проверка на валидацию количество символов в name
- [x] test_hackathon_field: Проверка поля hackathon на уникальность создания с использованием одинакого нейминга


>Participant_in_hackathon

Где были выполненны следующие тесты:  
- [x] test_succes_create_participant: Создается ли модель ParticipantInHackathon
- [x] test_unique_participant: Проверка уникальность при создании



Прошелся isort, затем black.


