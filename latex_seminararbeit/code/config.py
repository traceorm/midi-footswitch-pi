import xml.etree.ElementTree as ElementTree
from midimodes import GrandmeisterMIDI as midi
class xmlReader:
    def __init__(self, configFile):
        self.root=ElementTree.parse(configFile).getroot()
    def getSettingsOfSwitch(self,number):
        settings = []
        for schalter in self.root.findall('schalter'):
            if(schalter.get('number') == number):
                for preset in schalter.findall('preset'):
                    tempSettings = []
                    preset_unformated = ''.join(preset.itertext())
                    for s in preset_unformated.split():
                        if s.isdigit():
                            tempSettings.append(int(s))
                    settings.append(tempSettings)
                for controller in schalter.findall('controller'):
                    tempSettings = midi.setting_resolver[controller.get('name')]
                    if(len(tempSettings)==1):
                        setting_unformated = ''.join(controller.itertext())
                        for s in setting_unformated.split():
                            if s.isdigit():
                            value = int(s) 
                        tempSettings.append(value)
                    settings.append(tempSettings)
        return settings
