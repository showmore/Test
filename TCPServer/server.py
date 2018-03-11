import socketserver
import threading

from django.conf import settings

from .handler import TcpMsgHandler


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


import logging

logger = logging.getLogger(__name__)


def run():
    logger.debug("Start tcp server at {}:{}".format(
        settings.TCPSERVER['LISTENON'], settings.TCPSERVER['PORT']))
    server_instance = Server((settings.TCPSERVER['LISTENON'], settings.TCPSERVER['PORT']), TcpMsgHandler)
    th = threading.Thread(target=server_instance.serve_forever)
    th.daemon = True
    th.start()
