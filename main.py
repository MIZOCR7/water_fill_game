import pygame 
import random 
import copy, sys


pygame.init()

WIDTH, HEIGHT = 500, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Water Fill Game') 

FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 24)
new_game = True

tubes = 10
tube_colors = []

def main():
  while True:
    screen.fill('black') 
    clock.tick(FPS) 
    
    if new_game:
      pass 
    
    
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit() 
        
        
    pygame.display.update()
    


def generate_start():
  tubes_number = random.randint(10, 14) 
  tube_colors = []
  available_colors = [] 
  
  return tubes_number, tube_colors


   
if __name__ == '__main__':
  main()


