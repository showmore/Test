# -*- coding: UTF-8 -*- 

from spyne import Application, rpc, ServiceBase
from spyne import Iterable,Integer, Unicode, ComplexModel,Array,String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Name(ComplexModel):
    first_name = Unicode
    last_name = Unicode

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """
        for i in range(times):
            yield u'Hello, %s' % name

    @rpc(Array(Name), _returns=Iterable(Unicode))
    def say_hello_plus(self, name_plus):
        print('---', name_plus)
        if not name_plus:
            yield 'None'

        for name in name_plus:
            print(name.first_name)
            print(name.last_name)
            yield name.first_name+name.last_name


class HelloWorldService2(ServiceBase):
    @rpc(Array(String), _returns=Iterable(Unicode))
    def say_hello_plus2(self, name_plus):
        if not name_plus:
            yield 'None'

        for name in name_plus:
            yield name

application = Application([HelloWorldService, HelloWorldService2], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://192.168.8.23:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('192.168.8.23', 8000, wsgi_application)
    server.serve_forever()