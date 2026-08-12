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

tubes = 10
tube_colors = []
color_choices = ['red', 'orange', 'light blue', 'dark blue', 'dark green', 'pink', 'purple', 'dark gray', 'brown', 'light green', 'yellow', 'white', 'gold', 'cyan'] 

def main():
  new_game = True
  while True:
    screen.fill('black') 
    clock.tick(FPS) 
    
    if new_game:
      tubes, tube_colors = generate_start() 
      initial_colors = copy.deepcopy(tube_colors) 
      new_game = False 
    else:
      tube_rects = draw_tubes(tubes, tube_colors) 
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit() 
        
        
    pygame.display.update()
    


def generate_start():
  tubes_number = random.randint(10, 12) 
  tube_colors = []
  available_colors = [] 
  
  for i in range(tubes_number):
    tube_colors.append([]) 
    if i < tubes_number - 2:
      for j in range(4):
        available_colors.append(i) 
        
  for i in range(tubes_number - 2):
    for j in range(4):
      color = random.choice(available_colors) 
      tube_colors[i].append(color) 
      available_colors.remove(color)
  
  
  return tubes_number, tube_colors



def draw_tubes(tubes_num, tube_cols):

  tube_boxes = []
  if tubes % 2 == 0:
    tubes_per_row = tubes_num // 2
    offset = False
  else:
    tubes_per_row = tubes_num // 2 + 1
    offset = True

  spacing = WIDTH / tubes_per_row

  for i in range(tubes_per_row):
    for j in range(len(tube_cols[i])):
      pygame.draw.rect(screen, color_choices[tube_cols[i][j]], [5 + spacing*i, 200 - (50 * j), 65, 50], 0, 3)  

    box = pygame.draw.rect(screen, 'blue', [5 + spacing*i, 50, 65, 200], 5, 3)

    tube_boxes.append(box)  

  return tube_boxes

   
if __name__ == '__main__':
  main()


