from sds011 import SDS011
import time
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
sensor.sleep(sleep=False)
time.sleep(15)
print(sensor.query())
