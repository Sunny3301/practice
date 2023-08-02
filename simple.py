# blur detection script...

import cv2
from tqdm import trange


cap = cv2.VideoCapture('D:/video_quality_assessment/video_references/TEST_CASE_FOR_ABNORMAL_FRAME_RATE/pol-3363-lat-25.4552254lon-78.5368408dt-05-04-23ti-18-19-23.mp4')
f = open('D:/video_quality_assessment/scripts/blurDetection/try2/results.txt', 'w')

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
##### for canny ###
#kernel_size = 3
#low_threshold = 1
#ratio = 3
print("fps: ", cap.get(cv2.CAP_PROP_FPS))

for i in trange(frame_count, unit=' frames', leave=False, dynamic_ncols=True, desc='Calculating blur ratio'):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    ##### for canny #
    #fm = cv2.Canny(gray, low_threshold ,  low_threshold*ratio, kernel_size).var()

    # Sample quality bar. Parameters adjusted manually to fit horizontal image size
    cv2.rectangle(frame, (0, 1080), (int(fm*1.6), 1040), (0,0,255), thickness=cv2.FILLED)

    im = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("Output", im)
    print("fm: ",fm,"\n")
    f.write(str(fm)+'\r')

    k = cv2.waitKey(5) & 0xff # 0xff to only consider the last 8 bytes of the 
    if k == 27:
        break 

'''
**********************
RESULTS
**********************
// since the vehicles are always moving instead of using the threshold of 100 use 180 
// this is due to even if we take one frame 

pol-3725-lat-25.4638907lon-78.5608518dt-05-03-23ti-10-04-28.mp4 // wobbly video
average fm: 
187.0839516561326

pol-28-lat-28.6291903lon-77.2375933dt-05-04-23ti-06-28-15  // very blur dashcam video
average fm: 
307.32171827323486

pol-10-lat-28.510666lon-77.1810068dt-03-22-23ti-11-51-30  // the elevator wobble
'''