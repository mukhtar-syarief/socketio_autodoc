import socketio

from ..fixture.socket import *
from pdc_event_autodoc.documentation import SocketDocumentation


sm: socketio.AsyncServer = socketio.AsyncServer()

doc= SocketDocumentation()

base_data = {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {},
    'components': {
        'messages': {},
        'schemas': {}
    }
}

doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')


@doc.sub(event_name= 'pydantic', tags= ['SubPydantic'], schema= PydanticModel, summary= 'PydanticModel', description= 'Test create socket with data using pydantic model')
@doc.pub(event_name= 'pydantic', tags= ['PubPydantic'])
@sm.on('pydantic')
def test_schema_pydantic(sid, data: PydanticModel):
    print('success')

assert doc.main_data.asyncapi == '2.2.0'

assert doc.main_data.info == {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    }

assert doc.main_data.components == {
        'messages':{
            'pydantic': {
                'payload': {
                    '$ref': '#/components/schemas/pydantic'
                }
            }
        },
        'schemas': {
            'pydantic': {
                'type': 'object',
                'properties': {
                    'id':{
                        'type': 'integer',
                        'title': 'Id'
                    },
                    'name': {
                        'type': 'string',
                        'title': 'Name'
                    },
                    'address': {
                        'type': 'string',
                        'title': 'Address'
                    }
                },
                'required': ['id', 'name', 'address'],
                'title': 'PydanticModel'
            }
        }
    }

assert doc.main_data.channels == {
        'pydantic': {
            'subscribe': {
                'summary': 'PydanticModel',
                'description': 'Test create socket with data using pydantic model',
                'message':{
                    '$ref': '#/components/messages/pydantic'
                },
                'tags': [
                    {
                        'name': 'SubPydantic'
                    }
                ]
            },
            'publish':{
                'summary': '',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/pydantic'
                },
                'tags': [
                    {
                        'name': 'PubPydantic'
                    }
                ]
            }
        }
    }

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {
        'pydantic': {
            'subscribe': {
                'summary': 'PydanticModel',
                'description': 'Test create socket with data using pydantic model',
                'message':{
                    '$ref': '#/components/messages/pydantic'
                },
                'tags': [
                    {
                        'name': 'SubPydantic'
                    }
                ]
            },
            'publish':{
                'summary': '',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/pydantic'
                },
                'tags': [
                    {
                        'name': 'PubPydantic'
                    }
                ]
            }
        }
    },
    'components': {
        'messages':{
            'pydantic': {
                'payload': {
                    '$ref': '#/components/schemas/pydantic'
                }
            }
        },
        'schemas': {
            'pydantic': {
                'type': 'object',
                'properties': {
                    'id':{
                        'type': 'integer',
                        'title': 'Id'
                    },
                    'name': {
                        'type': 'string',
                        'title': 'Name'
                    },
                    'address': {
                        'type': 'string',
                        'title': 'Address'
                    }
                },
                'required': ['id', 'name', 'address'],
                'title': 'PydanticModel'
            }
        }
    }
}

doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')

@doc.sub(event_name= 'general_type', tags= ['TypeBiasa'])
@doc.pub(event_name= 'general_type', summary= 'type data biasa', description= 'Test untuk type data biasa str, int, bool')
@sm.on('general_type')
def test_general_type(sid, type_str: str):
    print('success')

assert doc.main_data.channels == {
        'general_type':{
            'subscribe': {
                'summary': '',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/general_type'
                },
                'tags': [
                    {
                        'name': 'TypeBiasa'
                    }
                ]
            },
            'publish': {
                'summary': 'type data biasa',
                'description': 'Test untuk type data biasa str, int, bool',
                'message': {
                    '$ref': '#/components/messages/general_type'
                },
                'tags': []
            }
        }
    }

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {
        'general_type':{
            'subscribe': {
                'summary': '',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/general_type'
                },
                'tags': [
                    {
                        'name': 'TypeBiasa'
                    }
                ]
            },
            'publish': {
                'summary': 'type data biasa',
                'description': 'Test untuk type data biasa str, int, bool',
                'message': {
                    '$ref': '#/components/messages/general_type'
                },
                'tags': []
            }
        }
    },
    'components': {
        'messages': {
            'general_type': {
                'payload': {
                    '$ref': '#/components/schemas/general_type'
                }
            }
        },
        'schemas': {
            'general_type': {
                'type': 'string',
                'title': 'ParsingModel[str]'
            }
        }
    }
}


doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')

@doc.sub(event_name= 'list_type', tags= ['UsingListType', 'List'], summary= 'Pakai data list')
@doc.pub(event_name= 'list_type', description= 'Use to identify type of params is list')
@sm.on('list_type')
def test_list_type(sid, type_list: List[str]):
    print('success')

