import RPi.GPIO as GPIO #wird für die ansteuerung der pins benötigt
import time   #wird für alles was mit zeit zu tun hat benötigt
import rtmidi #wird für midi benötigt
GPIO.setmode(GPIO.BCM)
#GPIOs need to be setup up


#Saveing GPIO Pin Nimbers for each switch here as Constant
# switch top left to right
S0_T = 17
S1_T = 24
S2_T = 11
S3_T = 13
S4_T = 16

# switches bottom left to right
S0_B = 3
S1_B = 7
S2_B = 2
S3_B = 9
S4_B = 18

#panic button to end programm // wichtig weil hardware gesteuert
PANIC = 8


#Setting up GPIO
#top line
GPIO.setup(S0_T, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S1_T, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S2_T, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S3_T, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S4_T, GPIO_IN, pull_up_down=GPIO.PUD_UP)

#bottomline

GPIO.setup(S0_B, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S1_B, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S2_B, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S3_B, GPIO_IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(S4_B, GPIO_IN, pull_up_down=GPIO.PUD_UP)

#panic button
#defining a panic button, which we wait for, to create a initity loop without loop //SINNVOLL DA JA REINE HARDWARE STEUERUNG
GPIO.setup(PANIC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#define functions for each switch to be triggerd by interrupts

#top buttons
def s0_tHit():
    #do midi stuff here
    print "HeyHo, there was a button pressed, it calls itself S0_T"

def s1_tHit():
    #do midi stuff here

def s2_tHit():
    #do midi stuff here

def s3_tHit():
    #do midi stuff here

def s4_tHit():
    #do midi stuff here


#bottom buttons
def s0_bHit():
    #do midi stuff here

def s1_bHit():
    #do midi stuff here

def s2_bHit():
    #do midi stuff here

def s3_bHit():
    #do midi stuff here

def s4_bHit():
    #do midi stuff here


#define all interrupt funktions on GIOP level. We need two for each switches
#since we got switches but want a button behavior / trigger on every change

#top line switch interrupts
def s0_tFalling(channel):
    s0_tHit()
def s0_tRising(chanel):
    s0_tHit()
def s1_tFalling(channel):
    s1_tHit()
def s1_tRising(chanel):
    s1_tHit()
def s2_tFalling(channel):
    s2_tHit()
def s2_tRising(chanel):
    s2_tHit()
def s3_tFalling(channel):
    s3_tHit()
def s3_tRising(chanel):
    s3_tHit()
def s4_tFalling(channel):
    s4_tHit()
def s4_tRising(chanel):
    s4_tHit()

#bottom line switch interrupts
def s0_bFalling(channel):
    s0_bHit()
def s0_bRising(chanel):
    s0_bHit()
def s1_bFalling(channel):
    s1_bHit()
def s1_bRising(chanel):
    s1_bHit()
def s2_bFalling(channel):
    s2_bHit()
def s2_bRising(chanel):
    s2_bHit()
def s3_bFalling(channel):
    s3_bHit()
def s3_bRising(chanel):
    s3_bHit()
def s4_bFalling(channel):
    s4_bHit()
def s4_bRising(chanel):
    s4_bHit()

#define interrupts at GPIO

#top line interrupts
GPIO.add_event_detect(S0_T, GPIO.FALLING, callback=s0_tFalling, bouncetime=300)
GPIO.add_event_detect(S0_T, GPIO.RISING, callback=s0_tRising, bouncetime=300)
GPIO.add_event_detect(S1_T, GPIO.FALLING, callback=s1_tFalling, bouncetime=300)
GPIO.add_event_detect(S1_T, GPIO.RISING, callback=s1_tRising, bouncetime=300)
GPIO.add_event_detect(S2_T, GPIO.FALLING, callback=s2_tFalling, bouncetime=300)
GPIO.add_event_detect(S2_T, GPIO.RISING, callback=s2_tRising, bouncetime=300)
GPIO.add_event_detect(S3_T, GPIO.FALLING, callback=s3_tFalling, bouncetime=300)
GPIO.add_event_detect(S3_T, GPIO.RISING, callback=s3_tRising, bouncetime=300)
GPIO.add_event_detect(S4_T, GPIO.FALLING, callback=s4_tFalling, bouncetime=300)
GPIO.add_event_detect(S4_T, GPIO.RISING, callback=s4_tRising, bouncetime=300)

#bottom line interrupts
GPIO.add_event_detect(S0_B, GPIO.FALLING, callback=s0_bFalling, bouncetime=300)
GPIO.add_event_detect(S0_B, GPIO.RISING, call(back=s0_bRising, bouncetime=300)
GPIO.add_event_detect(S1_B, GPIO.FALLING, callback=s1_bFalling, bouncetime=300)
GPIO.add_event_detect(S1_B, GPIO.RISING, callback=s1_bRising, bouncetime=300)
GPIO.add_event_detect(S2_B, GPIO.FALLING, callback=s2_bFalling, bouncetime=300)
GPIO.add_event_detect(S2_B, GPIO.RISING, callback=s2_bRising, bouncetime=300)
GPIO.add_event_detect(S3_B, GPIO.FALLING, callback=s3_bFalling, bouncetime=300)
GPIO.add_event_detect(S3_B, GPIO.RISING, callback=s3_bRising, bouncetime=300)
GPIO.add_event_detect(S4_B, GPIO.FALLING, callback=s4_bFalling, bouncetime=300)
GPIO.add_event_detect(S4_B, GPIO.RISING, callback=s4_bRising, bouncetime=300)





try:
    print "Programm ends on Panic Switch"
    GPIO.wait_for_edge(PANIC, GPIO.RISING)
    print "and there it is"
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
