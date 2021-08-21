from budget.common.datetime import DateTime
from budget.models.field import Field
from budget.models.model import Model


class Transaction(Model):
    id = Field(str)
    name = Field(str)
    from_ = Field(str)
    to = Field(str)
    value = Field(float)
    pay_date = Field(DateTime)
    start_date = Field(DateTime)
    due_date = Field(DateTime)
    planned_value = Field(float)
    planned = Field(bool) 
    comment = Field(str)
    tag = Field(str)