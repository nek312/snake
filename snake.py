from tkinter import * 
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 90
SPACE_SIZE = 25
BODY_PArTS = 20
SNAKE_COLOr = 'green'
FOOD_COLOr = '#FF0000'
BG_COLOr = '#000000'


class Snake:

  def __init__(self):
    self.body_size = BODY_PArTS
    self.coordinates = []
    self.squareas = []

    for i in range(0, BODY_PArTS):
      self.coordinates.append([0, 0])


    for x, y in self.coordinates:
      squarea = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOr, tag='snake')
      self.squareas.append(squarea)



class Food:

  def __init__(self):
    x = random.randint(0, GAME_WIDTH / SPACE_SIZE-1) * SPACE_SIZE
    y = random.randint(0, GAME_HEIGHT / SPACE_SIZE-1) * SPACE_SIZE
    
    self.coordinates = [x, y]

    canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOr, tag="food")



def next_turn(snake, food):

  x, y = snake.coordinates[0]

  if direction == 'up':
    y -= SPACE_SIZE
  elif direction == 'down':
    y += SPACE_SIZE
  elif direction == 'left':
    x -= SPACE_SIZE
  elif direction == 'right':
    x += SPACE_SIZE


  snake.coordinates.insert(0, (x,y))

  squarea = canvas.create_rectangle(x, y, x +SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOr)
  
  snake.squareas.insert(0, squarea)

  if x == food.coordinates[0] and y == food.coordinates[1]:

    global score

    score += 1

    label_1.config(text='Score:{}'.format(score))

    canvas.delete("food")

    food = Food()



  else:
    del snake.coordinates[-1]

    canvas.delete(snake.squareas[-1])

    del snake.squareas[-1]

  if check_collisions(snake):
    game_over()

  else:
    win.after


  win.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
  
  global direction 

  if new_direction == 'left':
    if direction != 'right':
      direction = new_direction
  if new_direction == 'right':
    if direction != 'left':
      direction = new_direction
  if new_direction == 'up':
    if direction != 'down':
      direction = new_direction
  if new_direction == 'down':
    if direction != 'up':
      direction = new_direction


def check_collisions(snake):

  x, y  = snake.coordinates[0]
  
  if x < 0 or x >= GAME_WIDTH:
    return True

  elif y < 0 or y >= GAME_HEIGHT:
    return True

  for body_part in snake.coordinates[1:]:
    if x == body_part[0] and y == body_part[1]:
      return True

  return False

def game_over():
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
                     



win = Tk()

photo = PhotoImage(file='iconpython.png')
win.iconphoto(False, photo)
# win.config(bg='#3d5694')
win.title('Snake')

win.maxsize(500,600)
win.minsize(350,400)
win.resizable(False, False)

score = 0
direction = 'down'
label_1 = Label(win, text='Score:{}'.format(score), font=('consolas', 34))
label_1.pack()

canvas = Canvas(win, bg=BG_COLOr, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

win.update()

win_width = win.winfo_width()
win_height = win.winfo_height()
screen_height = win.winfo_height()
screen_width = win.winfo_width()


win.geometry(f"{win_width}x{win_height}+{120}+{10}")

win.bind('<Left>', lambda event: change_direction('left'))
win.bind('<Right>', lambda event: change_direction('right'))
win.bind('<Up>', lambda event: change_direction('up'))
win.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

win.mainloop()