from marshmallow import Schema, fields


class HashDataSchema(Schema):
    id = fields.Number()
    caption = fields.Str()
    premalink = fields.URL()
    media_type = fields.Str()
    media_product_type = fields.Str()
    timestamp = fields.DateTime()
    comment_count = fields.Number()
    like_count = fields.Number()
