from frcteam195.database import Users, Config, MatchScouting, Teams, Words, WordCloud, connect, TimeCode, MatchScoutingL2, Matches
import socket
import threading
import socketserver
import datetime
import logging
import sys
import json
import time


logging.basicConfig(level=logging.INFO)
print_lock = threading.Lock()
skip_msg = "{'result': 'skip'}"

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        threaded(self.request)



def send_reply(client_sock, msg):
    msg += b'3'
    msg_size = len(msg)
    logging.debug("Message size is {}".format(msg_size))
    bytes_sent = 0
    bytes_to_send = msg
    while bytes_sent < msg_size:
        t_bytes_sent = client_sock.send(bytes_to_send)
        logging.debug("Bytes sent this chunk {}".format(t_bytes_sent))
        bytes_sent += t_bytes_sent
        logging.debug("Sent total of {} bytes so far...".format(bytes_sent))
        time.sleep(.5)
        bytes_to_send = msg[bytes_sent:]
        logging.debug("Bytes to send {}".format(len(bytes_to_send)))


def recv_timeout(the_socket,timeout=2):
    the_socket.setblocking(0)
    total_data=[];data=b'';begin=time.time()
    while 1:
        #if you got some data, then break after wait sec
        if total_data and time.time()-begin>timeout:
            break
        #if you got no data at all, wait a little longer
        elif time.time()-begin>timeout*2:
            break
        try:
            data=the_socket.recv(8192)
            if data:
                total_data.append(data)
                begin=time.time()
            else:
                time.sleep(0.1)
        except:
            pass
    return b''.join(total_data)


def threaded(client_sock):
    ret_string = "{{'result': '{0}', 'payload':{1}, 'hash': '{2}'}}"
    result = 'success'
    while True:
        try:
            data = recv_timeout(client_sock, 2)
            if data == b'\x03':
                logging.debug(str(datetime.datetime.now()) + " ETX character found!")
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
                    allianceStationId = None
                    if 'allianceStationId' in payload:
                        allianceStationId = payload['allianceStationId']
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    matches = json.dumps(MatchScouting.get(eventId, allianceStationId))
                    logging.info(str(datetime.datetime.now()) + " Size of matches is {}".format(len(matches)))
                    ret_bytes = ret_string.format(result, matches, this_hash).encode()
                logging.info(str(datetime.datetime.now()) + " Size of matches return string is {}".format(len(ret_bytes)))
                send_reply(client_sock, ret_bytes)
            elif jsonstr['cmd'] == 'get-match-teams':
                logging.info(str(datetime.datetime.now()) + " Sending response to {0}".format(jsonstr['cmd']))
                if 'payload' in jsonstr:
                    payload = jsonstr['payload']
                    matchId = payload['matchId']
                this_hash = TimeCode.get()
                if this_hash == last_hash:
                    ret_bytes = skip_msg.encode()
                else:
                    matches = json.dumps(Matches.get(matchId))
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
                logging.info(str(datetime.datetime.now()) + " Received put-word-cloud request {0}".format(jsonstr['cmd']))
                if 'payload' in jsonstr:
                    payload = jsonstr['payload']
                    ret = WordCloud.put(payload)
                ret_string = ret_string.format(ret, 0, "").encode()
                send_reply(client_sock, ret_string)
            else:
                send_reply(client_sock, ret_string.format("failure", "", 0).encode())
                logging.error(str(datetime.datetime.now()) + " Unrecognized request {0}".format(jsonstr['cmd']))
            logging.info(str(datetime.datetime.now()) + " Releasing lock.")
            break;
        except IOError as ioe:
            logging.error(str(datetime.datetime.now()) + " Error: {0}".format(ioe))
            send_reply(client_sock, ret_string)
        except Exception as ee:
            logging.error(str(datetime.datetime.now()) + " Error: {0}".format(ee))
            send_reply(client_sock, ret_string)
        except:
            logging.error(str(datetime.datetime.now()) + " Unknown exception occurred!")
            send_reply(client_sock, ret_string)
        finally:
            client_sock.close()
            if print_lock.locked():
                print_lock.release()
            break


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():

    conn = connect()
    if conn == None:
        logging.fatal(str(datetime.datetime.now()) + " Unable to connect to database -- exiting.")
        return
    conn.close()

    HOST, PORT = "0.0.0.0", 60195

    with ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler) as server:
        server.serve_forever()


if __name__ == '__main__':
    main()
