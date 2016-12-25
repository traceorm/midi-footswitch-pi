#!/usr/bin/env python
# coding: utf8
import rtmidi_python as rtmidi #wird für midi benötigt
import time

class GrandmeisterMIDI:

#define all the MIDI-MODES
    #volume
    setting_resolver={
        'volume_soft':[7],
        'volume_hard':[57],
        'clean':[31,0],
        'chrunch':[31,32],
        'lead':[31,64],
        'ultra':[31,96],
        'boost_off':[64,0],
        'boost_on':[64,64],
        'noise_gate_off':[63,0],
        'noise_gate_on':[63,64],
        'fx_loop_off':[55,0],
        'fx_loop_on':[55,64],
        'powersoak_0':[30,0],
        'powersoak_1':[30,26],
        'powersoak_5':[30,52],
        'powersoak_18':[30,78],
        'powersoak_36':[30,102],
        'mod_on':[52, 64],
        'mod_off':[52, 0],
        'mod_intensity':[31],
        'mod_speed':[26],
        'mod_chorus':[12, 0],
        'mod_flanger':[12, 32],
        'mod_phaser':[12, 64],
        'mod_tremolo':[12, 96],
        'relay_on':[63,64],
        'relay_off':[63,0],
        'delay_time':[4],
        'delay_feedback':[27],
        'delay_volume':[28],
        'reverb_on':[54,64],
        'reverb_off':[54,0],
        'reverb_volume':[29],
        'mute_on':[9,64],
        'mute_off':[9,0],
        'gain_hard':[56],
        'gain_soft':[20],
        'bass':[21],
        'mid':[22],
        'treble':[23],
        'resonance':[24],
        'presence':[25]
    }


##Klassenvariabeln

    def __init__(self, midi_channel, midi_device_name_part):
        self.__MIDI_CHANNEL=midi_channel
        self.__midiout = rtmidi.MidiOut()
        self.__available_ports = self.__midiout.get_ports()
        if(len(self.__available_ports) == 1):
            __midiout.open_port(0)
        else:
            for port in self.__available_ports:
                if(port.find(midi_device_name_part)>-1):
                    self.__midiout.open_port(name=port)
                else:
                    pass
                    ##no port found


	def functionResolver(self, functionList):
		#durch alle funktionen iterieren
		for command in functionList:
			#if length 1 programChange
			if(len(command)==1):
				programChange(command[0])
			#if length 2 controllerChange
			if(len(command)==2):
				controllerChange(command[0],command[1])
			time.sleep(0.01)


    def programChange(self, number):
        #hier dann bitte den entsprechenden Befehl zusammen basteln
        statusbyte = 0xC0+(__MIDI_CHANNEL-1)
        databyte1  = number
        __midiout.send_message([statusbyte,databyte1])


    def controllerChange(self, controller, value):
        statusbyte = 0xB0+(__MIDI_CHANNEL-1)
        databyte1 = controller
        databyte2 = value
        __midiout.send_message([statusbyte,databyte1,databyte2])