assert doc.main_data.channels == {
        'list_type':{
            'subscribe': {
                'summary': 'Pakai data list',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/list_type'
                },
                'tags': [
                    {
                        'name': 'UsingListType'
                    },{
                        'name': 'List'
                    }
                ]
            },
            'publish': {
                'summary': '',
                'description': 'Use to identify type of params is list',
                'message': {
                    '$ref': '#/components/messages/list_type'
                },
                'tags': []
            }
        }
    }

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {
        'list_type':{
            'subscribe': {
                'summary': 'Pakai data list',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/list_type'
                },
                'tags': [
                    {
                        'name': 'UsingListType'
                    },{
                        'name': 'List'
                    }
                ]
            },
            'publish': {
                'summary': '',
                'description': 'Use to identify type of params is list',
                'message': {
                    '$ref': '#/components/messages/list_type'
                },
                'tags': []
            }
        }
    },
    'components': {
        'messages': {
            'list_type': {
                'payload': {
                    '$ref': '#/components/schemas/list_type'
                }
            }
        },
        'schemas': {
            'list_type': {
                'title': 'ParsingModel[List[str]]',
                'type': 'array',
                'items':{
                    'type': 'string'
                }
            }
        }
    }
}




doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')

@doc.sub(event_name= 'union_type', tags= ['Union'], summary= 'Test union type')
@doc.pub(event_name= 'union_type', tags= ['UnionPub'], description= 'Tipe Union untuk publish')
@sm.on('union_type')
def test_union_type(sid, type_union: Union[str, int]):
    print('success')

assert doc.main_data.channels == {
        'union_type':{
            'subscribe': {
                'summary': 'Test union type',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/union_type'
                },
                'tags': [
                    {
                        'name': 'Union'
                    }
                ]
            },
            'publish': {
                'summary': '',
                'description': 'Tipe Union untuk publish',
                'message': {
                    '$ref': '#/components/messages/union_type'
                },
                'tags': [
                    {
                        'name': 'UnionPub'
                    }
                ]
            }
        }
    }

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {
        'union_type':{
            'subscribe': {
                'summary': 'Test union type',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/union_type'
                },
                'tags': [
                    {
                        'name': 'Union'
                    }
                ]
            },
            'publish': {
                'summary': '',
                'description': 'Tipe Union untuk publish',
                'message': {
                    '$ref': '#/components/messages/union_type'
                },
                'tags': [
                    {
                        'name': 'UnionPub'
                    }
                ]
            }
        }
    },
    'components': {
        'messages': {
            'union_type': {
                'payload': {
                    '$ref': '#/components/schemas/union_type'
                }
            }
        },
        'schemas': {
            'union_type': {
                'title': 'ParsingModel[Union[str, int]]',
                'anyOf':[
                    {
                        'type': 'string'
                    },{
                        'type': 'integer'
                    }
                ]
                }
            }
        }
    }


doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')

@doc.sub(event_name= 'union_pydantic', tags= ['SubUnionPydantic'], description= 'Untuk mengecek type data params berupa union dan model pydantic')
@doc.pub(event_name= 'union_pydantic', tags= ['PubUnionPydantic'], summary= 'Model Union Pydantic')
@sm.on('union_pydantic')
def test_union_pydantic(sid, type_union_pydantic: Union[str, PydanticModel]):
    print('success')

assert doc.main_data.channels == {
        'union_pydantic':{
            'subscribe': {
                'summary': '',
                'description': 'Untuk mengecek type data params berupa union dan model pydantic',
                'message': {
                    '$ref': '#/components/messages/union_pydantic'
                },
                'tags': [
                    {
                        'name': 'SubUnionPydantic'
                    }
                ]
            },
            'publish': {
                'summary': 'Model Union Pydantic',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/union_pydantic'
                },
                'tags': [
                    {
                        'name': 'PubUnionPydantic'
                    }
                ]
            }
        }
    }

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {
        'union_pydantic':{
            'subscribe': {
                'summary': '',
                'description': 'Untuk mengecek type data params berupa union dan model pydantic',
                'message': {
                    '$ref': '#/components/messages/union_pydantic'
                },
                'tags': [
                    {
                        'name': 'SubUnionPydantic'
                    }
                ]
            },
            'publish': {
                'summary': 'Model Union Pydantic',
                'description': '',
                'message': {
                    '$ref': '#/components/messages/union_pydantic'
                },
                'tags': [
                    {
                        'name': 'PubUnionPydantic'
                    }
                ]
            }
        }
    },
    'components': {
        'messages': {
            'union_pydantic': {
                'payload': {
                    '$ref': '#/components/schemas/union_pydantic'
                }
            }
        }, 
        'schemas': {
            'union_pydantic': {
                'title': 'ParsingModel[Union[str, PydanticModel]]', 
                'anyOf': [
                    {
                        'type': 'string'
                    }, {
                        '$ref': '#/components/schemas/PydanticModel'
                    }
                ]
            },
            'PydanticModel': {
                'title': 'PydanticModel', 
                'type': 'object', 
                'properties': {
                    'id': {
                        'title': 'Id', 
                        'type': 'integer'
                    }, 
                    'name': {
                        'title': 'Name', 
                        'type': 'string'
                    }, 
                    'address': {
                        'title': 'Address', 
                        'type': 'string'
                    }
                }, 
                'required': [
                    'id', 
                    'name', 
                    'address'
                ]
            }
        }
    }
}


