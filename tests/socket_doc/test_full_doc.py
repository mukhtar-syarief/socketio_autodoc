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
def test_general_schema_pydantic(sid, data: PydanticModel):
    print('success')


@doc.sub(event_name= 'general_type', tags= ['TypeBiasa'])
@doc.pub(event_name= 'general_type', summary= 'type data biasa', description= 'Test untuk type data biasa str, int, bool')
@sm.on('general_type')
def test_general_type_data(sid, type_str: str):
    print('success')


@doc.sub(event_name= 'list_type', tags= ['UsingListType', 'List'], summary= 'Pakai data list')
@doc.pub(event_name= 'list_type', description= 'Use to identify type of params is list')
@sm.on('list_type')
def test_list_type_data(sid, type_list: List[str]):
    print('success')


@doc.sub(event_name= 'union_type', tags= ['Union'], summary= 'Test union type')
@doc.pub(event_name= 'union_type', tags= ['UnionPub'], description= 'Tipe Union untuk publish')
@sm.on('union_type')
def test_union_type_data(sid, type_union: Union[str, int]):
    print('success')

@doc.sub(event_name= 'union_pydantic', tags= ['SubUnionPydantic'], description= 'Untuk mengecek type data params berupa union dan model pydantic')
@doc.pub(event_name= 'union_pydantic', tags= ['PubUnionPydantic'], summary= 'Model Union Pydantic')
@sm.on('union_pydantic')
def test_union_pydantic_data_with_none_type(sid, type_union_pydantic: Union[int, PydanticModel]):
    print('success')

@doc.sub(event_name= 'union_pydantic', tags= ['SubUnionPydantic'], description= 'Untuk mengecek type data params berupa union dan model pydantic')
@doc.pub(event_name= 'union_pydantic', tags= ['PubUnionPydantic'], summary= 'Model Union Pydantic')
@sm.on('union_pydantic')
def test_union_pydantic_data_with_none_type(sid, type_union_pydantic: Union[None, PydanticModel]):
    print('success')

@doc.sub(event_name= 'test_optional')
@doc.pub(event_name= 'test_optional')
@sm.on('test_optional')
def test_using_data_type_optional(sid, type_optional: Optional[str]):
    print('success')


@doc.sub(event_name= 'nested')
@doc.pub(event_name= 'nested')
@sm.on('pydantic')
def test_schema_data_nested_pydantic(sid, data: NestedPydantic):
    print('success')
