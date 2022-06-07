from peewee import *

db = SqliteDatabase('my_aggregator.db')


class BaseModel(Model):
    class Meta:
        database = db


class Feed(BaseModel):
    feed_id = IntegerField(unique=True)
    name = TextField()


class BanWord(BaseModel):
    ban_word_id = IntegerField(unique=True)
    word = TextField(unique=True)
    is_a_hashtag = BooleanField()


class WhiteWord(BaseModel):
    ban_word_id = IntegerField(unique=True)
    word = TextField(unique=True)
    is_a_hashtag = BooleanField()


class Channel(BaseModel):
    channel_id = IntegerField(unique=True)
    name = TextField()
    is_black_list_enabled = BooleanField()
    is_white_list_enabled = BooleanField()
    is_messages_types_sort_enabled = BooleanField()


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
