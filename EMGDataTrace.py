#EMG Data Trace
#Sarah van der Laan
#Summer 2014

import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class EMGData(BoxLayout):
	def addData(self):
		p = MeshLinePlot(color=[1,0,0,1])
		p.points = [(x, 0.5) for x in range(-10,10)]
		self.ids['my_graph'].add_plot(p)

	#method called when slider value changes (i.e. when slider is moved)
	def scale(self, value, slider):
		slider = self.ids[slider]
		#need to find way to check if slider is going left or right

#eventually need EMG data entered as a parameter
class EMGDataTrace(App):
	def build(self):
		screen = EMGData()
		#screen.addData()
		return screen
		#return EMGData()

if __name__ == "__main__":
	EMGDataTrace().run()

	
