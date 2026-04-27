import threading
import time

running = False

def update_loop(get_speed, update_gui):
    global running
    while running:
        try:
            data = get_speed()
            update_gui(data)
        except Exception as e:
            print("Error:", e)
        time.sleep(1)

def start(get_speed, update_gui):
    global running
    if running:
        return
    running = True
    t = threading.Thread(target=update_loop, args=(get_speed, update_gui), daemon=True)
    t.start()

def stop():
    global running
    running = False
