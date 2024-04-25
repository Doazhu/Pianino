import pygame
import sys

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)


width, height = 800, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Виртуальное пианино")

white = (255, 255, 255)
black = (0, 0, 0)
grey = (200, 200, 200)

notes = {
    pygame.K_a: pygame.mixer.Sound('1.mp3'),
    pygame.K_w: pygame.mixer.Sound('2.mp3'),
    pygame.K_s: pygame.mixer.Sound('3.mp3'),
    pygame.K_e: pygame.mixer.Sound('4.mp3'),
    pygame.K_d: pygame.mixer.Sound('5.mp3'),
    pygame.K_f: pygame.mixer.Sound('6.mp3'),
    pygame.K_t: pygame.mixer.Sound('7.mp3'),
    pygame.K_g: pygame.mixer.Sound('8.mp3'),
    pygame.K_y: pygame.mixer.Sound('9.mp3'),
    pygame.K_h: pygame.mixer.Sound('10.mp3'),
    pygame.K_u: pygame.mixer.Sound('11.mp3'),
    pygame.K_j: pygame.mixer.Sound('12.mp3')
}

keys = [
    {"rect": pygame.Rect(x * 67, 0, 65, 200), "color": white, "note": note}
    for x, note in enumerate(notes.values())
]

def draw_keys():
    for key in keys:
        pygame.draw.rect(screen, key["color"], key["rect"])
        pygame.draw.rect(screen, black, key["rect"], 3)

def play_notes():
    keys_to_play = [key for key in pygame.key.get_pressed() if key in notes]
    for key in keys_to_play:
        notes[key].play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for key in keys:
                if key["rect"].collidepoint(event.pos):
                    key["color"] = grey
                    key["note"].play()
        elif event.type == pygame.MOUSEBUTTONUP:
            for key in keys:
                key["color"] = white
        elif event.type == pygame.KEYDOWN:
            if event.key in notes:
                notes[event.key].play()

    screen.fill(black)
    draw_keys()
    pygame.display.flip()

pygame.quit()
sys.exit()
