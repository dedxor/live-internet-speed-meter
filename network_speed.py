import psutil
import time

class NetworkSpeed:
  def __init__(self):
    self.last_bytes_sent = 0
    self.last_bytes_recv = 0
    self.last_time = time.time()
  
    net = psutil.net_io_counters()
    self.last_bytes_sent = net.bytes_sent
    self.last_bytes_recv = net.bytes_recv
 
  def get_speed(self):
    currenttime = time.time()
    net = psutil.net_io_counters()
    current_bytes_sent = net.bytes_sent
    current_bytes_recv = net.bytes_recv

    time_diff = current_time - self.last_time

    upload speed = (current_bytes_sent - self.last_bytes_sent)/time_diff
    download speed = (current_bytes_recv - self.last_bytes_recv)/time/diff

    self.last_bytes_sent = current_bytes_sent
    self.last_bytes_recv = current_bytes_recv
    self.last_time = current_time

    upload_speed_mbps = (upload_speed*8) / (1024*1024)
    download_speed_mbps = (download_speed*8)/(1024*1024)
    return round(upload_speed_mbps, 2), round(download_speed_mbps, 2)