{
'schemas': {
    'PydanticModel': {
        'title': 'PydanticModel', 
        'type': 'object', 
        'properties': {
            'id': {
                'title': 'Id', 
                'type': 'integer'
            }, 
            'name': {
                'title': 'Name', 
                'type': 'string'
            }, 
            'address': {
                'title': 'Address', 
                'type': 'string'
                }
            }, 
        'required': [
            'id', 
            'name', 
            'address'
        ]
    }
}
}



doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')


@doc.sub(event_name= 'test_optional')
@doc.pub(event_name= 'test_optional')
@sm.on('test_optional')
def test_using_optional_params(sid, type_optional: Optional[str]):
    print('success')

assert doc.main_data.channels == {
    'test_optional': {
        'subscribe': {
            'summary': '',
            'description': '',
            'message': {
                '$ref': '#/components/messages/test_optional'
            },
            'tags': []
        },
        'publish': {
            'summary': '',
            'description': '',
            'message': {
                '$ref': '#/components/messages/test_optional'
            },
            'tags': []
        }
    }
}

assert doc.main_data.dict() == {
    'asyncapi': '2.2.0',
    'info': {
        'title': 'Test Aplications',
        'version': '0.0.1',
        'description': 'Hanya untuk test'
    },
    'channels': {
    'test_optional': {
        'subscribe': {
            'summary': '',
            'description': '',
            'message': {
                '$ref': '#/components/messages/test_optional'
            },
            'tags': []
        },
        'publish': {
            'summary': '',
            'description': '',
            'message': {
                '$ref': '#/components/messages/test_optional'
            },
            'tags': []
        }
    }
},
    'components': {
        'messages': {
            'test_optional': {
                'payload': {
                    '$ref': '#/components/schemas/test_optional'
                }
            }
        }, 
        'schemas': {
            'test_optional': {
                'title': 'ParsingModel[Union[str, NoneType]]', 
                'type': 'string'
            }
        },
    }
}



doc.reset_documentation()
doc.set_info_app(title= 'Test Aplications', version= '0.0.1', description= 'Hanya untuk test')


# @doc.pub(event_name='using_schema', schema= PydanticModel)
# @sm.on('using_schema')
# def create_using_schema(sid, data: List[str]):
#     print('pass')

# from pprint import pprint
# pprint(doc.main_data.dict())
# assert True == False




@doc.sub(event_name= 'nested')
@doc.pub(event_name= 'nested', schema= NestedPydantic)
@sm.on('pydantic')
def test_schema_nested_pydantic(sid, nested: NestedPydantic):
    print('success')

print(doc.main_data.dict())
assert doc.main_data.dict() == {
    'asyncapi': '2.2.0', 
    'info': {
        'title': 'Test Aplications', 
        'version': '0.0.1', 
        'description': 'Hanya untuk test'
        }, 
    'channels': {
        'nested': {
            'subscribe': {
                'summary': '', 
                'description': '', 
                'message': {
                    '$ref': '#/components/messages/nested'
                    }, 
                'tags': []
                }, 
            'publish': {
                'summary': '', 
                'description': '', 
                'message': {
                    '$ref': '#/components/messages/nested'
                    }, 
                'tags': []
                }
            }
        }, 
    'components': {
        'messages': {
            'nested': {
                'payload': {
                    '$ref': '#/components/schemas/nested'
                    }
                }
            }, 
        'schemas': {
            'nested': {
                'title': 'NestedPydantic', 
                'type': 'object', 
                'properties': {
                    'id': {
                        'title': 'Id', 
                        'type': 'integer'
                        }, 
                    'models': {
                        'title': 'Models', 
                        'type': 'array', 
                        'items': {
                            '$ref': '#/components/schemas/PydanticModel'
                            }
                        }
                    }, 
                'required': [
                    'id', 
                    'models'
                    ]
                }
            }
        }
    }
