import sys

from PyQt5 import QtCore, QtWebSockets, QtNetwork
from PyQt5.QtCore import QUrl, QCoreApplication, QTimer
from PyQt5.QtWidgets import QApplication
import json


class Client(QtCore.QObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.client =  QtWebSockets.QWebSocket("",QtWebSockets.QWebSocketProtocol.Version13,None)
        
    ###
        
        self.client.textMessageReceived.connect(self.processTextMessage)

        # self.client.textFrameReceived.connect(self.processTextFrame)

        # # self.client.binaryMessageReceived.connect(self.processBinaryMessage)
        # self.client.disconnected.connect(self.socketDisconnected)

    ###

        self.client.error.connect(self.error)

        self.client.open(QUrl("ws://127.0.0.1:1302"))
        self.client.pong.connect(self.onPong)

    def processTextMessage(self, message):
        print("processTextMessage - message: {}".format(message))

    def do_ping(self):
        print("client: do_ping")
        self.client.ping(b"foo")

    def send_message(self):
        print("client: send_message")
        self.client.sendTextMessage(json.dumps({"request" : 1}))

    def onPong(self, elapsedTime, payload):
        print("onPong - time: {} ; payload: {}".format(elapsedTime, payload))

    def error(self, error_code):
        print("error code: {}".format(error_code))
        print(self.client.errorString())

    def close(self):
        self.client.close()

def quit_app():
    print("timer timeout - exiting")
    QCoreApplication.quit()

def ping():
    client.do_ping()

def send_message():
    client.send_message()

if __name__ == '__main__':
    global client
    app = QApplication(sys.argv)

    timer = QTimer()
    timer.timeout.connect(ping)
    timer.setInterval(1000)
    timer.start()
    
    timer2 = QTimer()
    timer2.timeout.connect(send_message)
    timer2.setInterval(1000)
    timer2.start()

    # timer2 = QTimer
    # timer2.singleShot(3000, send_message)

    QTimer.singleShot(12000, quit_app)

    client = Client()

    app.exec_()