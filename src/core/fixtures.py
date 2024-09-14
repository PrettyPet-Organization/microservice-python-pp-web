# Here are functions that create test instances of specific application models

from common.models.roles import Role
from common.models.tags import Tag
from common.models.tools import Tool
from projects.models.groups_for_projects import Group
from projects.models.project_types import ProjectType
from projects.models.projects import Project
from projects.models.roles_in_project import RolesInProject
from projects.models.tools_in_project import ToolsInProject


def create_instance_common():
    pass


def create_instance_hackathons():
    pass


def create_instance_profiles():
    pass


def create_instance_projects():
    # Создание типов проектов
    type1 = ProjectType.objects.create(type_name="Backend")

    # Создание ролей
    role1 = Role.objects.create(role_name="Developer")
    role2 = Role.objects.create(role_name="Designer")

    # Создание групп
    group1 = Group.objects.create(group_name="Group A")

    # Создание инструментов
    tool1 = Tool.objects.create(tool_name="Git")
    tool2 = Tool.objects.create(tool_name="Docker")

    # Создание тегов
    tag1 = Tag.objects.create(tag_name="Python")
    tag2 = Tag.objects.create(tag_name="Django")

    # Создание проекта
    project1 = Project.objects.create(
        project_type=type1,
        project_name="Project 1",
        core_idea="Core idea of project 1",
        description="Description of project 1",
        finish_date="2024-12-31",
        status=Project.ProjectStatus.NOT_STARTED,
    )

    # Добавление информации о количестве участников для каждой роли и инструмента
    RolesInProject.objects.create(role=role1, project=project1, participants_needed=4)
    RolesInProject.objects.create(role=role2, project=project1, participants_needed=5)
    ToolsInProject.objects.create(tool=tool1, project=project1, participants_needed=6)
    ToolsInProject.objects.create(tool=tool2, project=project1, participants_needed=7)

    # Добавление связей ManyToMany
    project1.tags.set([tag1, tag2])
    project1.groups.set([group1])
