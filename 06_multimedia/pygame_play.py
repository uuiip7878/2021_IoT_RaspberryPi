import pygame

pygame.init()

pygame.mixer.music.load('R.mp3')

while True:
    cmd = input("play:p, pause:pp, unpause:up, stop:s, quit:q > ")
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    elif cmd == '+':
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)
        print(pygame.mixer.music.get_volume())
    elif cmd == 'q':
        break
    elif cmd == '-':
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.1)
    else:
        print("incorrect cmd")

#pygame.mixer.music.unload()