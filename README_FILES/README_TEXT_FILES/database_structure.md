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