#dict['key1']['ket2]

#dict['3']['format']['tags']["sensor data"]

#data['sensor data']

import json

def read_json_value(file_path):
    with open(file_path , 'r') as file:
        data = json.load(file)
        sensor_string =  data['3']['streams']#['tags']#['sensorData']#['value']
        #sensor_string = eval(sensor_string)
        print(sensor_string[0].get('chroma_location').get('value'))
        #sensor_string = eval(sensor_string[0])
         # print(sensor_string)
        print(type(sensor_string[0].get('chroma_location')))
        #for elem in sensor_string:
        #    count+=1
        #    sum_pitch += elem['pitch']
        #    print(elem['timeStamp'],"   ", elem['pitch'])
        #avg_pitch = sum_pitch/count
        #print(avg_pitch)
        
        #print(elem['bit_rate'])
            # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

            # print(rep)
    #return value


# Example usage
json_file_path = "D:/video quality assessment/video references/pol-3442-lat-25.4609651lon-78.5743676dt-05-03-23ti-12-09-23.json"
hhe = read_json_value(json_file_path)
