from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models.custom_user import CustomUser
from hackathons.models.hackathons import Hackathon
from hackathons.models.participants_in_hackathon import ParticipantsInHackathon
from profiles.models.profiles import Profile


class HackathonsTest(TestCase):

    def setUp(self):
        self.hackathon = Hackathon.objects.create(
            name="Test Hackathon",
            core_idea="Core idea",
            task="lorem task",
            image_url="lorem",
        )

    def test_success_create_hackathon(self):

        hackathon = Hackathon.objects.create(
            name="Hackathons New",
            core_idea="Core idea",
            task="lorem task",
            image_url="lorem",
        )

        self.assertIsInstance(hackathon, Hackathon)
        self.assertEqual(hackathon.name, "Hackathons New")
        self.assertTrue(hackathon.core_idea, self.hackathon.core_idea)

    def test_bad_name_max_length(self):

        max_length = Hackathon._meta.get_field("name").max_length
        long_name = "A" * max_length

        hackathon = Hackathon(name=long_name)
        hackathon.full_clean()

        exceeded_name = "A" * (max_length + 1)
        hackathon = Hackathon(name=exceeded_name)

        with self.assertRaises(ValidationError) as context:
            hackathon.full_clean()
        self.assertEqual(
            context.exception.message_dict["name"][0],
            "Ensure this value has at most 40 characters (it has 41).",
        )

    def test_hackathon_field(self):
        hackathon1 = Hackathon.objects.create(name="Hackathons New")
        hackathon2 = Hackathon.objects.create(name="Hackathons New")
        self.assertNotEqual(hackathon1.hackathon, hackathon2.hackathon)


class ParticipantInHackathonTest(TestCase):
    def setUp(self):

        user = CustomUser.objects.create_user(
            username="existinguser",
            email="existinguser@example.com",
            password="Testpassword123",
        )
        self.hackathon = Hackathon.objects.create(name="Test Hackathon")
        self.profile = Profile.objects.create(user=user)
        self.participants = ParticipantsInHackathon.objects.create(
            profile=self.profile,
        )

    def test_succes_create_participant(self):
        self.assertIsInstance(self.participants, ParticipantsInHackathon)

    def test_unique_participant(self):
        user = CustomUser.objects.create_user(
            username="existinguser1",
            email="existinguser1@example.com",
            password="Testpassword123",
        )
        profile = Profile.objects.create(user=user)
        participants = ParticipantsInHackathon.objects.create(profile=profile)

        self.assertNotEqual(participants.participant, self.participants.participant)
