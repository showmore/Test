import socketserver
import time
import array
from AlcholInspection.models import ClientRegistration
from .commands import COMMANDS
import logging

logger = logging.getLogger(__name__)

class TcpMsgHandler(socketserver.BaseRequestHandler):

    def filter_data(self,data):
        logger.debug("RAW packet: {}".format(data))
        ret=[]
        for i in range(1, len(data) - 1):
            if i <= 6:
                ret.append(data[i])
            else:
                if data[i] == 123 or data[i] == 125:
                    if not ((123 in ret) or (125 in ret)):
                        ret.append(data[i])
                else:
                    ret.append(data[i])
        ret.insert(0,123)
        ret.append(125)
        return array.array('B',ret).tobytes()

    def validatepocket(self, data):
        logger.debug("packet: {}".format(data))
        cmd, pdata, chk = hex(data[6]), data[7:-2], hex(data[-2])
        my_chk = hex((~sum([x for x in data[:-2]]) + 1) & 0xff)
        logger.debug("chksum field in the packet is {}, the acturl checksum is {}".format(
            chk,my_chk
        ))
        if chk == my_chk:
            return cmd, pdata
        else:
            logger.debug("Chksum not equal, ignore the packet")
            return None, None


    def handle(self):
        client_ip = self.client_address[0]
        logger.debug("Client {} connected".format(client_ip))
        if not ClientRegistration.objects.filter(ipaddress=client_ip,enabled=True).exists():
            logger.debug("Ip address {} not in the device list,ignore".format(client_ip))
            return
        try:
            while True:
                #data=b''
                data=self.request.recv(1024).strip()

                # data += header
                # plen = data[2:6]
                # plen = plen[3] + int((str(plen[2]) + '00'), 16) + int((str(plen[1]) + '0000'), 16) + int(
                #     (str(plen[0]) + '000000'), 16)
                # logger.debug("Calculated packet length is {},so continue".format(plen))
                # recved = self.request.recv(plen)
                # data+=recved
                # if data.count(b'{')>1 or data.count(b'}'):
                #     data+=self.request.recv(int(data[1:].count(b'{')/2 + data.count(b'}')/2))
                (cmd, pdata) = self.validatepocket(
                    self.filter_data(data))
                logger.debug("The command of the packet is {},command data is {}".format(
                    cmd,pdata))
                if cmd is not None:
                    ret = COMMANDS[cmd](pdata, client_ip)
                    if ret is not None:
                        self.request.send(ret)
        except Exception as e:
            logger.exception("error runing command")
        finally:
            self.request.close()
