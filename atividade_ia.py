import pygame.display as display
import pygame.event as pygame_event
import pygame.draw as draw
import pygame


pygame.init()
screen = display.set_mode((800, 600))
size_selector = pygame.image.load("size_selector.png").convert()
plus_button = pygame.image.load("plus_button.png").convert()
minus_button = pygame.image.load("minus_button.png").convert()
ok_button = pygame.image.load("ok_button.png").convert()
selector_rect = size_selector.get_rect()
plus_rect = plus_button.get_rect()
minus_rect = minus_button.get_rect()
ok_rect = ok_button.get_rect()
selector_rect.left = 304
selector_rect.top = 206
plus_rect.left = 432
plus_rect.top = 206
minus_rect.left = 432
minus_rect.top = 270
ok_rect.top = 334
ok_rect.left = 336
array_size_font = pygame.font.SysFont('ubuntu', 80)
array_size = 2
key_up = True
is_on_menu = True
adjacency_matrix = []
graph = []



def is_button_pressed(button):
    global key_up
    if button:
        if key_up:
            key_up = False
            return(True)
        else:
            return(False)
    else:
        key_up = True
        return(False)

def menu(mouse_pos, is_mouse_pressed):
    global is_on_menu
    global array_size

    screen.blit(size_selector, selector_rect)
    screen.blit(minus_button, minus_rect)
    screen.blit(plus_button, plus_rect)
    screen.blit(ok_button, ok_rect)
    screen.blit(array_size_font.render(str(array_size), True, (0, 0, 0)), (349, 221))

    if(is_mouse_pressed and plus_rect.collidepoint(mouse_pos)):
        if(array_size < 6):
            array_size += 1
    if(is_mouse_pressed and minus_rect.collidepoint(mouse_pos)):
        if(array_size > 2):
            array_size -= 1
    if(is_mouse_pressed and ok_rect.collidepoint(mouse_pos)):
        is_on_menu = False

def create_graph():
    global adjacency_matrix
    global graph
    for i in range(array_size):
        graph.append([])
        for j in range(array_size):
            graph[i].append(j+array_size*i)
    print(graph)
    for i in range(array_size):
        for j in range(array_size):
            print(i)<
            


def draw_graph():
    pass


def main():   
    global is_on_menu
    running = True
    mouse_state = (False, False, False)
    mouse_button_down = False
    mouse_pos = (0,0)
    
    while is_on_menu:
        for event in pygame_event.get():
            mouse_pos = pygame.mouse.get_pos()
            mouse_state = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                running = False
                is_on_menu = False
        mouse_button_down = is_button_pressed(mouse_state[0])
        screen.fill((200, 200, 200))
        menu(mouse_pos, mouse_button_down)
        display.flip()
    create_graph()
    while running:
        for event in pygame_event.get():
            mouse_pos = pygame.mouse.get_pos()
            mouse_state = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                running = False
        mouse_button_down = is_button_pressed(mouse_state[0])
        screen.fill((200, 200, 200))
        draw_graph()
        display.flip()  

if __name__ == "__main__":
    main()