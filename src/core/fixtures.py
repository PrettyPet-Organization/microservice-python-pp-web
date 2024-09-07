# Here are functions that create test instances of specific application models

from projects.models.projects import Project
from projects.models.roles_in_project import Role
from projects.models.groups_for_projects import Group
from projects.models.tools_in_project import Tool
from projects.models.tags_in_project import Tag
from projects.models.project_types import ProjectType


def create_instance_common():
    pass


def create_instance_hackathons():
    pass


def create_instance_profiles():
    pass


def create_instance_projects():
    type1 = ProjectType.objects.create(type_name='Backend')

    role1 = Role.objects.create(role_name='Developer')
    role2 = Role.objects.create(role_name='Designer')

    group1 = Group.objects.create(group_name='Group A')

    tool1 = Tool.objects.create(tool_name='Git')
    tool2 = Tool.objects.create(tool_name='Docker')

    tag1 = Tag.objects.create(tag_name='Python')
    tag2 = Tag.objects.create(tag_name='Django')

    project1 = Project.objects.create(
        project_type=type1,
        project_name='Project 1',
        core_idea='Core idea of project 1',
        description='Description of project 1',
        finish_date='2024-12-31',
        status=Project.ProjectStatus.NOT_STARTED
    )

    # Добавление связей ManyToMany
    project1.roles.set([role1, role2])
    project1.tools.set([tool1, tool2])
    project1.tags.set([tag1, tag2])
    project1.groups.set([group1])
