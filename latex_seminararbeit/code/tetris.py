import time
import rtmidi


bpm=140
viertelzeit=60/bpm

länge = {
    1:4*viertelzeit,
    2:2*viertelzeit,
    4:1*viertelzeit,
    8:0.5*viertelzeit,
    16:0.25*viertelzeit,
    32:0.125*viertelzeit
}

def punktierte(wert):
    return länge[wert]*1.5

lied = [
    [länge[4],79],[länge[8],74],[länge[8],75],
    [länge[4],77],[länge[8],75],[länge[8],74],
    [länge[4],72],[länge[8],72],[länge[8],75],
    [länge[4],79],[länge[8],77],[länge[8],75],
    [punktierte(4),74],[länge[8],75],
    [länge[4],77],[länge[4],79],
    [länge[4],75],[länge[4],72],
    [länge[4],72],[länge[4],0],
    [länge[8],0],[länge[4],77],[länge[8],80],
    [länge[4],84],[länge[8],82],[länge[8],80],
    [punktierte(4),79],[länge[8],75],
    [länge[4],79],[länge[8],77],[länge[8],75],
    [länge[4],74],[länge[8],74],[länge[8],75],
    [länge[4],77],[länge[4],79],
    [länge[4],75],[länge[4],72],
    [länge[4],72],[länge[4],0]
]

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

for note in lied:
    #print("play note"+str(note[0]))
    note_on = [0x90, note[1], 112] # channel 1, middle C, velocity 112
    note_off = [0x80, note[1], 0]
    if note[1] == 0:
        note_on = note_off
    midiout.send_message(note_on)
    time.sleep(note[0])
    midiout.send_message(note_off)
    #print("stop note")

del midiout





