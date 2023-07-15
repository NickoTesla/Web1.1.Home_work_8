from mongoengine import Document, StringField, DateTimeField, ReferenceField


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = StringField()
    author = ReferenceField(Author)
    quote = StringField()


class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)
