from picamera import PiCamera
camera = PiCamera()
picture_number = 1
import time

def setup():
    camera.start_preview(alpha=200)

def take_picture():    
    for i in range(10):
        camera.capture('/home/pi/my_photo%s.jpg' % i)
        time.sleep(45)    
    while True:
        pass

def destroy():
    camera.stop_preview()

def main():
    while True:
        take_picture()
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()