# Autodoc for Socketio and Fastapi

Create autodoc for socketio and access using API Router.

Use decorator and method for describe the event running, Use sub for 'subscribe' and use pub for 'publish'.
This code also integrated with pydantic, so it will be detect data model in your params if using pydantic. 
Beside that other type data like array or general type like str, int, etc can be solved. 
Other type from python typing like Optional and Union especially Union with none type can be solved.


## Example Using

To use this import the class SokcetDocumentations, and assign the class to var.
Use decorator (@) to create documentation. There is two option to create documentation.
First is class method sub to define the event under decorator is subscribe, The second is pub to define the event or method under decorator is to publish. In this bellow is example how to use the code:

```
from pdc-event-autodoc.documentations.documentation import SocketDocumentation 

doc = SocketDocumentation()
```

First time is set your application info like bellow:
```
doc.set_info_app(title= 'Example', version= '1.0.0', description= 'This is example documentation of Example app version 1.0.0')
```



You can decla your params using pydantic model:
```
class PydanticModel(BaseModel):
    id: int
    name: str
    address: str

# Example using pydantic model
@doc.sub(event_name= 'message', 
        tags= ['SubcribeMessage'], 
        schema= PydanticModel, 
        summary= 'ReceiveMessage', 
        description= 'This is event when we receive a message.')
@sm.on('message')
def test_general_schema_pydantic(sid, data: PydanticModel):
    return data.dict()
```

Or using general type like 
```
@doc.pub(event_name= 'message', 
        tags= ['PublishMessage'],
        summary= 'To Send a Message', 
        description= 'This is event when we want to send a message.')
@sm.on('message')
def test_general_schema_pydantic(sid, data: str):
    return sm.emit(sid, data)
```


## Notice
### Dont't forget to declare your type params (it can be Pydantic model, array, str, int, Optional or Union, etc).
### If not be declare it will be detect that your function using Any params.