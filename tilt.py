 # the purpose of this file it to read all the json files and create a object for the fetch clas in read_metadata
 # then passing the json files through to the fetch class in read_metadata...

import json 

 # the purpose of this activity is to check if the video quality is good or not 
 # one script starts the whole process, one script reads and makes a list of all the json files in a folder 
 # then one script reads each json files data and stores the different values required in its variables 
 # then subscripts that use each of these variables value to compute if the video is useable in different aspects....
 # main file will only invoke the json_lister file adn pass the folder path to the json_lister class
  # json lister will read all the json files in the given path and makes a list of em and then passes this json files one by one to the read_metadata file
     # in read metadata file the fetch class will store all the information of each of the parameter and it will invoke all the other parameter tester files...
 # main
 #   |--json_lister
 #           |---read_metadata
 #                    |-- tilt.py



 # this script takes pitch value of each and every time frame and gives it a score out of 0 to 10 where 
 # 10 being the best and 0 being the worst. Then the average of each timestamp's score-value it displayed.
 # good : pol-2785-lat-28.6356967lon-77.2202516dt-03-23-23ti-19-06-31
 # bad  : pol-3442-lat-25.4609651lon-78.5743676dt-05-03-23ti-12-09-23
 # output format : timestamp    pitch_value    score
 #*****************
 # importing the used libraries
import json 

 # map_value_to_score() maps the score of each pitch value to its timestamp 
 # ON A SCALE OF: 0(BEST) - 20(WORST) (INCREMENT OF 2)
 # ANGULAR SCALE:   90    - 80(O.1736)/100(-O.1736)
def map_value_to_score(value):
    min_value = 0.0
    max_value = 0.17365
    if abs(value) <= min_value:
        return 10
    elif abs(value) >= max_value:
        return 0
    else:
        return (round((abs(value) - min_value) / (max_value - min_value)*10 , 5))

 # this function return the average of the pitch values stored in the json file (one pitch value for everytime stamp) 
 # main focus of this function is to tell is the phone is tilted or not while recording is taking place... 
 # pitch is the angle between a plane parallel to the device's screen and a plane parallel to the ground.
 # 1 means completely parallel to the ground and 0 means perpendicular to the gound(since it is a cos function)...
 # and any value in between conresponds to a angle, calculating which i havent worked on yet
 # one flaw with the sensor data is that it cannot collect pitch value for every timestamp so by default stores the value 0.0 
 # since this function returns the avgerage 0.0 value decreases the overall value of average below acceptable limit so we skip 0.0 values
def get_pitch(data):
   sum = 0
   count = 0
   sensor_string =  data['3']['format']['tags']['sensorData']['value']
    # eval() convert the data to string type 
   sensor_string = eval(sensor_string)
   for elem in sensor_string:
        if elem['pitch'] != 0.0:
            score = map_value_to_score(elem['pitch'])
            #this line prints all the timestamps and there respective pitch values 
            print(elem['timeStamp'],"   ", elem['pitch'],"   ", score)
            sum += score
            count +=1
   return (round(sum/count , 5))


def main():
     # for now taken the path to one singular file...
     # later may write a seprate code script to read data form each file and print data of each video...
     # giving the file path and storing it in json_file_path variable 
     # D:/video_quality_assessment/video_references/ALL_VIDEOS_WITH_METADATA/temp_metadata.json
     # D:/video_quality_assessment/video_references/pol-2785-lat-28.6356967lon-77.2202516dt-03-23-23ti-19-06-31.json
    json_file_path = "D:/video_quality_assessment/video_references/ALL_VIDEOS_WITH_METADATA/temp_metadata.json"
    with open( json_file_path , 'r') as file:
        data = json.load(file)
         #to see the whole json file in proper indented form use the following code...
        #print(json.dumps(data , indent = 2))
    pitch_value = get_pitch(data)
    print("The average value of pitch is: ", pitch_value)

if __name__ == "__main__":
    main()