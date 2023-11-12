import pygame
import sys

class StartScreen:
    def __init__(self, width, height, title="CodeDiffuse", font_size=60):
        self.width = width
        self.height = height
        self.title = title
        self.font_size = font_size

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        font_path = "../Resources/text/Black_Ops_One/BlackOpsOne-Regular.ttf"

        try:
            self.font = pygame.font.Font(font_path, font_size)
        except(FileNotFoundError):
            self.font = pygame.font.Font(font_path.replace("..","."), font_size)

        #Background Image
        path_background="../Resources/background2.gif"

        try:
            self.background=pygame.image.load(path_background)
        except(FileNotFoundError):
            self.background=pygame.image.load(path_background.replace("..","."))

        self.background = pygame.transform.scale(self.background, (width, height))
    

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (200,192,192))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        return True

            self.screen.blit(self.background, (0, 0))

            self.draw_text(self.title, self.width // 2, self.height // 4)
            self.draw_text("Press SPACE to Start", self.width // 2, (3*(self.height)) // 4)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Example usage
if __name__ == "__main__":
    pygame.init()
    start_screen = StartScreen(800, 600)
    start_screen.run()
