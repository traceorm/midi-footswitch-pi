def __init__(self, midi_channel, midi_device_name_part):
    self.__MIDI_CHANNEL=midi_channel
    self.__midiout = rtmidi.MidiOut()
    self.__available_ports = self.__midiout.getports()
        for port in self.__available_ports
            if(port.find(midi_device_name_part)>-1):
                self.__midiout.open_port(port)
            else:
                pass
def controllerChange(self, controller, value):
        statusbyte = 0xB0+(__MIDI_CHANNEL-1)
        __midiout.send_message([statusbyte,controller,value])                

