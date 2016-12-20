import rtmidi #wird für midi benötigt

class GrandmeisterMIDI:

	def __init__(self, MIDI_CHANNEL):
         self.MIDI_CHANNEL

	MIDI_CHANNEL = 0

	def preset(self, number):
		#hier dann bitte den entsprechenden Befehl zusammen basteln

	def midiResolver(self, valueToResolve):
		#diese funktion wird alle Midi-Befehlswerte die letzlich aus dem XML-File kommen entgegen nehmen und den entsprechenden midi befehl entsenden

	#define all the MIDI-MODES
	PRESET_0 = 0
	PRESET_1 = 1
	PRESET_2 = 2
	PRESET_3 = 3
	PRESET_4 = 4
	PRESET_5 = 5
	PRESET_6 = 6
	PRESET_7 = 7
	PRESET_8 = 8
	PRESET_9 = 9

	PRESET_10 = 10
	PRESET_11 = 11
	PRESET_12 = 12
	PRESET_13 = 13
	PRESET_14 = 14
	PRESET_15 = 15
	PRESET_16 = 16
	PRESET_17 = 17
	PRESET_18 = 18
	PRESET_19 = 19

	PRESET_20 = 20
	PRESET_21 = 21
	PRESET_22 = 22
	PRESET_23 = 23
	PRESET_24 = 24
	PRESET_25 = 25
	PRESET_26 = 26
	PRESET_27 = 27
	PRESET_28 = 28
	PRESET_29 = 29

	PRESET_30 = 30
	PRESET_31 = 31
	PRESET_32 = 32
	PRESET_33 = 33
	PRESET_34 = 34
	PRESET_35 = 35
	PRESET_36 = 36
	PRESET_37 = 37
	PRESET_38 = 38
	PRESET_39 = 39

	PRESET_40 = 40
	PRESET_41 = 41
	PRESET_42 = 42
	PRESET_43 = 43
	PRESET_44 = 44
	PRESET_45 = 45
	PRESET_46 = 46
	PRESET_47 = 47
	PRESET_48 = 48
	PRESET_49 = 49

	PRESET_50 = 50
	PRESET_51 = 51
	PRESET_52 = 52
	PRESET_53 = 53
	PRESET_54 = 54
	PRESET_55 = 55
	PRESET_56 = 56
	PRESET_57 = 57
	PRESET_58 = 58
	PRESET_59 = 59

	PRESET_60 = 60
	PRESET_61 = 61
	PRESET_62 = 62
	PRESET_63 = 63
	PRESET_64 = 64
	PRESET_65 = 65
	PRESET_66 = 66
	PRESET_67 = 67
	PRESET_68 = 68
	PRESET_69 = 69	

	PRESET_70 = 70
	PRESET_71 = 71
	PRESET_72 = 72
	PRESET_73 = 73
	PRESET_74 = 74
	PRESET_75 = 75
	PRESET_76 = 76
	PRESET_77 = 77
	PRESET_78 = 78
	PRESET_79 = 79

	PRESET_90 = 90
	PRESET_91 = 91
	PRESET_92 = 92
	PRESET_93 = 93
	PRESET_94 = 94
	PRESET_95 = 95
	PRESET_96 = 96
	PRESET_97 = 97
	PRESET_98 = 98
	PRESET_99 = 99

	PRESET_100 = 100
	PRESET_101 = 101
	PRESET_102 = 102
	PRESET_103 = 103
	PRESET_104 = 104
	PRESET_105 = 105
	PRESET_106 = 106
	PRESET_107 = 107
	PRESET_108 = 108
	PRESET_109 = 109

	PRESET_110 = 110
	PRESET_111 = 111
	PRESET_112 = 112
	PRESET_113 = 113
	PRESET_114 = 114
	PRESET_115 = 115
	PRESET_116 = 116
	PRESET_117 = 117
	PRESET_118 = 118
	PRESET_119 = 119

	PRESET_120 = 120
	PRESET_121 = 121
	PRESET_122 = 122
	PRESET_123 = 123
	PRESET_124 = 124
	PRESET_125 = 125
	PRESET_126 = 126
	PRESET_127 = 127




	#all the CHANNELS
	CLEAN   		= 	'clean'				#cc31 value 0-31
	CHRUNCH 		= 	'chrunch'			#cc31 value 32-63
	LEAD 			= 	'lead'				#cc31 value 64-95
	ULTRA			= 	'ultra'				#cc31 value 96-127

	#boost
	BOOST_OFF		=  	'boost_off' 		#cc64 value 0-63
	BOOST_OFF		=  	'boost_off' 		#cc64 value 64-127

	#noisegate
	NOISE_GATE_OFF	=  	'noise_gate_off' 	#cc63 value 0 - 63
	NOISE_GATE_ON	=  	'noise_gate_on' 	#cc63 value 64 - 127

	#fx-loop
	FX_LOOP_OFF 	= 	'fx_loop_off'		#cc55 value 0-63
	FX_LOOP_ON 		= 	'fx_loop_on'		#cc55 value 64-127

	#powersoak
	POWERSOAK_0		=	'powersoak_0'		#cc30 value 0-25
	POWERSOAK_1		=	'powersoak_1'		#cc30 value 26-61
	POWERSOAK_5		=	'powersoak_5'		#cc30 value 52-77
	POWERSOAK_18	=	'powersoak_18'		#cc30 value 78-101
	POWERSOAK_36	=	'powersoak_36'		#cc30 value 102-127


	##EFEKTE FEHLEN NOCH!







