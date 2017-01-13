import xml.etree.ElementTree as ElementTree
from midimodes import GrandmeisterMIDI
class xmlReader:



	def __init__(self, configFile):
		self.root=ElementTree.parse(configFile).getroot()
	def getSettingsOfSwitch(self,number):
		settings = []
		#durch root laufen und alle 'schalter' suchen
		for schalter in self.root.findall('schalter'):
			#falls da der gesuchte schalter bei ist
			if(schalter.get('number') == number):
				for preset in schalter.findall('preset'):
					tempSettings = []
					preset_unformated = ''.join(preset.itertext())
					for s in preset_unformated.split():
						if s.isdigit():
							tempSettings.append(int(s))
					settings.append(tempSettings)
				#durch alle controller laufen
				for controller in schalter.findall('controller'):
					#Name des Controllers auflösen and damit Einstellung erfahren
					tempSettings = GrandmeisterMIDI.setting_resolver[controller.get('name')]
					#if there is only one item in list
					if(len(tempSettings)==1):
						#look into controller and get the value as second item
						setting_unformated = ''.join(controller.itertext())
						for s in setting_unformated.split():
							if s.isdigit():
								value = int(s) 
						tempSettings.append(value)
					settings.append(tempSettings)

		return settings		
