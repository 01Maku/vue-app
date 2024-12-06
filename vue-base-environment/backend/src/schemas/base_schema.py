from marshmallow import Schema, fields

class BaseSampleTableSchema(Schema):
    id = fields.Int(dump_only=True)
    string_data = fields.Str(required=True)
    integer_data = fields.Int(required=True)
    float_data = fields.Float(required=True)
    boolean_data = fields.Bool(default=True)
    text_data = fields.Str()
    date_data = fields.Date()

    class Meta:
        fields = ("id", "string_data", "integer_data", "float_data", "boolean_data", "text_data", "date_data")
