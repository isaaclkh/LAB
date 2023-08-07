import base64
import socket

def clientToServer(localIP, localPort):
    bufferSize = 50000

    # 데이터그램 소켓을 생성
    UDPServerSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # 주소와 IP로 Bind
    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    # 들어오는 데이터그램 Listen
    while (True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(type(message))
        print(message)
        print(clientMsg)
        print(clientIP)

        message = message.decode('utf-8')
        message = base64.b64decode(message)
        message = message.decode('utf-8')
        print(message)

        if message is not None:
            
            return message
