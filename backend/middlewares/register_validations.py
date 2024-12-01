from marshmallow import Schema, fields, validate  # type: ignore


class RegisterSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3), error_messages={"required": "Username is required"})
    email = fields.Email(required=True, error_messages={"required": "Email is required"})
    password = fields.Str(required=True, validate=validate.Length(min=8), error_messages={"required": "Password is required"})
    password_confirm = fields.Str(required=True, validate=validate.Length(min=8), error_messages={"required": "Password confirmation is required"})


register_schema = RegisterSchema()
