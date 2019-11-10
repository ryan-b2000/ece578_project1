import socket
import threading
import cv2
import struct
class client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.address = ('127.0.0.1', 4444)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(self.address)
        self.capture = cv2.VideoCapture(0)

    def send_img(self):
        try:
            while True:
                success, frame = self.capture.read()
                while not success and frame is None:
                    success, frame = self.capture.read()
                result, imgencode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                self.s.sendall(struct.pack('i', imgencode.shape[0]))
                self.s.sendall(imgencode)
        except Exception as e:
            print(e)
            self.s.sendall(struct.pack('c', 1))
            self.capture.release()
            self.close()

    def recv_data(self):
        while True:
            data_recv = self.s.recv(1024)
            print('>服务端：', data_recv.decode('gbk'))
            print(type(data_recv))

def main():
    t1 = client()
    thread_send = threading.Thread(target=t1.send_img)
    thread_recv = threading.Thread(target=t1.recv_data)
    thread_send.start()
    thread_recv.start()
    thread_send.join()
    thread_recv.join()
if __name__ == '__main__':
    main()