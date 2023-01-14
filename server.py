import socket
import logging

logging.basicConfig(filename="server.log", level=logging.INFO)


def set_host():
    while True:
        print('Type HOST below or write "def" for default HOST')
        try:
            msg = input()
            if msg == "def":
                host = '127.0.0.1'
            else:
                host = msg
            break
        except:
            print('You enter not supported HOST, please try again')
    return host


def set_port():
    while True:
        print('Type PORT below or write "def" for default PORT')
        try:
            msg = input()
            if msg == "def":
                port = 9090
                break
            elif type(msg) is not int:
                print('You enter not supported PORT, please try again')
            else:
                port = msg
                break
        except:
            print('You enter not supported PORT, please try again')
    return port


def message_handler(conn, addr):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break



            data = "You do not have access to use this server"
            send_message(data)
            conn.close()
            log = 'Last user do not enter a right login or password'
            logging.info(log)
            print(log)
            break

        except Exception as ex:
            log = 'An error in receiving messages was occurred by exception: %s' % ex
            logging.error(log)
            print(log)
        else:
            send_message(data)


def send_message(data):
    try:
        conn.send(data.encode())
        log = "Last message was send back to client successfully"
        logging.info(log)
        print(log)
    except Exception as ex:
        log = 'An error in sending message was occurred by exception: %s' % ex
        logging.error(log)
        print(log)


HOST = set_host()
PORT = set_port()

log = "Server started with HOST: %s and PORT: %s" % (HOST, PORT)
logging.info(log)
print(log)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        sock.bind((HOST, PORT))
    except:
        log = 'Unable to connect to %s PORT. Trying to connect to %s PORT' % (PORT, PORT+1)
        logging.error(log)
        print(log)
        PORT = PORT + 1
    else:
        break

while True:
    log = 'Listening %s port...' % PORT
    logging.info(log)
    print(log)

    sock.listen(1)
    conn, addr = sock.accept()
    message_handler(conn, addr)

    conn.close()