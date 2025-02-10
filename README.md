# 🐍Python Games with turtle graphics 🐢

Install on terminal
```
C:\....\....>pip install turtle
```
Go to proyects!
```python
import turtle
import time
import random
import winsound
```
# Python "tetris" Game 🏆
Легендарная игра от создателя Алексей Пажитнов!
<br>

![https://github.com/dimagutierrez](https://github.com/DimaGutierrez/Python-Games/blob/main/img/python_turtle_tetris.png)
## Settings 💻
Run > `tetris_turtle.py`
<br>
## тетрис controls 🎮
🕹️Move  (← <kbd>A</kbd> ) (→ <kbd>D</kbd> )
<br>
🕹️Rotate = <kbd>space</kbd> 
```python
# Keyboard
wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")
wn.onkeypress(lambda: shape.rotate(grid), "space")
```
<br>

# Space Shooting 🛸...
many functions available here, movements and statistics, graphic animations, sound efects!
```python
import turtle
import random
import winsound
```
<br>

![https://github.com/dimagutierrez](https://github.com/DimaGutierrez/Python-Games/blob/main/img/Space_shooting.jpg)
## Settings 💻
Run > `space_shooting_turtle.py`
the py file and the images must be in the same folder
<br>
## controls 🎮
🕹️Move  (← <kbd>◄</kbd> ) (→ <kbd>►</kbd> ) (↑ <kbd>▲</kbd> ) (↓ <kbd>▼</kbd> )
<br>
🕹️Shooting = <kbd>space</kbd> 
```python
# Keyboard binding
wn.listen()
wn.onkeypress(quit_game, "q")
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.onkeypress(fire_missile, "space")
```
## Sound Efects / misile, explossion
```Ruby
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.fire()
            winsound.PlaySound("SS_missile.wav",winsound.SND_ASYNC)
            break
```
<br>

# ChernoBird ☢️
FlappyBird 
![https://github.com/dimagutierrez](https://github.com/DimaGutierrez/Python-Games/blob/main/img/python_chernobird.png)
## Settings 💻
Run > `cherno_bird.py`
the py file and the images must be in the same folder
<br>
Theme & graphic design Dima Gutierrez
## controls 🎮
🕹️Fly press <kbd>space</kbd>  маленькая птичка летит 🐤
<br>

# Python "Pong" Game 🏓

![https://github.com/dimagutierrez](https://github.com/DimaGutierrez/Python-Games/blob/main/img/python_pong.png)
## Settings 💻
Run > `pong.py`
<br>
## Controls 🎮
🕹️Player A   (↑ <kbd>W</kbd> ) (↓ <kbd>S</kbd> )
<br>
🕹️Player B   (↑ <kbd>▲</kbd> ) (↓ <kbd>▼</kbd> )
```python
# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
```
<br>

# Python "Turtle Race" 🏁

![https://github.com/dimagutierrez](https://github.com/DimaGutierrez/Python-Games/blob/main/img/python_turtle_race.png)
## Settings 💻
Run > `turtle race.py`
```python
from turtle import *
from random import *
import turtle
import time
```
<br>

# Python "tetris" One block version 🟨

![https://github.com/dimagutierrez](https://github.com/DimaGutierrez/Python-Games/blob/main/img/python_turtle_tetris_oneb.png)
## Settings 💻
Run > `tetris_one_block.py`
<br>
## тетрис controls 🎮
🕹️Move  ( ← <kbd>◄</kbd> ) ( → <kbd>►</kbd> )
<br>
## This simple version has a score counter
```python
score_count = 0
score = turtle.Turtle()
score.color('red')
score.up()
score.hideturtle()
score.goto(60,-300)
score.write('Score: 0', align='center', font=('Courier', 24, 'normal'))
```
<br><br>

Visit > discussions/

## Enjoy the games! 🐍
[![Python](https://img.shields.io/badge/Python-0095D5?style=for-the-badge&logo=Python&logoColor=white&labelColor=101010)]()
<br></br>

```python
Visit discussion for more ideas & star my repo! ⭐🚀
https://github.com/DimaGutierrez/Python-Games/discussions
```
![galaxy brain](https://github.com/user-attachments/assets/e4fabfee-b97e-40f2-9df2-89a4e5a17e8c)

<br></br>
