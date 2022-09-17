import pytest
from typing import TypeVar, Generic
from pydantic.generics import GenericModel
from pydantic import BaseModel
from pprint import pprint

from pdc_event_autodoc import SocketDocumentation

T = TypeVar('T')


doc = SocketDocumentation()


class Event(GenericModel, Generic[T]):
    data: T
    shopid: int
    
    
class DisconnectEvent(BaseModel):
    msg: str
    msgId: int
    
    
class ConnectEvent(BaseModel):
    connect_id: int


@doc.sub('disconnect')
def generic(data: Event[DisconnectEvent]):
    pass


@doc.sub('connect')
def generic(data: Event[ConnectEvent]):
    pass



pprint(SocketDocumentation.main_data.dict())




    
