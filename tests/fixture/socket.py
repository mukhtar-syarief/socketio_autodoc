import pytest

from pydantic import BaseModel
from typing import List, Optional, Union

class PydanticModel(BaseModel):
    id: int
    name: str
    address: str


class NestedPydantic(BaseModel):
    id: int
    models: List[PydanticModel]


@pytest.fixture
def sid():
    return 'SID'

@pytest.fixture
def data() -> PydanticModel:
    return PydanticModel(id= 1, name= 'nama', address= 'address')

@pytest.fixture
def type_str() -> str:
    return 'test'

@pytest.fixture
def type_list() -> List[str]:
    return ['list']

@pytest.fixture
def type_union() -> Union[str, int]:
    return 'union'

@pytest.fixture
def type_union_pydantic() -> Union[str, PydanticModel]:
    return 'union_pydantic'

@pytest.fixture
def type_optional() -> Optional[str]:
    return 'optional'

@pytest.fixture
def nested() -> NestedPydantic:
    return NestedPydantic(id= 2, models= [PydanticModel(id= 4, name = 'tasya', address= 'malayu')])