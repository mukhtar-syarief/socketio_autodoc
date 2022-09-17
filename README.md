# Autodoc for Socketio and Fastapi

Create autodoc for socketio and access using API Router.

Use decorator and method for describe the event running, Use sub for 'subscribe' and use pub for 'publish'.
This code also integrated with pydantic, so it will be detect data model in your params if using pydantic. 
Beside that other type data like array or general type like str, int, etc can be solved. 
Other type from python typing like Optional and Union especially Union with none type can be solved.


## Notice
Dont't forget to declare your type params (it can be Pydantic model, array, str, int, Optional or Union, etc).
If not be declare it will be detect that your function using Any params.