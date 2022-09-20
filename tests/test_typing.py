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


@pytest.fixture
def data_connect() -> Event[ConnectEvent]:
    return Event(shopid= 1, data= ConnectEvent(connect_id = 1))

@pytest.fixture
def data_disconnect() -> Event[DisconnectEvent]:
    return Event(data= DisconnectEvent(msg= 'disconnect', msgId=1), shopid= 1)


@doc.sub('disconnect')
def test_generic_data_disconnect(data_disconnect: Event[DisconnectEvent]):
    pass


assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': '',
        'version': '',
        'description': '',
    },
    'channels': {
        'disconnect': {
            'subscribe': {
                'summary': '',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/disconnect'
                },
                'tags': []
            }
        }
    },
    'components': {
        'messages': {
            'disconnect': {
                'payload': {
                    '$ref': '#/components/schemas/disconnect'
                }
            }
        },
        'schemas': {
            'DisconnectEvent': {
                'properties': {
                    'msg': {
                        'title': 'Msg', 
                        'type': 'string'
                        },
                    'msgId': {
                        'title': 'Msgid',
                        'type': 'integer'
                        }
                    },
                'required': ['msg', 'msgId'],
                'title': 'DisconnectEvent',
                'type': 'object'},
            'disconnect': {
                'properties': {
                    'data': {
                        '$ref': '#/components/schemas/DisconnectEvent'
                        },
                    'shopid': {
                        'title': 'Shopid',
                        'type': 'integer'
                        }
                    },
                'required': [
                    'data', 
                    'shopid'
                    ],
                'title': 'Event[DisconnectEvent]',
                'type': 'object'
            }
        }
    }
}


@doc.sub('connect')
def test_generic_data_connect(data_connect: Event[ConnectEvent]):
    pass

pprint(doc.main_data.dict())

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'channels': {
        'connect': {
            'subscribe': {
                'description': '',
                'message': {'$ref': '#/components/messages/connect'},
                'summary': '',
                'tags': []
                }
            },
        'disconnect': {
            'subscribe': {
                'description': '',
                'message': {'$ref': '#/components/messages/disconnect'},
                'summary': '',
                'tags': []
                }
            }
        },
    'components': {
        'messages': {
            'connect': {
                'payload': {
                    '$ref': '#/components/schemas/connect'
                    }
                },
            'disconnect': {
                'payload': {
                    '$ref': '#/components/schemas/disconnect'
                    }
                }
            },
        'schemas': {
            'ConnectEvent': {
                'properties': {
                    'connect_id': {
                        'title': 'Connect ''Id',
                        'type': 'integer'}},
                'required': [
                    'connect_id'
                    ],
                'title': 'ConnectEvent',
                'type': 'object'
                },
            'DisconnectEvent': {
                'properties': {
                    'msg': {
                        'title': 'Msg',
                        'type': 'string'
                        },
                    'msgId': {
                        'title': 'Msgid',
                        'type': 'integer'
                        }
                    },
                'required': [
                    'msg', 
                    'msgId'
                    ],
                'title': 'DisconnectEvent',
                'type': 'object'
                },
            'connect': {
                'properties': {
                    'data': {
                        '$ref': '#/components/schemas/ConnectEvent'
                        },
                    'shopid': {
                        'title': 'Shopid',
                        'type': 'integer'
                        }
                    },
                'required': [
                    'data', 
                    'shopid'
                    ],
                'title': 'Event[ConnectEvent]',
                'type': 'object'
                },
            'disconnect': {
                'properties': {
                    'data': {
                        '$ref': '#/components/schemas/DisconnectEvent'
                        },
                    'shopid': {
                        'title': 'Shopid',
                        'type': 'integer'
                        }
                    },
                'required': ['data', 'shopid'],
                'title': 'Event[DisconnectEvent]',
                'type': 'object'
                }
            }
        },
 'info': {
    'description': '', 
    'title': '', 
    'version': ''
    }
}


def test_event_disconnect():
    print(SocketDocumentation.main_data.dict())




    
