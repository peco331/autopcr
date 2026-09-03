"""Pydantic v1 API compatibility for both Pydantic 1 and 2 runtimes."""

try:
    from pydantic.v1 import BaseModel, Field
    from pydantic.v1.class_validators import make_generic_validator
    from pydantic.v1.fields import ModelField
    from pydantic.v1.generics import GenericModel
    from pydantic.v1.main import object_setattr, validate_model
    from pydantic.v1.validators import int_validator
except ImportError:
    from pydantic import BaseModel, Field
    from pydantic.class_validators import make_generic_validator
    from pydantic.fields import ModelField
    from pydantic.generics import GenericModel
    from pydantic.main import object_setattr, validate_model
    from pydantic.validators import int_validator
