import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 850
SCREEN_TITLE = ""


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("Images/bg.png")
        self.dino = Dino("Images/Dino.png", 1)
        self.cactus = Cactus("Images/cactus.png", 1)
        self.dino.jump = False
        self.score = 0
        self.background2 = arcade.load_texture("Images/Bg2.png")
        self.game_over = False

    def setup(self):
        self.dino.center_x = 50
        self.dino.center_y = 75
        self.cactus.center_x = SCREEN_WIDTH
        self.cactus.center_y = 75
        self.cactus.change_x = 5
        self.dino.change_y = 0

    def on_draw(self):
        arcade.start_render()
        if self.game_over == False:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            self.dino.draw()
            self.cactus.draw()
            score_text = f"Score: {self.score}"
            arcade.draw_text(score_text,100,800,arcade.color.ANTIQUE_WHITE,30)
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background2)
            score_text = f"Score: {self.score}"
            arcade.draw_text(score_text,390,450,arcade.color.ANTIQUE_WHITE,50)

    def update(self, delta_time):
        self.dino.update()
        self.cactus.update()
        if arcade.check_for_collision(self.dino,self.cactus):
            self.dino.stop()
            self.cactus.stop()
            self.game_over = True
        #updating the score on the screen
        if self.cactus.center_x <= 0:
            self.score += 1 

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.dino.jump == False:
            self.dino.change_y = 15
            self.dino.jump = True

    def on_key_release(self, key, modifiers):
        pass


class Dino(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.4
        if self.center_y <= 75:
            self.center_y = 75
            self.jump = False


class Cactus(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
#Homework: create another cactus sprite, and place it a little bit above the first one
