from peewee import *

db = SqliteDatabase('my_aggregator.db')


class BaseModel(Model):
    class Meta:
        database = db


class Feed(BaseModel):
    name = TextField(default="")


class BanWord(BaseModel):
    word = TextField(unique=True)
    is_a_hashtag = BooleanField(default=False)


class WhiteWord(BaseModel):
    word = TextField(unique=True)
    is_a_hashtag = BooleanField(default=False)


class Channel(BaseModel):
    channel_id = IntegerField(unique=True)
    name = TextField()
    is_black_list_enabled = BooleanField(default=False)
    is_white_list_enabled = BooleanField(default=False)
    is_messages_types_sort_enabled = BooleanField(default=False)


class MessageType(BaseModel):
    type = TextField(unique=True)


class FeedChannel(BaseModel):
    feed = ForeignKeyField(Feed)
    channel = ForeignKeyField(Channel)


class ChannelBanWord(BaseModel):
    channel = ForeignKeyField(Channel)
    ban_word = ForeignKeyField(BanWord)


class ChannelWhiteWord(BaseModel):
    channel = ForeignKeyField(Channel)
    white_word = ForeignKeyField(WhiteWord)


class ChannelMessageType(BaseModel):
    channel = ForeignKeyField(Channel)
    message_type = ForeignKeyField(MessageType)


def create_tables():
    with db:
        db.create_tables([
            Feed,
            BanWord,
            WhiteWord,
            Channel,
            MessageType,
            FeedChannel,
            ChannelBanWord,
            ChannelWhiteWord,
            ChannelMessageType
        ])
