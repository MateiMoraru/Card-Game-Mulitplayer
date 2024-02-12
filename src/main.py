import time
import pygame
from spritesheet import Spritesheet
from window import Window
from environment import Environment
from text import FloatingText, Text

# GAME STATES
MAINMENU = 0
INGAME = 1
INVENTORY = 2
CRAFTING = 3
DIED_MENU = 4

class Main:
    def __init__(self):
        start = time.time()
        print("INFO: Initialising pygame...")
        pygame.init()
        print("INFO: Initialising window...")
        self.window = Window(size=(1200, 800), fps=0, window_title="Minicraft")
        self.window.set_color((54, 54, 54))
        print("INFO: Loading fonts...")
        self.font = pygame.Font("assets/font.ttf", 30)
        self.font2 = pygame.Font("assets/font.ttf", 15)
        print("INFO: Loading spritesheets...")
        self.spritesheet = Spritesheet("assets/spritesheet.png", (16, 28), 80)
        print("INFO: Initialising environment...")
        self.environment = Environment(self.window, self.spritesheet, self.font)
        print(f"Done! (Everything loaded correctly in {round((time.time() - start) * 1000, 2)}ms)")

        self.running = True


    def run(self):
       # try:
        self.loop()
        self.quit(0)
        #except Exception as e:
        #    print(f"Encountered error: {e}")
        #    self.quit(-1)


    def loop(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.quit()
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_END:
                        self.quit()

            self.draw()
        

    def draw(self):
        self.window.draw_start()

        for i in range(0, 9):
            self.window.get().blit(self.spritesheet.image(i), (i * 50 + 100, 100))
        
        Text(self.font, f"FPS: {self.window.get_fps()}", (0, 0, 0), (0, 0)).draw(self.window.get())
        self.window.draw_end()



    def quit(self, code:int=0):
        print(f"Exited program with exit code: {code}")
        self.window.quit()
        pygame.quit()
        quit()


if __name__ == "__main__":
    main = Main()
    main.run()