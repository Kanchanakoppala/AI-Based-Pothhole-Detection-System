from ultralytics import YOLO
import cv2, os
class PotholeDetector:
    def __init__(self, model_path='best.pt', conf=0.4):
        if not os.path.exists(model_path):
            raise FileNotFoundError('Place best.pt in project root directory.')
        self.model=YOLO(model_path); self.conf=conf
    def detect_image(self,path):
        img=cv2.imread(path); results=self.model(img,conf=self.conf)[0]; data=[]
        for b in results.boxes:
            x1,y1,x2,y2=map(int,b.xyxy[0]); c=float(b.conf[0])
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img,f'{c:.2f}',(x1,y1-5),0,0.5,(0,255,0),2)
            data.append({'confidence':c,'area':(x2-x1)*(y2-y1)})
        return img,data
    def detect_video(self,path):
        cap=cv2.VideoCapture(path)
        out='output.mp4'; fourcc=cv2.VideoWriter_fourcc(*'mp4v')
        w,h=int(cap.get(3)),int(cap.get(4)); writer=cv2.VideoWriter(out,fourcc,20,(w,h)); all=[]
        while True:
            r,f=cap.read()
            if not r: break
            res=self.model(f,conf=self.conf)[0]
            for b in res.boxes:
                x1,y1,x2,y2=map(int,b.xyxy[0]); c=float(b.conf[0])
                cv2.rectangle(f,(x1,y1),(x2,y2),(0,255,0),2)
                all.append({'confidence':c,'area':(x2-x1)*(y2-y1)})
            writer.write(f)
        cap.release(); writer.release(); return out,all
