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
	
	def update(self):
		if self.state == 0:
			self.yPos = 50
			
		elif self.state == 1:
			self.yPos = 150
			
		elif self.state ==2:
			self.yPos = 280
			
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
		
		self.gameState = 0
		self.score = 0
		
	def isEnd(self):
		if (self.asteroid1.Xpos == self.penguin.xPos and self.asteroid1.state == self.penguin.state) or (self.asteroid2.Xpos == self.penguin.xPos and self.asteroid2.state == self.penguin.state):
			self.gameState = 2
	
	def text_objects(self,text, font):
		textSurface = font.render(text, True, (0,0,0))
		return textSurface, textSurface.get_rect()
	
	def message(self, text):
		LargeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = self.text_objects(text, LargeText)
		TextRect.center =(320,200)
		self.screen.blit(TextSurf,TextRect)
		
	def display_score(self, text):
		normalText = pygame.font.Font('freesansbold.ttf', 20)
		TextSurf, TextRect = self.text_objects(text, normalText)
		TextRect.center =(400, 30)
		self.screen.blit(TextSurf, TextRect)
		
	def update(self):
		
		self.penguin.update()
		
		if self.coloumnXpos <= 100:
			if self.isEnd():
				self.gameState = 2
		
		if self.coloumnXpos <= 0:
			self.coloumnXpos = 600
			self.score = self.score + 1
			random.shuffle(self.coloumn)
		else:
			"""
			"""
			self.coloumnXpos = self.coloumnXpos - 1
			"""
			"""
		for i in range(len(self.coloumn)):
			self.coloumn[i].update(i, self.coloumnXpos)
		
	def render(self):
		
		self.screen.fill((255,255,255))
		if self.gameState == 2:
			self.message("Score: " + str(self.score))
		else:
			self.display_score("Score: " + str(self.score))
			self.screen.blit(self.penguin.image, (self.penguin.xPos,self.penguin.yPos))
			self.screen
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
							
					if self.gameState == 0:
						if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
							self.gameState = 1
	
					if self.gameState == 1:
						if event.key == pygame.K_DOWN:
							self.penguin.state = (self.penguin.state + 1) %3 
						if event.key == pygame.K_UP:
							self.penguin.state = (self.penguin.state +2) %3
							
					if self.gameState == 2:
						self.gameState = 1
						self.score = -1
							
			if self.gameState != 2:	
				self.update()
				self.render()
	
if __name__ == "__main__":
	game = spaceFruit()
	game.main()
