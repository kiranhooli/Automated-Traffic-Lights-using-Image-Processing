import cv2
import numpy as np
import vehicles
import time
def counter(videos,road):
    count=0
    url = videos
    road = str(road)
    cap=cv2.VideoCapture(url)


    # for real time capture
    # cap = cv2.VideoCapture(0)

    #Get width and height of video

    w=cap.get(3)
    h=cap.get(4)
    frameArea=h*w
    areaTH=frameArea/400

    #Lines
    start_line=int(2*(h/5))
    end_line=int(3*(h/5))
    end_limit=int(4*(h/5))

    line_color=(255,0,0)
    pt1 =  [0, end_line]
    pt2 =  [w, end_line]
    pts_L1 = np.array([pt1,pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1,1,2))

    pt3 =  [0, end_limit]
    pt4 =  [w, end_limit]
    pts_L2 = np.array([pt3,pt4], np.int32)
    pts_L2 = pts_L2.reshape((-1,1,2))

    #Background Subtractor
    fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)

    #Kernals
    kernalOp = np.ones((3,3),np.uint8)
    kernalOp2 = np.ones((5,5),np.uint8)
    kernalCl = np.ones((11,11),np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cars = []
    max_p_age = 5
    pid = 1

    while(cap.isOpened()):
        ret,frame=cap.read()
        for i in cars:
            i.age_one()
        fgmask=fgbg.apply(frame)
        fgmask2=fgbg.apply(frame)

        if ret==True:

            #Binarization
            ret,imBin=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
            ret,imBin2=cv2.threshold(fgmask2,200,255,cv2.THRESH_BINARY)
            
            #Opening i.e First Erode then dilate to remove background noise
            mask=cv2.morphologyEx(imBin,cv2.MORPH_OPEN,kernalOp)
            mask2=cv2.morphologyEx(imBin2,cv2.MORPH_OPEN,kernalOp)

            #Closing i.e First Dilate then Erode to remove foreground noise
            mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernalCl)
            mask2=cv2.morphologyEx(mask2,cv2.MORPH_CLOSE,kernalCl)

            #Find Contours
            _, countours0,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            for cnt in countours0:
                area=cv2.contourArea(cnt)
                if area>areaTH:
                    ####Tracking######
                    m=cv2.moments(cnt)
                    cx=int(m['m10']/m['m00'])
                    cy=int(m['m01']/m['m00'])
                    x,y,w,h=cv2.boundingRect(cnt)

                    new=True
                    if cy in range(end_limit):
                        for i in cars:
                            if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                                new = False
                                i.updateCoords(cx, cy)

                                if i.going_DOWN(end_line,start_line)==True:
                                    count+=1
                                    print("Vehicle : ", (count), ' crossed at', time.strftime("%c"))
                                break
                            if i.getState()=='1':
                                if i.getDir()=='move'and i.getY()>end_limit:
                                    i.setDone()
                            if i.timedOut():
                                index=cars.index(i)
                                cars.pop(index)
                                del i

                        if new==True: #If nothing is detected,create new
                            p=vehicles.Car(pid,cx,cy,max_p_age)
                            cars.append(p)
                            pid+=1

                    cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
                    img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            for i in cars:
                cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

            disp_text='Count : '+str(count)
            frame=cv2.polylines(frame,[pts_L1],False,line_color,thickness=2)
            frame=cv2.polylines(frame,[pts_L2],False,(255,255,255),thickness=1)
            cv2.putText(frame, road, (10, 20), font, 0.5, (0,0,0), 2, cv2.LINE_AA)
            cv2.putText(frame, road, (10, 20), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(frame, disp_text, (10, 40), font, 0.7, (0,0,0), 2, cv2.LINE_AA)
            cv2.putText(frame, disp_text, (10, 40), font, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('Frame',frame)

            if cv2.waitKey(1)&0xff==ord('q'):
                return count
        else:
            return count

    cap.release()
    cv2.destroyAllWindows()








