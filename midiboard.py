import RPi.GPIO as GPIO #wird für die ansteuerung der pins benötigt
import time   #wird für alles was mit zeit zu tun hat benötigt
import xml_reader as reader
from midimodes import GrandmeisterMIDI

#GPIOs need to be setup up
GPIO.setmode(GPIO.BCM)

### Konfiguration
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

midi = GrandmeisterMIDI(0, 'USB')

currentBar  = 1 
#variablen die, die aktuelle Funktionen der Schalter vorhalten
#die idee ist im moment alle funktionen die initiert werden sollen als array zu speichern und dann in den HIT-Funktionen alle befehle aus zuführen
#Funktionen sollen aus xml datei geladen werden
currentFunctions = {
	"T1" : [0,[1,2],0], 
	"T2" : [0,0,0],
	"T3" : [0,0,0],
	"T4" : [0,0,0],
	"B1" : [0,0,0],
	"B2" : [0,0,0],
	"B3" : [0,0,0],
	"B4" : [0,0,0],
}


bar1_config = reader.xml_reader(grandmeister_config_bar1.xml)
bar1Functions = {
	"T1" : bar1_config.getSettingsOfSwitch('T1')
	"T2" : bar1_config.getSettingsOfSwitch('T2')
	"T3" : bar1_config.getSettingsOfSwitch('T3')
	"T4" : bar1_config.getSettingsOfSwitch('T4')
	"B1" : bar1_config.getSettingsOfSwitch('B1')
	"B2" : bar1_config.getSettingsOfSwitch('B2')
	"B3" : bar1_config.getSettingsOfSwitch('B3')
	"B4" : bar1_config.getSettingsOfSwitch('B4')
}
del bar1_config

bar2_config = reader.xml_reader(grandmeister_config_bar2.xml)
bar2Functions = {
	"T1" : bar2_config.getSettingsOfSwitch('T1')
	"T2" : bar2_config.getSettingsOfSwitch('T2')
	"T3" : bar2_config.getSettingsOfSwitch('T3')
	"T4" : bar2_config.getSettingsOfSwitch('T4')
	"B1" : bar2_config.getSettingsOfSwitch('B1')
	"B2" : bar2_config.getSettingsOfSwitch('B2')
	"B3" : bar2_config.getSettingsOfSwitch('B3')
	"B4" : bar2_config.getSettingsOfSwitch('B4')
}
del bar2_config

bar3_config = reader.xml_reader(grandmeister_config_bar3.xml)
bar3Functions = {
	"T1" : bar3_config.getSettingsOfSwitch('T1')
	"T2" : bar3_config.getSettingsOfSwitch('T2')
	"T3" : bar3_config.getSettingsOfSwitch('T3')
	"T4" : bar3_config.getSettingsOfSwitch('T4')
	"B1" : bar3_config.getSettingsOfSwitch('B1')
	"B2" : bar3_config.getSettingsOfSwitch('B2')
	"B3" : bar3_config.getSettingsOfSwitch('B3')
	"B4" : bar3_config.getSettingsOfSwitch('B4')
}
del bar3_config

bar4_config = reader.xml_reader(grandmeister_config_bar4.xml)
bar4Functions = {
	"T1" : bar4_config.getSettingsOfSwitch('T1')
	"T2" : bar4_config.getSettingsOfSwitch('T2')
	"T3" : bar4_config.getSettingsOfSwitch('T3')
	"T4" : bar4_config.getSettingsOfSwitch('T4')
	"B1" : bar4_config.getSettingsOfSwitch('B1')
	"B2" : bar4_config.getSettingsOfSwitch('B2')
	"B3" : bar4_config.getSettingsOfSwitch('B3')
	"B4" : bar4_config.getSettingsOfSwitch('B4')
}
del bar4_config

bar5_config = reader.xml_reader(grandmeister_config_bar5.xml)
bar5Functions = {
	"T1" : bar5_config.getSettingsOfSwitch('T1')
	"T2" : bar5_config.getSettingsOfSwitch('T2')
	"T3" : bar5_config.getSettingsOfSwitch('T3')
	"T4" : bar5_config.getSettingsOfSwitch('T4')
	"B1" : bar5_config.getSettingsOfSwitch('B1')
	"B2" : bar5_config.getSettingsOfSwitch('B2')
	"B3" : bar5_config.getSettingsOfSwitch('B3')
	"B4" : bar5_config.getSettingsOfSwitch('B4')
}
del bar5_config

