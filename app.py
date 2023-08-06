import cv2
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from drone import *
from serialcomm import *
def app():

    

    def single_cam(camselect):
            cap = cv2.VideoCapture(0)  #select ip camera from string
            window_name = 'Camera '+str(camselect)
            cv2.namedWindow(window_name)
            while True:
                if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                    break
                ret, frame = cap.read()
                if not ret:
                    break
                cv2.imshow(window_name, frame)
                if cv2.waitKey(1) == ord('d'):
                    cap.release()
                    break
            cap.release()
            cv2.destroyAllWindows()

    def cam1():
        camselect = 0
       # camselect='rtsp://admin:isdr@432@192.168.50.252:554/PSIA/streaming/channels/102'
        single_cam(1)
    def cam2():
        camselect = 0
        #camselect='rtsp://admin:isdr@431@192.168.51.213:554/PSIA/streaming/channels/102'
        single_cam(2)
    def cam3():
        camselect = 0
        #camselect='rtsp://admin:isdr@433@192.168.50.131:554/PSIA/streaming/channels/102'
        single_cam(3)
    def cam4():
        camselect = 0
        #camselect='rtsp://admin:isdr@430@192.168.50.180:558/PSIA/streaming/channels/102'
        single_cam(4)


    def show_webcam():
            cap = cv2.VideoCapture(0)
            window_name = 'Webcam'
            cv2.namedWindow(window_name)
            while True:
                if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                    break
                ret, frame = cap.read()
                if not ret:
                    break
                h_concat_frame = np.concatenate((frame, frame), axis=1)
                concat_frame = np.concatenate((h_concat_frame, h_concat_frame), axis=0)
                window_size = cv2.getWindowImageRect(window_name)[2:]
                resized_frame = cv2.resize(concat_frame, window_size)
                cv2.imshow(window_name, resized_frame)
                if cv2.waitKey(1) == ord('d'):
                    cap.release()
                    break
            cap.release()
            cv2.destroyAllWindows()


    root = Tk()
    root.title('App')
    root.geometry('850x500')
    root.configure(bg='#fff')
    root.resizable(False,False)


    button_1 = Button(root, text='Camera 1',width=20,pady=5,bg='#57a1f8',fg='White',border=0,font= ('Microsoft YaHei UI Light', 10, 'bold'),command=cam1).place(x=218.75,y=20)
    button_2 = Button(root, text='Camera 2',width=20,pady=5,bg='#57a1f8',fg='White',border=0,font= ('Microsoft YaHei UI Light', 10, 'bold'),command=cam2).place(x=438.75,y=20)
    button_3 = Button(root, text='Camera 3',width=20,pady=5,bg='#57a1f8',fg='White',border=0,font= ('Microsoft YaHei UI Light', 10, 'bold'),command=cam3).place(x=218.75,y=70)
    button_4 = Button(root, text='Camera 4',width=20,pady=5,bg='#57a1f8',fg='White',border=0,font= ('Microsoft YaHei UI Light', 10, 'bold'),command=cam4).place(x=438.75,y=70)


   # button_all = Button(root, text='View all',width=50,pady=5,bg='#57a1f8',fg='White',border=0,font= ('Microsoft YaHei     UILight', 10,'bold'),command=show_webcam).place(x=218.75,y=120)
    button_auto = Button(root, text='Enter Automatic mode',width=50,pady=5,bg='#57a1f8',fg='White',border=0,font=  ('Microsoft YaHeiUI  Light', 10,'bold'),command=serialcom).place(x=218.75,y=200)
    root.mainloop()






