# Here are functions that create test instances of specific application models

from projects.models.groups_for_projects import Group
from projects.models.project_types import ProjectType
from projects.models.projects import Project
from projects.models.roles_in_project import Role, RolesInProject
from projects.models.tags_in_project import Tag
from projects.models.tools_in_project import Tool, ToolsInProject
# Импорт профиля
from profiles.models.profiles import Profile
from accounts.models.custom_user import CustomUser
from profiles.models.cities import City
# Импорт хакатона
from hackathons.models.hackathons import Hackathons
from hackathons.models.hackathon_prizes import HackathonPrizes
from hackathons.models.groups_in_hackathon import GroupsInHackathon
from hackathons.models.groups_for_hackathons import GroupsForHackathons
from hackathons.models.participants_in_hackathon import ParticipantsInHackathon
from hackathons.models.participant_in_hackathon_groups import ParticipantInHackathonGroups
from hackathons.models.participant_in_hackathon_roles import ParticipantInHackathonRoles
from hackathons.models.participant_in_hackathon_tools import ParticipantInHackathonTools
from hackathons.models.hackathon_participation_request import HackathonParticipationRequest

def create_instance_common():
    pass


def create_instance_hackathons():
    # Создание пользователя
    customuser = CustomUser.objects.create(
        email='example@example.com',
        password='password123D',
        code_word='CustomUser'
    )

    # Создание города для пользователя
    city = City.objects.create(
        name='Example',
        slug='example'
    )

    # Создание профиля пользователя
    profile = Profile.objetcs.create(
        user=customuser,
        city=city,
        public_name='ExampleProfile',
        age='20'

    )

    # Создание Хакатона
    hackathons = Hackathons.objects.create(
        type_id=1,
        name='Hackathons New',
        core_idea='Core idea',
        task='lorem task',
        image_url='lorem',
        prize_id='1',
    )

    # Создание Призов Хакатона
    hackathonsprizes = HackathonPrizes.objects.create(
        prize_id=hackathons,
        name='Example Hackathons Prizes',
        description='Example Hackathons Prizes Description'
    )

    # Создание Группы Хакатона
    groupinhackathon = GroupsInHackathon.objects.create(
        group_id=1,
        hackathon_id=hackathons
    )
    groupforhackathon = GroupsForHackathons.objects.create(
        group_id=groupinhackathon,
        group_name='Example Group for Hackathons'
    )

    # Создание Участника Хакатона
    participantsinhackathon = ParticipantsInHackathon.objects.create(
        participant_id=1,
        hackathon_id=hackathons,
        profile_id=profile
    )

    # Создание Группы Участника Хакатона
    participantsinhackathongroup = ParticipantInHackathonGroups.objects.create(
        participant_id=participantsinhackathon,
        group_id=groupforhackathon
    )

    # Создание Роли Участника Хакатона
    role = Role.objects.create(role_name="Participants")

    # Создание Роли Участника хакатона
    participantsinhackathonroles = ParticipantInHackathonRoles.objects.create(
        participant_id=participantsinhackathon,
        role_id=role
    )

    # Создание Инструмента
    tool = Tool.objects.create(tool_name="Git")

    # Создание Инструмета для Участников Хакатона
    participantsinhackathontools = ParticipantInHackathonTools.objects.create(
        participant_id=participantsinhackathon,
        tool_id=tool
    )

    # Создание Обращение Участника
    participantsinhackathonrequest = HackathonParticipationRequest.objects.create(
        profile_id=tool,
        hackathon_id=hackathons
    )

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