bar6_config = reader.xml_reader(grandmeister_config_bar6.xml)
bar6Functions = {
	"T1" : bar6_config.getSettingsOfSwitch('T1')
	"T2" : bar6_config.getSettingsOfSwitch('T2')
	"T3" : bar6_config.getSettingsOfSwitch('T3')
	"T4" : bar6_config.getSettingsOfSwitch('T4')
	"B1" : bar6_config.getSettingsOfSwitch('B1')
	"B2" : bar6_config.getSettingsOfSwitch('B2')
	"B3" : bar6_config.getSettingsOfSwitch('B3')
	"B4" : bar6_config.getSettingsOfSwitch('B4')
}
del bar6_config

bar7_config = reader.xml_reader(grandmeister_config_bar7.xml)
bar7Functions = {
	"T1" : bar7_config.getSettingsOfSwitch('T1')
	"T2" : bar7_config.getSettingsOfSwitch('T2')
	"T3" : bar7_config.getSettingsOfSwitch('T3')
	"T4" : bar7_config.getSettingsOfSwitch('T4')
	"B1" : bar7_config.getSettingsOfSwitch('B1')
	"B2" : bar7_config.getSettingsOfSwitch('B2')
	"B3" : bar7_config.getSettingsOfSwitch('B3')
	"B4" : bar7_config.getSettingsOfSwitch('B4')
}
del bar7_config

bar8_config = reader.xml_reader(grandmeister_config_bar8.xml)
bar8Functions = {
	"T1" : bar8_config.getSettingsOfSwitch('T1')
	"T2" : bar8_config.getSettingsOfSwitch('T2')
	"T3" : bar8_config.getSettingsOfSwitch('T3')
	"T4" : bar8_config.getSettingsOfSwitch('T4')
	"B1" : bar8_config.getSettingsOfSwitch('B1')
	"B2" : bar8_config.getSettingsOfSwitch('B2')
	"B3" : bar8_config.getSettingsOfSwitch('B3')
	"B4" : bar8_config.getSettingsOfSwitch('B4')
}
del bar8_config

barTooBarFunctions = {
	1: bar1Functions,
	2: bar2Functions,
	3: bar3Functions,
	4: bar4Functions,
	5: bar5Functions,
	6: bar6Functions,
	7: bar7Functions,
	8: bar8Functions
}


### Methoden, welche das Senden aufrufen
## werden ggf einen switch / elifchain brauchen für die currentBar    

#top buttons
def s0_tHit():
	midi.functionResolver(currentFunctions[1])
    #do midi stuff here
def s1_tHit():
    midi.functionResolver(currentFunctions[2])
def s2_tHit():
    #do midi stuff here
    midi.functionResolver(currentFunctions[3])
def s3_tHit():
    #do midi stuff here
    midi.functionResolver(currentFunctions[4])
def s4_tHit():
    #kein midi stuff hier, nur inkrementieren der currentBar     variable und aufrufen der led-funktion.
    currentBar     += 1
    if(currentBar>8):
    	currentBar = 1
    currentFunctions = barTooBarFunctions[currentBar]	
    setLEDBar()

#bottom buttons
def s0_bHit():
    #do midi stuff here
    midi.functionResolver(currentFunctions[5])
def s1_bHit():
    #do midi stuff here
    midi.functionResolver(currentFunctions[6])
def s2_bHit():
    #do midi stuff here
    midi.functionResolver(currentFunctions[7])
def s3_bHit():
    #do midi stuff here
    midi.functionResolver(currentFunctions[8])
def s4_bHit():
    #kein midi stuff hier, nur inkrementieren der currentBar     variable und aufrufen der led-funktion.
    currentBar     -= 1
    if(currentBar<1):
    	currentBar = 8
    setLEDBar()


def setLEDBar():
	## hier leds in abhängigkeit der currentBar setzen.


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





#alles interuppt gesteuert, also kann auf hardware off gewartet werden, um endlos loop zu verhindern

try:
    print "Programm ends on Panic Switch"
    GPIO.wait_for_edge(PANIC, GPIO.RISING)
    print "and there it is"
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
