# blur detection script...

import cv2
from tqdm import trange


cap = cv2.VideoCapture('D:/video_quality_assessment/video_references/TEST_CASE_FOR_CONTRAST_BRIGHTNESS_AND_DYNAMIC_RANGE/pol-3008-lat-28.7030953lon-77.2699271dt-03-23-23ti-08-43-28.mp4')
f = open('D:/video_quality_assessment/scripts/blockingdetection/results.txt', 'w')

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cv2.CAP_PROP_FRAME_COUNT)
sum = 0.0
count = 0

for i in trange(frame_count, unit=' frames', leave=False, dynamic_ncols=True, desc='Calculating blur ratio'):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgray = cv2.resize(gray, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("Output", imgray)
    print(cv2.Laplacian(gray, cv2.CV_64F))
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Sample quality bar. Parameters adjusted manually to fit horizontal image size
    cv2.rectangle(frame, (0, 1080), (int(fm*1.6), 1040), (0,0,255), thickness=cv2.FILLED)

    #im = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    #cv2.imshow("Output", im)
    print("\nfm: ",fm,"\n")
    f.write(str(fm)+'\r')
    sum += fm
    count+=1 

    k = cv2.waitKey(160) & 0xff # 0xff to only consider the last 8 bytes of the 
    if k == 27:
        break 
avg = sum /count
f.write("average fm: "+'\r')
f.write(str(avg)+'\r')