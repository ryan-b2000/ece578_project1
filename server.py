import socket
import struct
import cv2
import threading
import numpy
class sever(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建socket对象
        self.s.bind(('',2222))
        self.s.listen(128)
        self.newSocket, self.clientAddr = self.s.accept()
        print('now waiting for frames...')

    def recv_img(self):
        while True:
            data = self.newSocket.recv(65535)
            if len(data) == 1 and data[0] == 1:
                self.s.close()
                cv2.destroyAllWindows()
                exit()
            if len(data) != 4:
                length = 0
            else:
                length = struct.unpack('i', data)[0]
            data = self.newSocket.recv(65535)
            if length != len(data):
                continue
            data = numpy.array(bytearray(data))
            imgdecode = cv2.imdecode(data, 1)
            imgdecode = cv2.bilateralFilter(imgdecode, 5, 50, 100)
            imgdecode = cv2.flip(imgdecode, 1)
            cv2.rectangle(imgdecode, (int(0.5 * imgdecode.shape[1]), 0),
                          (imgdecode.shape[1], int(0.8 * imgdecode.shape[0])), (255, 0, 0), 2)
            cv2.imshow('frames', imgdecode)
            if cv2.waitKey(1) == 27:
                break

    def send_data(self, data):

        msg = data
        self.newSocket.send(msg.encode('utf-8'))


def main():
    t2 = sever()
    thread_rece = threading.Thread(target=t2.recv_img)
    thread_rece.start()
    thread_send = threading.Thread(target=t2.send_data('ada'))
    thread_send.start()
    thread_rece.join()
    thread_send.join()
if __name__ == '__main__':
    main()
