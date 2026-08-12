import pygame 
import random 
import copy, sys


pygame.init()

WIDTH, HEIGHT = 550, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Water Fill Game') 

FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 24)

tubes = 10
tube_colors = []
color_choices = ['red', 'orange', 'lightblue', 'darkblue', 'darkgreen', 'pink', 'purple', 'darkgray', 'brown', 'lightgreen', 'yellow', 'white', 'gold', 'cyan'] 

def main():
  win = False
  selected = False
  select_rect = None 
  dest_rect = None
  new_game = True
  while True:
    screen.fill('black') 
    clock.tick(FPS) 
    
    if new_game:
      tubes, tube_colors = generate_start()
      initial_colors = copy.deepcopy(tube_colors)
      new_game = False
      tube_rects = draw_tubes(tubes, tube_colors, select_rect)
    else:
      tube_rects = draw_tubes(tubes, tube_colors, select_rect) 
    win = check_win(tube_colors) 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit() 
      keys = pygame.key.get_just_pressed()
      if keys[pygame.K_SPACE]:
        tube_colors = copy.deepcopy(initial_colors) 
        
      elif keys[pygame.K_RETURN]:
        new_game = True 
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        if select_rect is None:
          for item in range(len(tube_rects)):
            if tube_rects[item].collidepoint(event.pos):
              selected = True
              select_rect = item 
        else:
          for item in range(len(tube_rects)):
            if tube_rects[item].collidepoint(event.pos):
              dest_rect = item 
              tube_colors = calc_move(tube_colors, select_rect, dest_rect) 
              select_rect = None 
        
    
    if win:
      win_text = font.render('You Win :) Press Enter for a new Board', True, 'white') 
      screen.blit(win_text, (50, 265)) 
    restart_text = font.render('Stuck? Space to restart, Enter for new board', True, 'white')
    screen.blit(restart_text, (10,10)) 
        
    pygame.display.update()
    


def generate_start():
  tubes_number = random.randint(10, 13) 
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



def draw_tubes(tubes_num, tube_cols, select_rect):

  tube_boxes = []
  if tubes_num % 2 == 0: 
    tubes_per_row = tubes_num // 2
    offset = False
  else:
    tubes_per_row = tubes_num // 2 + 1
    offset = True

  spacing = WIDTH / tubes_per_row

  for i in range(tubes_per_row):
    for j in range(len(tube_cols[i])):
      pygame.draw.rect(screen, color_choices[tube_cols[i][j]], [5 + spacing*i, 200 - (50 * j), 65, 50], 0, 3)  

    box = pygame.draw.rect(screen, 'green' if select_rect == i else 'blue', [5 + spacing*i, 50, 65, 200], 5, 3)
     
    tube_boxes.append(box)  
  if offset:
    for i in range(tubes_per_row - 1):
      for j in range(len(tube_cols[i + tubes_per_row])): 
        pygame.draw.rect(screen, color_choices[tube_cols[i+ tubes_per_row][j]], [(spacing*0.5) + 10 + spacing * i, 450 - (50*j), 55, 48], 0, 3) 
    
      box = pygame.draw.rect(screen, 'blue', [(spacing*0.5) + 5 + spacing*i, 300, 65, 200], 3, 3) 
      if select_rect == i + tubes_per_row:
        pygame.draw.rect(screen, 'green', [(spacing * 0.5) + 5 + spacing * i, 300, 65, 200], 5, 3)
      tube_boxes.append(box) 
  
  else:
      for i in range(tubes_per_row):
        for j in range(len(tube_cols[i + tubes_per_row])): 
          pygame.draw.rect(screen, color_choices[tube_cols[i+ tubes_per_row][j]], [ 5 + spacing * i, 450 - (50*j), 65, 50], 0, 3) 
      
        box = pygame.draw.rect(screen, 'blue', [5 + spacing*i, 300, 65, 200], 5, 3) 
        if select_rect == i + tubes_per_row: 
          pygame.draw.rect(screen, 'green', [5 + spacing * i, 300, 65, 200], 5, 3)
        tube_boxes.append(box) 
  
  return tube_boxes

  
def calc_move(colors, selected_rect, destination):
  if selected_rect == destination:
    return colors
  chain = True 
  length = 1 
  color_on_top = None
  color_to_move = None
  
  if len(colors[selected_rect]) > 0:
    color_to_move = colors[selected_rect][-1] 
    for i in range(1, len(colors[selected_rect])):
      if chain: 
        if colors[selected_rect][-1 - i] == color_to_move:
          length += 1
        else:
          chain = False 
  
  if len(colors[destination]) < 4:
    if len(colors[destination]) == 0:
      color_on_top = color_to_move 
    else:
      color_on_top = colors[destination][-1] 
  
  if color_to_move is not None and color_on_top == color_to_move:
    for i in range(length):
      if len(colors[destination]) < 4:
        if len(colors[selected_rect]) > 0:
          colors[destination].append(color_on_top) 
        colors[selected_rect].pop(-1) 
  
  return colors


def check_win(colors):
  won = True 
  for i in range(len(colors)):
    if len(colors[i]) > 0:
      if len(colors[i]) != 4:
        won = False 
      else:
        first_color = colors[i][-1]
        for j in range(len(colors[i])): 
          if colors[i][j] != first_color:
            won = False 
  
  return won


if __name__ == '__main__':
  main()


