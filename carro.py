import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Carro(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.aceler = 6
		self.velocidad = 6
		self.imagenes = [util.cargar_imagen('imagenes/coche.png'),
						util.cargar_imagen('imagenes/carroestre.png')]
                self.arrancon = pygame.mixer.Sound('sonidos/acelerar2.wav')
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(10, 265)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:
			if teclas[K_SPACE] and self.rect.x<=1300:
                                self.acelerar()
                        elif self.rect.x>=0:
                                self.arrancon.stop()
                                self.rect.x -= self.velocidad
			if teclas[K_UP] and self.rect.y>=115:
				self.rect.y -= 10
				self.image = self.imagenes[0]
			elif teclas[K_DOWN] and self.rect.y<=465-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]

	def acelerar(self):
                self.arrancon.play()
                self.rect.x += self.aceler

	
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
