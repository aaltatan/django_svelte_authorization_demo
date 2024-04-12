from ninja import Schema


class CustomerSchemaBase(Schema):
    name: str
    age: int


class CustomerSchemaIn(CustomerSchemaBase): ...


class CustomerSchemaOut(CustomerSchemaBase): ...
