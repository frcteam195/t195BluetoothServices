from frcteam195.database import Users, Config, MatchScouting, Teams, Words, WordCloud, connect, TimeCode, MatchScoutingL2, Matches
from bluetooth import *
from _thread import *
import threading
import datetime
import logging
import sys
import json
import time


logging.basicConfig(level=logging.INFO)
print_lock = threading.Lock()
skip_msg = "{'result': 'skip'}"


def send_reply(client_sock, msg):
    msg_size = len(msg)
    bytes_sent = 0
    bytes_to_send = msg
    while bytes_sent < msg_size:
        bytes_sent += client_sock.send(bytes_to_send)
        time.sleep(.5)
        bytes_to_send = bytes_to_send[bytes_sent-1:]
    client_sock.send(b'\x03')


def threaded(client_sock):
    ret_string = "{{'result': '{0}', 'payload':{1}, 'hash': '{2}'}}"
    result = 'success'
    while True:
        try:
            data = None
            while True:
                new_data = client_sock.recv(2048)
                if len(new_data) == 0: break
                data += new_data
            if data is None:
                logging.debug(str(datetime.datetime.now()) + " empty message received!")
                print_lock.release()
                break
            elif data == b'\x03':
                logging.debug(str(datetime.datetime.now()) + " ETX character found!")
                print_lock.release()
                break

            logging.debug(str(datetime.datetime.now()) + " received [%s]" % data)
            jsonstr = json.loads(data)
            last_hash = 195
            if 'last_hash' in jsonstr:
                last_hash = jsonstr['last_hash']
            logging.info(str(datetime.datetime.now()) + " " + jsonstr['cmd'])
            if jsonstr['cmd'] == "get-config":
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                if 'payload' in jsonstr:
                    payload = jsonstr['payload']
                    computerName = payload['computerName']
                config = json.dumps(Config.get(computerName))
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    ret_bytes = ret_string.format(result, config, this_hash).encode()
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-users':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                users = json.dumps(Users.get())
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    ret_bytes = ret_string.format(result, users, this_hash).encode()
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-matches':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                if 'payload' in jsonstr:
                    payload = jsonstr['payload']
                    eventId = payload['eventId']
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    matches = json.dumps(MatchScouting.get(eventId))
                    logging.info(str(datetime.datetime.now()) + " Size of matches is {}".format(len(matches)))
                    ret_bytes = ret_string.format(result, matches, this_hash).encode()
                logging.info(str(datetime.datetime.now()) + " Size of matches return string is {}".format(len(ret_bytes)))
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-matches-l2':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                if 'payload' in jsonstr:
                    payload = jsonstr['payload']
                    eventId = payload['eventId']
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    matches = json.dumps(MatchScoutingL2.get(eventId))
                    logging.info(str(datetime.datetime.now()) + " Size of matches is {}".format(len(matches)))
                    ret_bytes = ret_string.format(result, matches, this_hash).encode()
                logging.info(str(datetime.datetime.now()) + " Size of matches return string is {}".format(len(ret_bytes)))
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-matches-all':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    matches = json.dumps(Matches.get())
                    logging.info(str(datetime.datetime.now()) + " Size of matches is {}".format(len(matches)))
                    ret_bytes = ret_string.format(result, matches, this_hash).encode()
                logging.info(str(datetime.datetime.now()) + " Size of matches return string is {}".format(len(ret_bytes)))
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-teams':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                teams = json.dumps(Teams.get())
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    ret_bytes = ret_string.format(result, teams, this_hash).encode()
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-words':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                words = json.dumps(Words.get())
                ret_bytes = ret_string.format(result, words, "").encode()
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-word-cloud':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                wordcloud = json.dumps(WordCloud.get())
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    ret_bytes = ret_string.format(result, wordcloud, this_hash).encode()
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'put-match-scouting':
                logging.info(str(datetime.datetime.now()) + " Received put-match-scouting request {0}".format(jsonstr['cmd']))
                ret = 'failure'
                if 'key' in jsonstr:
                    key = jsonstr['key']
                    if 'payload' in jsonstr:
                        payload = jsonstr['payload']
                        ret = MatchScouting.put(key, payload)
                ret_string = ret_string.format(ret, 0, "").encode()
                send_reply(client_sock, ret_string)
            elif jsonstr['cmd'] == 'put-teams':
                logging.info(str(datetime.datetime.now()) + " Received put-teams request {0}".format(jsonstr['cmd']))
                if 'key' in jsonstr:
                    key = jsonstr['key']
                    if 'payload' in jsonstr:
                        payload = jsonstr['payload']
                        ret = Teams.put(key, payload)
                ret_string = ret_string.format(ret, 0, "").encode()
                send_reply(client_sock, ret_string)
            elif jsonstr['cmd'] == 'put-word-cloud':
                logging.info(str(datetime.datetime.now()) + " Received put-teams request {0}".format(jsonstr['cmd']))
                if 'payload' in jsonstr:
                    payload = jsonstr['payload']
                    ret = WordCloud.put(payload)
                ret_string = ret_string.format(ret, 0, "").encode()
                send_reply(client_sock, ret_string)
            else:
                send_reply(client_sock, ret_string.format("failure", "", 0).encode())
                logging.error(str(datetime.datetime.now()) + " Unrecognized request {0}".format(jsonstr['cmd']))
            logging.info(str(datetime.datetime.now()) + " Releasing lock.")
            print_lock.release()
            break;
        except IOError as ioe:
            logging.error(str(datetime.datetime.now()) + " Error: {0}".format(ioe))
        except Exception as ee:
            logging.error(str(datetime.datetime.now()) + " Error: {0}".format(ee))
        except:
            logging.error(str(datetime.datetime.now()) + " Unknown exception occurred!")
        finally:
            client_sock.close()
            if print_lock.locked():
                print_lock.release()
            break


def Main():

    conn = connect()
    if conn == None:
        logging.fatal(str(datetime.datetime.now()) + " Unable to connect to database -- exiting.")
        return
    conn.close()

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
        logging.debug(str(datetime.datetime.now()) + " Waiting for connection on RFCOMM channel {}".format(port))


        try:
            client_sock, client_info = server_sock.accept()
            logging.debug(str(datetime.datetime.now()) + " Accepted connection from " + str(client_info))
            print_lock.acquire()
            logging.debug(str(datetime.datetime.now()) + " Starting command handling")
            start_new_thread(threaded, (client_sock,))
            logging.debug(str(datetime.datetime.now()) + " Command handling done")
        except:
            logging.error("Unexpected error: %s".format(sys.exc_info()[0]))
            continue
    server_sock.close()


if __name__ == '__main__':
    Main()
