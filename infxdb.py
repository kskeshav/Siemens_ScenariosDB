from datetime import datetime
from influxdb import InfluxDBClient
import os
client = InfluxDBClient(host='localhost',
                        port=8086,
                        username='admin',
                        password='secretpassword')

# line = 'power_info,sensor=motor1 power_in=123,power_out=348'
# client.write([line], {'db': 'energy'}, 204, 'line')


f_path = 'data/oxts/data/'
for filename in os.listdir(f_path):
    f = os.path.join(f_path, filename)
    if os.path.isfile(f):
        with open(f) as file:
            line = file.readline()
        line.rstrip('\n')
        l = line.split(' ')
        values = 'lat=' + l[0]+' lon=' + l[1]+',alt=' + l[2]+',roll=' + l[3]+',pitch=' + l[4]+',yaw=' + l[5]+',vn=' + l[6]+',ve=' + l[7]+',vf=' + l[8]+',vl=' + l[9]+',vu=' + l[10]+',ax=' + l[11]+',ay=' + l[12]+',ay=' + l[13]+',af=' + l[14]+',al=' + l[15]+',au=' + l[16]+',wx=' + l[17]+',wy=' + l[18]+',wz=' + l[19]+',wf=' + l[20]+',wl=' + l[21]+',wu=' + l[22]+',pos_accuracy=' + l[23]+',vel_accuracy=' + l[24]+',navstat=' + l[25]+',numsats=' + l[26]+',posmode=' + l[27]+',velmode=' + l[28]+',orimode=' + l[29]
        # i += 1
        to_write = 'kitti_dataset,'+values
        client.write([to_write], {'db': 'energy'}, 204, 'line')
        
client.close()