import logging
import struct
from collections import defaultdict
from datetime import date
from datetime import datetime

import AlcholInspection.models as m

logger = logging.getLogger(__name__)


def ping(pdata, ipaddress):
    """
    ping 命令
    :param pdata: 数据
    :param ipaddress: 客户端IP
    :return:
    """
    logger.debug("ping from {}".format(ipaddress))
    try:
        rec, _ = m.ClientStatus.objects.filter(client__ipaddress=ipaddress).get_or_create(defaults={
            'client': m.ClientRegistration.objects.filter(ipaddress=ipaddress, enabled=True).get(),
            'status': 0,
        })
        rec.status_update = datetime.now()
        rec.save()
    except m.ClientRegistration.MultipleObjectsReturned:
        pass


def command_not_exist(pdata, ipaddress):
    logger.debug("command not exits!")

    def empty_func(pdata, ipaddress):
        return None

    return empty_func


def upload(pdata, ipaddress):
    logger.debug("Upload command start")

    rec = m.InspectionRecord.objects.create(
        aircrew=''.join([chr(int(hex(x), 16)) for x in pdata[:8]]),
        value=struct.unpack('f', pdata[8:12])[0],
        drunk=pdata[12],
        unit=pdata[13],
        datetime=datetime.strptime('{}{}'.format(
            pdata[14:22].decode('ascii'),
            pdata[22:].decode('ascii')
        ),'%Y%m%d%H%M%S')
    )
    try:
        rec.client = m.ClientRegistration.objects.get(ipaddress=ipaddress)
    except Exception as e:
        logger.exception("error occured....")
    rec.save()
    logger.debug("aircrew no: {}, alchol value:{}, is drunk:{}, unit:{},date:{}".format(
        rec.aircrew, rec.value, rec.drunk, rec.unit, rec.datetime))


def accur_time(pdata, ipaddress):
    print("accur_time")
    if hex(pdata[0]) == '0xff':
        now = datetime.now()
        ret_packet = bytearray()
        ret_packet.append(112)
        ret_packet.extend([now.year - 2000, now.month, now.day,
                           now.hour, now.minute, now.second])
        return ret_packet


def setup_ip(pdata, ipaddress):
    pass


def resend_data(pdata, ipaddress):
    pass


_commands = [
    ('0x80', ping),
    ('0x83', upload),
    ('0x70', accur_time),
    ('0x71', setup_ip),
    ('0x72', resend_data)
]

COMMANDS = defaultdict(command_not_exist, _commands)
