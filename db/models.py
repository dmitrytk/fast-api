from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Field(models.Model):
    name = fields.CharField(max_length=50, unique=True)
    type = fields.CharField(max_length=50, null=True)
    location = fields.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "fields"


class Well(models.Model):
    name = fields.CharField(max_length=50)
    type = fields.CharField(max_length=50, null=True)
    bottom = fields.DecimalField(max_digits=20, decimal_places=2, null=True)
    field = fields.ForeignKeyField('models.Field', related_name='wells')

    class Meta:
        table = "wells"
        unique_together = (("field", "name"),)


FieldModel = pydantic_model_creator(Field, name="Field")
FieldInModel = pydantic_model_creator(Field, name="FieldIn", exclude_readonly=True)

WellModel = pydantic_model_creator(Well, name="Well")
WellInModel = pydantic_model_creator(Well, name="WellIn", exclude_readonly=True)
