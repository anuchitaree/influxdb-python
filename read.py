from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
bucket = "my-bucket"

client = InfluxDBClient(
    url="http://localhost:8086",
    token="NbU2UNq4ZkwPD0WnvqBcqG3pteeJUFhVRWcO8PMk13ibJLPSgmNUTc6aiU8LLgamW_zVkySo-IVe89700aAzcw==",
    org="organization",
)

write_api = client.write_api(write_options=SYNCHRONOUS)
p = Point("my_measurement2").tag("location", "Prague2").field("temperature2", 30)

write_api.write(bucket=bucket, record=p)

query_api = client.query_api()

query = 'from(bucket:"my-bucket")\
|> range(start: -10s)\
|> filter(fn:(r) => r._measurement == "my_measurement2")\
|> filter(fn:(r) => r.location == "Prague2")\
|> filter(fn:(r) => r._field == "temperature2")'

result = query_api.query(query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value(),record.get_time()))

print(results)
