import socket
import random
from struct import pack, unpack
from datetime import datetime as dt
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import Integer, IpAddress, OctetString
import re
import time

def upd():
    upd = open("set", "r").read().splitlines()[0]
    return upd
upd()

def upd_time():
    current_time = time.strftime("%H : %M")
    return current_time
upd_time()

def xerox():
    try:
        ip_xerox = '192.168.1.159'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_xerox = cmdgen.UdpTransportTarget((ip_xerox, 161))
        real_fun = getattr(generator, 'getCmd')
        res_xerox = real_fun(comm_data, transport_xerox, value)
        ent_xerox = str(res_xerox)
        ent_xerox = ent_xerox[318:333]
        ent_xerox = re.findall("\d+", ent_xerox)[0]
        ent_xerox = int(ent_xerox)
        per_ent_xerox = (ent_xerox * 100 // 30000)
        return per_ent_xerox
    except:
        per_ent_xerox = "🗙"
        return per_ent_xerox
xerox()

def hp_buh():
    try:
        ip_hp_buh = '192.168.10.162'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_buh = cmdgen.UdpTransportTarget((ip_hp_buh, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_buh = real_fun(comm_data, transport_hp_buh, value)
        ent_hp_buh = str(res_hp_buh)
        ent_hp_buh = ent_hp_buh[318:333]
        ent_hp_buh = re.findall("\d+", ent_hp_buh)[0]
        return ent_hp_buh
    except:
        ent_hp_buh = "🗙"
        return ent_hp_buh
hp_buh()

def hp_secr_black():
    try:
        ip_hp_secr_black = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_secr_black = cmdgen.UdpTransportTarget((ip_hp_secr_black, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_secr_black = real_fun(comm_data, transport_hp_secr_black, value)
        ent_hp_secr_black = str(res_hp_secr_black)
        ent_hp_secr_black = ent_hp_secr_black[318:333]
        ent_hp_secr_black = re.findall("\d+", ent_hp_secr_black)[0]
        return ent_hp_secr_black
    except:
        ent_hp_secr_black = "🗙"
        return ent_hp_secr_black
hp_secr_black()

def hp_secr_cyan():
    try:
        ip_hp_secr_cyan = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,2)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_secr_cyan = cmdgen.UdpTransportTarget((ip_hp_secr_cyan, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_secr_cyan = real_fun(comm_data, transport_hp_secr_cyan, value)
        ent_hp_secr_cyan = str(res_hp_secr_cyan)
        ent_hp_secr_cyan = ent_hp_secr_cyan[318:333]
        ent_hp_secr_cyan = re.findall("\d+", ent_hp_secr_cyan)[0]
        return ent_hp_secr_cyan
    except:
        pass
hp_secr_cyan()

def hp_secr_mageneta():
    try:
        ip_hp_secr_mageneta = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,3)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_secr_mageneta = cmdgen.UdpTransportTarget((ip_hp_secr_mageneta, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_secr_mageneta = real_fun(comm_data, transport_hp_secr_mageneta, value)
        ent_hp_secr_mageneta = str(res_hp_secr_mageneta)
        ent_hp_secr_mageneta = ent_hp_secr_mageneta[318:333]
        ent_hp_secr_mageneta = re.findall("\d+", ent_hp_secr_mageneta)[0]
        return ent_hp_secr_mageneta
    except:
        pass
hp_secr_mageneta()

def hp_secr_yellow():
    try:
        ip_hp_secr_yellow = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,4)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_secr_yellow = cmdgen.UdpTransportTarget((ip_hp_secr_yellow, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_secr_yellow = real_fun(comm_data, transport_hp_secr_yellow, value)
        ent_hp_secr_yellow = str(res_hp_secr_yellow)
        ent_hp_secr_yellow = ent_hp_secr_yellow[318:333]
        ent_hp_secr_yellow = re.findall("\d+", ent_hp_secr_yellow)[0]
        return ent_hp_secr_yellow
    except:
        pass
hp_secr_yellow()

def kyocera_max():
    try:
        ip_kyocera_max = '192.168.10.159'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_kyocera_max = cmdgen.UdpTransportTarget((ip_kyocera_max, 161))
        real_fun = getattr(generator, 'getCmd')
        res_kyocera_max = real_fun(comm_data, transport_kyocera_max, value)
        ent_kyocera_max = str(res_kyocera_max)
        ent_kyocera_max = ent_kyocera_max[318:333]
        ent_kyocera_max = re.findall("\d+", ent_kyocera_max)[0]
        ent_kyocera_max = int(ent_kyocera_max)
        per_ent_kyocera_max = (ent_kyocera_max * 100 // 7200)
        return per_ent_kyocera_max
    except:
        per_ent_kyocera_max = "🗙"
        return per_ent_kyocera_max
kyocera_max()

def hp_darin():
    try:
        ip_hp_darin = '192.168.10.157'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_darin = cmdgen.UdpTransportTarget((ip_hp_darin, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_darin = real_fun(comm_data, transport_hp_darin, value)
        ent_hp_darin = str(res_hp_darin)
        ent_hp_darin = ent_hp_darin[318:333]
        ent_hp_darin = re.findall("\d+", ent_hp_darin)[0]
        return ent_hp_darin
    except:
        ent_hp_darin = "🗙"
        return ent_hp_darin
hp_darin()

def kyocera_black():
    try:
        ip_kyocera_black = '192.168.1.160'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,4)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_kyocera_black = cmdgen.UdpTransportTarget((ip_kyocera_black, 161))
        real_fun = getattr(generator, 'getCmd')
        res_kyocera_black = real_fun(comm_data, transport_kyocera_black, value)
        ent_kyocera_black = str(res_kyocera_black)
        ent_kyocera_black = ent_kyocera_black[318:333]
        ent_kyocera_black = re.findall("\d+", ent_kyocera_black)[0]
        ent_kyocera_black = int(ent_kyocera_black)
        per_ent_kyocera_black = (ent_kyocera_black * 100 // 1200)
        return per_ent_kyocera_black
    except:
        per_ent_kyocera_black = "🗙"
        return per_ent_kyocera_black
kyocera_black()

def kyocera_cyan():
    try:
        ip_kyocera_cyan = '192.168.1.160'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,3)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_kyocera_cyan = cmdgen.UdpTransportTarget((ip_kyocera_cyan, 161))
        real_fun = getattr(generator, 'getCmd')
        res_kyocera_cyan = real_fun(comm_data, transport_kyocera_cyan, value)
        ent_kyocera_cyan = str(res_kyocera_cyan)
        ent_kyocera_cyan = ent_kyocera_cyan[318:333]
        ent_kyocera_cyan = re.findall("\d+", ent_kyocera_cyan)[0]
        ent_kyocera_cyan = int(ent_kyocera_cyan)
        per_ent_kyocera_cyan = (ent_kyocera_cyan * 100 // 1200)
        return per_ent_kyocera_cyan
    except:
        pass
kyocera_cyan()

def kyocera_mageneta():
    try:
        ip_kyocera_mageneta = '192.168.1.160'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,2)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_kyocera_mageneta = cmdgen.UdpTransportTarget((ip_kyocera_mageneta, 161))
        real_fun = getattr(generator, 'getCmd')
        res_kyocera_mageneta = real_fun(comm_data, transport_kyocera_mageneta, value)
        ent_kyocera_mageneta = str(res_kyocera_mageneta)
        ent_kyocera_mageneta = ent_kyocera_mageneta[318:333]
        ent_kyocera_mageneta = re.findall("\d+", ent_kyocera_mageneta)[0]
        ent_kyocera_mageneta = int(ent_kyocera_mageneta)
        per_ent_kyocera_mageneta = (ent_kyocera_mageneta * 100 // 1200)
        return per_ent_kyocera_mageneta
    except:
        pass
kyocera_mageneta()

def kyocera_yellow():
    try:
        ip_kyocera_yellow = '192.168.1.160'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_kyocera_yellow = cmdgen.UdpTransportTarget((ip_kyocera_yellow, 161))
        real_fun = getattr(generator, 'getCmd')
        res_kyocera_yellow = real_fun(comm_data, transport_kyocera_yellow, value)
        ent_kyocera_yellow = str(res_kyocera_yellow)
        ent_kyocera_yellow = ent_kyocera_yellow[318:333]
        ent_kyocera_yellow = re.findall("\d+", ent_kyocera_yellow)[0]
        ent_kyocera_yellow = int(ent_kyocera_yellow)
        per_ent_kyocera_yellow = (ent_kyocera_yellow * 100 // 1200)
        return per_ent_kyocera_yellow
    except:
        pass
kyocera_yellow()

def hp_svc():
    try:
        ip_hp_svc = '192.168.10.173'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_svc = cmdgen.UdpTransportTarget((ip_hp_svc, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_svc = real_fun(comm_data, transport_hp_svc, value)
        ent_hp_svc = str(res_hp_svc)
        ent_hp_svc = ent_hp_svc[318:333]
        ent_hp_svc = re.findall("\d+", ent_hp_svc)[0]
        return ent_hp_svc
    except:
        ent_hp_svc = "🗙"
        return ent_hp_svc
hp_svc()

def hp_director_black():
    try:
        ip_hp_director_black = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,1)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_director_black = cmdgen.UdpTransportTarget((ip_hp_director_black, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_director_black = real_fun(comm_data, transport_hp_director_black, value)
        ent_hp_director_black = str(res_hp_director_black)
        ent_hp_director_black = ent_hp_director_black[318:333]
        ent_hp_director_black = re.findall("\d+", ent_hp_director_black)[0]
        return ent_hp_director_black
    except:
        ent_hp_director_black = "🗙"
        return ent_hp_director_black
hp_director_black()

def hp_director_cyan():
    try:
        ip_hp_director_cyan = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,2)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_director_cyan = cmdgen.UdpTransportTarget((ip_hp_director_cyan, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_director_cyan = real_fun(comm_data, transport_hp_director_cyan, value)
        ent_hp_director_cyan = str(res_hp_director_cyan)
        ent_hp_director_cyan = ent_hp_director_cyan[318:333]
        ent_hp_director_cyan = re.findall("\d+", ent_hp_director_cyan)[0]
        return ent_hp_director_cyan
    except:
        pass
hp_director_cyan()

def hp_director_mageneta():
    try:
        ip_hp_director_mageneta = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,3)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_director_mageneta = cmdgen.UdpTransportTarget((ip_hp_director_mageneta, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_director_mageneta = real_fun(comm_data, transport_hp_director_mageneta, value)
        ent_hp_director_mageneta = str(res_hp_director_mageneta)
        ent_hp_director_mageneta = ent_hp_director_mageneta[318:333]
        ent_hp_director_mageneta = re.findall("\d+", ent_hp_director_mageneta)[0]
        return ent_hp_director_mageneta
    except:
        pass
hp_director_mageneta()

def hp_director_yellow():
    try:
        ip_hp_director_yellow = '192.168.10.164'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,4)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_hp_director_yellow = cmdgen.UdpTransportTarget((ip_hp_director_yellow, 161))
        real_fun = getattr(generator, 'getCmd')
        res_hp_director_yellow = real_fun(comm_data, transport_hp_director_yellow, value)
        ent_hp_director_yellow = str(res_hp_director_yellow)
        ent_hp_director_yellow = ent_hp_director_yellow[318:333]
        ent_hp_director_yellow = re.findall("\d+", ent_hp_director_yellow)[0]
        return ent_hp_director_yellow
    except:
        pass
hp_director_yellow()

def brother():
    try:
        ip_brother = '192.168.10.160'
        community = 'public'
        value = (1,3,6,1,2,1,43,11,1,1,9,1,2)
        generator = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('server', community, 1)
        transport_brother = cmdgen.UdpTransportTarget((ip_brother, 161))
        real_fun = getattr(generator, 'getCmd')
        res_brother = real_fun(comm_data, transport_brother, value)
        ent_brother = str(res_brother)
        ent_brother = ent_brother[318:333]
        ent_brother = re.findall("\d+", ent_brother)[0]
        ent_brother = int(ent_brother)
        per_ent_brother = (ent_brother * 100 // 12000)
        return per_ent_brother
    except:
        per_ent_brother = "🗙"
        return per_ent_brother
brother()
