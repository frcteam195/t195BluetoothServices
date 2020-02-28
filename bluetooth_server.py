from frcteam195.database import Users, Config, MatchScouting
from bluetooth import *
from _thread import *
import threading
import datetime
import logging
import sys
import json


logging.basicConfig(level=logging.INFO)
print_lock = threading.Lock()


def threaded(client_sock):
    while True:
        try:
            data = client_sock.recv(1024)
            logging.info(str(datetime.datetime.now()) + " received [%s]" % data)
            if data == b'\x03':
                logging.info(str(datetime.datetime.now()) + " ETX character found!")
                print_lock.release()
                break

            jsonstr = json.loads(data)
            logging.info(str(datetime.datetime.now()) + " " + jsonstr['cmd'])
            if jsonstr['cmd'] == "get-config":
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                client_sock.send(b"{'result': 'success', 'payload':{'role': 'Red 1', 'event': 'Winter Nationals'}}")
            print_lock.release()
            break;
        except IOError as ioe:
            logging.error(str(datetime.datetime.now()) + " Error: {0}".format(ioe))
    client_sock.close()


def Main():
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "c3252081-b20b-46df-a9f8-1c3722eadbef"

    advertise_service( server_sock, "Team195ScoutingServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ],
                       #       protocols = [ OBEX_UUID ]
                       )

    while True:
        logging.info(str(datetime.datetime.now()) + " Waiting for connection on RFCOMM channel %d".format(port))


        try:
            client_sock, client_info = server_sock.accept()
            logging.info(str(datetime.datetime.now()) + " Accepted connection from " + str(client_info))
            print_lock.acquire()
            start_new_thread(threaded, (client_sock,))
        except:
            logging.error("Unexpected error: %s".format(sys.exc_info()[0]))
    server_sock.close()


if __name__ == '__main__':
    Main()
