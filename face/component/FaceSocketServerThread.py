import os
import socket
import struct
from threading import Thread
from wx.lib.pubsub import pub
import xml.etree.ElementTree as ET


class FaceSocketServerThread(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.address = (host, port)
        self.start()

    def run(self):
        dataBuffer = bytes()
        headSize = 20
        tailSize = 4
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(self.address)
            s.listen(1)
            con, clientAddress = s.accept()
            with con:
                while True:
                    data = con.recv(1024)
                    if data:
                        dataBuffer += data
                        while True:
                            if len(dataBuffer) < headSize:
                                print(dataBuffer)
                                print("Data package（%s Byte）< header size" % len(dataBuffer))
                                break

                            # read header
                            headPack = struct.unpack('!LLLLL', dataBuffer[:headSize])
                            headFlag = headPack[0]
                            # it contains 3 column size
                            bodySize = headPack[1] - 12
                            protocol = headPack[2]
                            print("Header :", headFlag)
                            print("Protocol :", protocol)
                            print("Body size :", bodySize)
                            if len(dataBuffer) < headSize + bodySize:
                                print("Data package（%s Byte）out of %s Byte" % (len(dataBuffer), headSize + bodySize))
                                break

                            dataBody = dataBuffer[headSize:headSize + bodySize]
                            self.dataHandle(headPack, dataBody)

                            # process next data package
                            dataBuffer = dataBuffer[(headSize + bodySize + tailSize):]

    def dataHandle(self, headPack, dataBody):
        print("Body:", dataBody)
        dataRoot = ET.fromstring(dataBody)

        if dataRoot:
            blackTag = dataRoot.find('BlackList')
            realTag = dataRoot.find('RealList')
            confidenceTag = dataRoot.find('Confidence')
            timestampTag = dataRoot.find('CollectTime')
            blackData = blackTag.text
            realData = realTag.text
            # print("RealData:", realData)
            print("Confidence :", confidenceTag.text, "CollectTime :", timestampTag.text)
            pub.sendMessage('face.refresh', index='0', blackData=blackData, realData=realData)


if __name__ == '__main__':
    socketServer = FaceSocketServerThread('192.168.1.130', 6789)
