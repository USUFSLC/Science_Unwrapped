#!/usr/bin/env python

import random
import pygame

class Asteroid(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("asteroid.png")
		self.Xpos = 400
		self.Ypos = 175
		self.rect = self.image.get_rect()
		self.state = 0
		
	def update(self, state, xPos):
		
		self.state = state
		if self.state == 0:
			self.Ypos = 50
		elif self.state == 1:
			self.Ypos = 150
		elif self.state == 2:
			self.Ypos = 280
		
		self.Xpos = xPos

class Apple(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("apple.png").convert()
		self.Xpos = 400
		self.Ypos = 50
		self.rect = self.image.get_rect()
		self.rect.move(self.Xpos, self.Ypos)
		self. state = 0
		
	def update(self, state, xPos):
		self.state = state
		
		if self.state == 0:
			self.Ypos = 50
		elif self.state == 1:
			self.Ypos = 150
		elif self.state == 2:
			self.Ypos = 280
		
		self.Xpos = xPos
		self.rect.move(self.Xpos, self.Ypos)

class Penguin(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("babytux.png").convert()
		self.xPos = 100
		self.yPos = 0
		self.state = 0
		self.rect = self.image.get_rect()
		self.rect.move(self.xPos, self.yPos)
		
class spaceFruit(object):
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((640,400))
		self.screenrect = self.screen.get_rect()
		pygame.display.set_caption("SpaceFruit")
		self.running = True
		self.penguin = Penguin()
		self.asteroid1 = Asteroid()
		self.asteroid2 = Asteroid()
		self.apple = Apple()
		self.coloumn = [self.asteroid1, self.apple, self.asteroid2]
		self.coloumnXpos = 600
		
		self.asteroidGroup = pygame.sprite.Group(self.asteroid1, self.asteroid2)
		self.appleGroup = pygame.sprite.Group(self.apple)
		
	def isEnd(self):
		if (self.asteroid1.Xpos == self.penguin.xPos and self.asteroid1.state == self.penguin.state) or (self.asteroid2.Xpos == self.penguin.xPos and self.asteroid2.state == self.penguin.state):
			self.running = False
		
	def update(self):
		
		if self.penguin.state == 0:
			self.penguin.yPos = 50
			
		elif self.penguin.state == 1:
			self.penguin.yPos = 150
			
		elif self.penguin.state ==2:
			self.penguin.yPos = 280
			
		self.penguin.rect.move(self.penguin.xPos, self.penguin.yPos)
		
		
		if self.coloumnXpos <= 100:
			if self.isEnd():
				self.running = False
		
		if self.coloumnXpos <= 0:
			self.coloumnXpos = 600
			
			random.shuffle(self.coloumn)
		else:
			self.coloumnXpos = self.coloumnXpos - .5
		
		for i in range(len(self.coloumn)):
			self.coloumn[i].update(i, self.coloumnXpos)
		
	def render(self):
		
		self.screen.fill((255,255,255))
		self.screen.blit(self.penguin.image, (self.penguin.xPos,self.penguin.yPos))
		for obj in self.coloumn:
			self.screen.blit(obj.image, (obj.Xpos,obj.Ypos))
		pygame.display.flip()
		
		
	def main(self):
	
		while( self.running ):
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if event.key == pygame.K_DOWN:
						self.penguin.state = (self.penguin.state + 1) %3 
					if event.key == pygame.K_UP:
						self.penguin.state = (self.penguin.state +2) %3
						
			self.update()
			self.render()
	
if __name__ == "__main__":
	game = spaceFruit()
	game.main()
