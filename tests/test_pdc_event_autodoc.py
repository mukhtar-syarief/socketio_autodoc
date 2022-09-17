from pdc_event_autodoc import __version__, SocketDocumentation


def test_version():
    assert __version__ == '0.1.0'

def test_socket_data():
    assert SocketDocumentation.main_data == {
        'asyncapi': '2.2.0',
        'info': {
            'title': '',
            'version': '',
            'description': ''
        },
        'channels': {},
        'components': {
            'messages': {},
            'schemas': {}
        }
    }