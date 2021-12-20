import picamera
import time
path = '/home/pi/src3/06_multimedia'

camera = picamera.PiCamera()
try:
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(3)
    camera.rotation = 100
    while(True):
        v = input("photo:1, video:2, exit:9 > ")
        if v is "1":
            tt = time.strftime("%Y%m%d_%H%M%S")
            print("사진 촬영")
            camera.capture('%s/photo_%s.jpg' % (path,tt))
        elif v is "2":
            tt = time.strftime("%Y%m%d_%H%M%S")
            print("press enter to stop recording..")
            print("동영상 촬영")
            camera.start_recording('%s/video_%s.h264' % (path,tt))
            input("")
            camera.stop_recording()
        elif v is "9":
            break
        else:
            print("incorrect command")
finally:
    camera.stop_preview()