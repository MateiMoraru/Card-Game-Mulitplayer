import pygame

class Spritesheet(object):
    def __init__(self, filename, size:int=32, total_size:int=320):
        self.size = size #ex 16x16
        
        self.total_size = total_size #128x128

        if not isinstance(self.size, int):
            self.size_w = self.size[0]
            self.size_h = self.size[1]
            self.sprites_no = self.total_size / self.size[0]
            self.unit_size = total_size / size[0]

        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Failed to load spritesheet:', filename)
            print(message)
        print("INFO: Spritesheet loaded correctly")
        

    def image_at(self, rectangle, colorkey = None):

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    

    def image(self, id, colorkey = (0, 0, 0), size=(32, 32)):
        w, h = self.size
        x = (id % (self.sprites_no)) * w
        y = (id // (self.sprites_no)) * h
        image = self.image_at((x, y, w, h), colorkey)
        return pygame.transform.scale(image, size)
    

    def images_at(self, rects, colorkey = (0, 0, 0)):
        return [self.image_at(rect, colorkey) for rect in rects]
    

    def load_strip(self, rect, image_count, colorkey = (0, 0, 0)):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)