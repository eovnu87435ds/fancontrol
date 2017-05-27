import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
n=10
for counter in range(0,n):
  GPIO.output(21, 1)
  print("21 HIGH")
  time.sleep(1)
  GPIO.output(22, 1)
  print("22 HIGH")
  time.sleep(1)
  GPIO.output(21, 0)
  print("21 LOW")
  time.sleep(1)
  GPIO.output(22, 0)
  print("22 LOW")
  time.sleep(1)

GPIO.cleanup()
print("Finished.")
