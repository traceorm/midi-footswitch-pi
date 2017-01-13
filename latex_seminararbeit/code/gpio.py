GPIO.setmode(GPIO.BCM)
S0_T = 17
GPIO.setup(S0_T, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(S0_T, GPIO.BOTH, callback=s0_tBoth, bouncetime=300)
def s0_tBoth(channel):
	midi.functionResolver(currentFunctions['T0'])