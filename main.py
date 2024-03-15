from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import schedule
import random
import time

# You can generate a Token from the "Tokens Tab" in the UI
token = "wiFlgH8M0wcqCE_0eWLPvzDFoHwxhENER7HcpWqaaN0GQBfJ7rLwBktzAMADpiBPCgijp4ni8U8tdV96-hPWpA=="
org = "organization"
bucket = "my-bucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)

sequence = [
    "mem,host=host1 used_percent=23.43234543",
    "mem,host=host1 available_percent=15",
    "mem,host=host1 test1_percent=13",
    "mem,host=host1 test2=20",
]
write_api.write(bucket, org, sequence)

STOP = True

i = 1000
while STOP:
    sequence = []
    m1 = random.randint(100, 500)
    sequence.append("pressing,host=host1 press1=" + str(m1))
    m2 = random.randint(500, 1000)
    sequence.append("pressing,host=host1 press2=" + str(m2))
    # m3 = random.randint(300, 500)
    # sequence.append("pressing,host=host1 press3=" + str(m3))
    # m4 = random.randint(400, 600)
    # sequence.append("pressing,host=host1 press4=" + str(m4))
    write_api.write(bucket, org, sequence)
    i = i - 1
    print(sequence)
    time.sleep(10)
    if i == 0:
        STOP = False



#  Write Dictionary-style object ใช้ไม่ได้
write_api.write("my-bucket", org, {"measurement": "h2o_feet", "tags": {"location": "coyote_creek"},
                                                    "fields": {"water_level": 1.0}, "time": 1})

# schedule.every(1).seconds.do(job)
