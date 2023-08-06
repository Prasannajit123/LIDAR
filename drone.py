from ultralytics import YOLO
import cv2
import cvzone
import math
import time
from gmail import*
# from roboflow import Roboflow
# rf = Roboflow(api_key="f1Ws9sCH12W5dEbGfVEk")
# project = rf.workspace().project("final_lids")
# model = project.version(1).model


#cap=cv2.VideoCapture('rtsp://admin:isdr@432@192.168.50.252:554/PSIA/streaming/channels/102')
#cap=cv2.VideoCapture('rtsp://admin:isdr@431@192.168.51.213:554/PSIA/streaming/channels/102')
#cap=cv2.VideoCapture('rtsp://admin:isdr@433@192.168.50.131:554/PSIA/streaming/channels/102')
#cap=cv2.VideoCapture('rtsp://admin:isdr@430@192.168.50.180:558/PSIA/streaming/channels/102')
def detector(dist,angle):
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    ptime=0
    wait=0
    detect=False
    model=YOLO('best.pt')

    mycolor=(0,0,255)

    classNames = ['drone']

    while(True):
        success,img=cap.read()
        results=model(img,stream=True)
        detect=False
        ntime=time.time()
        fps=int(1/(ntime-ptime))
        for r in results:
            boxes=r.boxes
            for box in boxes:
            #Bounding boxes
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                w,h=x2-x1,y2-y1

                #confidence
                conf=(math.ceil(box.conf[0]*100))/100
                conf=str(conf)
                #cvzone.cornerRect(img,(x1,y1,w,h))
                # cv2.putText(img,conf,(x1,y1-30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
                #Classes
                cls=int(box.cls[0])
                #cv2.putText(img,str(classNames[cls]),(x1,y1+30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
                currentclass=classNames[cls]
                #print(len(boxes))
                mycolor=(255,0,0)
                if(currentclass=='drone'):
                    wait=0
                    detect=True
                    cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (x1+10,y1-20), scale=1, thickness=1,colorT=(255,255,255),colorR=mycolor)
                    cv2.rectangle(img,(x1,y1),(x2,y2),mycolor,3)
                    

                else:
                    
                    print(wait)
                    detect=False
                
                
        
        if(detect==False):
            wait=wait+1
            print(wait)
      
        else:
            email_alert(dist,angle)
        #cv2.putText(img,str(fps),(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
        ptime=ntime
        if(angle>=0)&(angle<90):
            nm='Camera 1'
        else:
            nm='Camera 2'
        cv2.imshow(nm,img)        
        if(cv2.waitKey(10)&0xFF==ord('d'))|(wait>50):
         break



    cap.release()
    cv2.destroyAllWindows()

#detector(23,120)



