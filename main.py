import random
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

# Lista de nomes de véias
nomes = [
    "Dona Marlene", "Dona Odete", "Dona Lourdes", "Dona Aparecida", "Dona Tereza",
    "Dona Jandira", "Dona Neuza", "Dona Ivone", "Dona Cacilda", "Dona Sebastiana",
    "Dona Dalva", "Dona Nair", "Dona Filomena", "Dona Antônia", "Dona Geralda",
    "Dona Zuleide", "Dona Efigênia", "Dona Raimunda", "Dona Quitéria", "Dona Iracema"
]

class PixSimulator(App):
    def build(self):
        self.label = Label(text="Esperando PIX das véia...", font_size='20sp')
        Clock.schedule_interval(self.simular_pix, random.randint(30, 60))
        return self.label

    def simular_pix(self, dt):
        nome = random.choice(nomes)
        valor = random.randint(10, 100)
        self.label.text = f"💸 PIX recebido de {nome}: R$ {valor},00"

if __name__ == '__main__':
    PixSimulator().run()