# Созданы модели:

## 1. Project

1. project_name: CharField
2. project_type: ForeignKey to=ProjectType
3. core_idea:    CharField
4. description:  TextField
5. finish_date:  DateField
6. status:       CharField
7. tools:        ManyToManyField(to=Tools, through=ToolsInProject)
8. roles:        ManyToManyField(to=Role, through=RolesInProject)
9. tags:         ManyToManyField(to=Tag)
10. groups:      ManyToManyField(to=Group)

## 2. ProjectType

1. type_name: CharField

## 3.RolesInProject
1. role: ForeignKey(to=Role)
2. project: ForeignKey(to=Project)
3. participants_needed: PositiveIntegerField

## 4. ToolsInProject
1. tool: ForeignKey(to=Tool)
2. project: ForeignKey(to=Project)
3. participants_needed: PositiveIntegerField

## 5. Tag
1. tag_name = CharField

## 6. Group

1. group_name = CharField

## 7. ParticipantInProject

1. project: ForeignKey(to=Project)
2. profile: ForeignKey(to=Profile)
3. roles: ManyToManyField(to=Role, through=RolesInProject)
4. tools: ManyToManyField(to=Tool, through=ToolsInProject)
5. groups: ManyToManyField(to=Group)

## 8. ProjectParticipationRequest

1. profile: ForeignKey(to=Profile)
2. project: ForeignKey(to=Project)
3. cover_letter: TextField
4. resume_url: URLField
5. status: CharField

# Для запуска скрипта:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py create_instance_projects
```

# Также для всех моделей созданы сериализаторы

## Пример на проекте

    class ProjectsSerializer(ModelSerializer):
        roles = RolesInProjectSerializer(many=True, source="rolesinproject_set")
        tools = ToolsInProjectSerializer(many=True, source="toolsinproject_set")
        tags = TagsSerializer(many=True)
        groups = GroupSerializer(many=True)
    
        class Meta:
            model = Project
            fields = [
                "project_type",
                "project_name",
                "core_idea",
                "description",
                "finish_date",
                "status",
                "tools",
                "roles",
                "tags",
                "groups",
        ]

P.S декоратор **@property** использован для функции is_finished модели проекта