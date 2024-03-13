from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"

client = InfluxDBClient(
    url="http://localhost:8086",
    token="NbU2UNq4ZkwPD0WnvqBcqG3pteeJUFhVRWcO8PMk13ibJLPSgmNUTc6aiU8LLgamW_zVkySo-IVe89700aAzcw==",
    org="organization",
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

# write_api.write(bucket=bucket, record=p)

## using Table structure

query_api = client.query_api()
tables = query_api.query('from(bucket:"my-bucket") |> range(start: -1m)')

for table in tables:
    print(table)
    for row in table.records:
        print(row.values)

# FluxTable() columns: 9, records: 1
# {
#     'result': '_result', 
#     'table': 0, 
#     '_start': datetime.datetime(2024, 3, 13, 2, 34, 33, 366742,tzinfo=tzutc()), 
#      '_stop': datetime.datetime(2024, 3, 13, 2, 34, 43, 366742, tzinfo=tzutc()), 
#      '_time': datetime.datetime(2024, 3, 13, 2, 34, 43, 360182, tzinfo=tzutc()), 
#      '_value': 25.3, 
#      '_field': 'temperature',
#      '_measurement': 'my_measurement',
#       'location': 'Prague'
#       }




## using csv library
# csv_result = query_api.query_csv('from(bucket:"bucket") |> range(start: -10m)')
# val_count = 0
# for row in csv_result:
#     for cell in row:
#         val_count += 1
