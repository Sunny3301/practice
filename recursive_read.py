import os
import math as m
import json

def linear(value , min , max):
    if (value == min):
        return 0
    elif (value == max):
        return 10
    else:
        return (round(abs(value - min) / abs(max - min)*10 , 5))

def map_value_to_score(value):

    #print(m.acos(value))
    new_value = m.acos(value) * (180.0 / m.pi) # to get the result in degrees and not in radians 
    #print(new_value , "   ", type(new_value))
    if (new_value> 100 or new_value <80):
        return(-1)
    elif (new_value<90):
        return(linear(new_value , 80 , 90))
    elif(new_value>90):
        return(linear(new_value , 100 , 90))

    
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
            if score != -1:
                print(elem['timeStamp'],"   ", elem['pitch'],"   ", score)
                sum += score
                count +=1
   if count == 0:
       return ("not enough information")
   return (round(sum/count , 5))

def read_json_files_in_folder(folder_path):
    json_data_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_data_list.append(data)
                pitch_value = get_pitch(data)
                print("The average value of pitch is: ", pitch_value)
                print("*************************************************************************")
    return json_data_list

def main():
     # for now taken the path to one singular file...
     # later may write a seprate code script to read data form each file and print data of each video...
     # giving the file path and storing it in json_file_path variable 
    #json_file_path = "D:/video_quality_assessment/video_references/pol-2785-lat-28.6356967lon-77.2202516dt-03-23-23ti-19-06-31.json"
    #with open( json_file_path , 'r') as file:
        #data = json.load(file)
         #to see the whole json file in proper indented form use the following code...
        #print(json.dumps(data , indent = 2))
    #pitch_value = get_pitch(data)
    #print("The average value of pitch is: ", pitch_value)
    folder_path = "D:/video_quality_assessment/video_references/ALL_VIDEOS_WITH_METADATA/OLD_METADATA"
    json_data_list = read_json_files_in_folder(folder_path)
    #for idx, json_data in enumerate(json_data_list):
        #print(f"JSON file {idx+1}:")
        #print(json_data)

if __name__ == "__main__":
    main()