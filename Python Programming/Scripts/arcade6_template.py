import arcade


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = ""


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("Images/bg.png")
        self.dino = Dino("Images/Dino.png",1)
        self.cactus = Cactus("Images/cactus.png",1)
        self.dino.jump = False
    def setup(self):
        self.dino.center_x = 50
        self.dino.center_y = 75
        self.cactus.center_x = 900
        self.cactus.center_y = 75
        self.dino.change_y = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.dino.draw()
        self.cactus.draw()

    def update(self, delta_time):
        self.dino.update()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.dino.jump == False:
            self.dino.change_y = 12
            self.jump = True

    def on_key_release(self, key, modifiers):
        pass

class Dino(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.5 #We slowly change the dino's speed. So it goes up smoothly and down smoothly.    
        if self.center_y <= 75:
            self.center_y = 75
            self.jump = False

class Cactus(arcade.Sprite):
    def update(self):
        pass
window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
#HOMEWORK: move the cactus to the left side, by changing its center_x, and if cactus center_x < 0, move the cactus back to the right edge. 