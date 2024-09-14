## 1. Role
1. role_name: CharField

## 2. Tool
1. tool_name: CharField

## 3. Tag
1. tag_name: CharField

## 4. News
1. author: ForeignKey(to=Profile)
2. title: CharField
3. description: CharField
4. image_url: ImageField
5. likes: PositiveIntegerField
6. is_open: BooleanField
7. topics: ManyToManyField
8. tags: ForeignKey(to=Tag)

## 5. SocialLink
1. link_name: CharField
2. url: URLField

## 6. Topic
1. topic_name = CharField

## 7. UsefulMaterial
1. title: CharField
2. description: CharField
3. image_url: ImageField
4. likes: PositiveIntegerField
5. link_name: CharField