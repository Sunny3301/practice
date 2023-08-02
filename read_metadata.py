 # purpose of this file is to be used as module to be imported in the execution file and not a executable script itself...
 # **************
 # importing the used libraries
import json 

 # giving the file path and storing it in json_file_path variable 
json_file_path = "D:/video quality assessment/video references/pol-3442-lat-25.4609651lon-78.5743676dt-05-03-23ti-12-09-23.json"
with open( json_file_path , 'r') as file:
    data = json.load(file)
     #to see the whole json file in proper indented form use the following code...
    #print(json.dump(data , indent = 2))


class fetch():
    def __init__(self):
        self.data = 0
        print()

 # this function return the average of the pitch values stored in the json file (one pitch value for everytime stamp) 
 # main focus of this function is to tell is the phone is tilted or not while recording is taking place... 
 # pitch is the angle between a plane parallel to the device's screen and a plane parallel to the ground.
 # 0 means completely parallel to the ground and 1 means perpendicular to the gound...
 # and any value in between conresponds to a angle, calculating which i havent worked on yet
 # one flaw with the sensor data is that it cannot collect pitch value for every timestamp so by default stores the value 0.0
 # since this function returns the avgerage 0.0 value decreases the overall value of average below acceptable limit
 # hence a better approach would be to remove the 0.0 values while taking average
def get_pitch(self):
    sum = 0
    count = 0
    sensor_string =  self.data['3']['format']['tags']['sensorData']['value']
     # eval() convert the data to string type 
    sensor_string = eval(sensor_string)
    for elem in sensor_string:
         #this line prints all the timestamps and there respective pitch values 
        #print(elem['timeStamp'],"   ", elem['pitch'])
        sum += elem['pitch']
        count +=1
    avg = sum/count
    return avg
        
 # function get_chroma_location() returns the value of the chroma_location variable in json file (either a left or a right)
 # this function might help in the figuring out where the main source of light is in a time frame/whole video 
 # main goal is to make it easy to implemeent chromatic/ brightness balancing/ corrections in a video
def get_chroma_location():
     # **streams is messed up,the whole thing is list but stores information as dictionary
    sensor_string = data['3']['streams']   
    return(sensor_string[0].get('chroma_location').get('value'))

 # function get_framerate() returns framerate of the whole video (most suitable one being 30fps)
 # if the framerate is below 24 frames per seconf the video is precieved as choppy and the detail can be lost 
 # so this function's main role is to help prioritize the videos with a high frame rate than those which dont...
def get_framerate():
    sensor_string = data['1']['VideoFrameRate']
    return(sensor_string['value'])

 # function get_bitrate() returns the bitrate value, that is the amount of information stored per second of the video...
 # helps us figure out which video has the right amount of details and information stored even before we play the video
def get_bitrate():
    sensor_string = data['3']['format']['bit_rate']
    return(sensor_string['value'])

 #function get_resolution() returns the resolution (number of pixels in each frame of the vidoe) of the video (height x width)
 # ideal resolution is 1620 x 1080 
 # main goal is to eliminate videos with improper resolution 
def get_resolution():
    sensor_string = data['1']['ImageSize']
    return(sensor_string['value'])

 # function get_bitdepth() returns the bitdepth(color range) of each frame of the video...
 # ideal bitdepth is 24-30, if less than this the video will not have enough contrast, mssing details in darker/ brighter areas of the frame
def get_bitdepth():
    sensor_string = data['1']['BitDepth']
    return(sensor_string['value'])

 # calling  for all the functions to test they are working properly...
 # print(get_bitdepth())
 # print(get_bitrate())
 # print(get_chroma_location())
 # print(get_framerate())
 # print(get_resolution())
 # print(get_pitch())