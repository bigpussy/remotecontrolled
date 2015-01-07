import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
def rgb(red,green,blue):
	GPIO.output(11, red)
	GPIO.output(12, green)
	GPIO.output(13, blue)
