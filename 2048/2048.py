import random
from maincolors import *
import pygame
from pygame.locals import *
import sys
import numpy as np


class Game2048:
    def __init__(self, difficulty):
        self.weight = 400
        self.height = 400
        self.spacing = 5
        self.difficulty = difficulty
        self.score = 0
        self.colors = normalmode_colors
        self.color_mode = 0
        self.is_over = 0
        self.difficulty_levels = ['Normal', 'Hard', 'Very Hard']

        pygame.init()
        pygame.display.set_caption("2048")
        pygame.font.init()

        self.font = pygame.font.SysFont('franklingothicmedium', 25)
        self.display = pygame.display.set_mode((self.weight + 100, self.height + 200))

        self.matrix = np.zeros((4, 4), dtype=int)
        self.possible_moves = ['u', 'd', 'l', 'r']

    def sum(self, matrix):
        s = 0
        for i in matrix:
            for j in range(len(i)):
                s += i[j]
        return s

    def nightmode_toggle(self):
        self.color_mode = (self.color_mode + 1) % 2
        if self.color_mode == 1:
            self.colors = nightmode_colors
        else:
            self.colors = normalmode_colors

    def is_2048(self):
        result = np.where(self.matrix == 2048)

        if len(result[0]) > 0:
            return True
        return False

    def game_over(self):
        pygame.draw.rect(self.display,
                         (191, 0, 0),
                         pygame.Rect(125, 225, 250, 150),
                         border_radius=8)

        text = self.font.render('GAME OVER!', True, (self.colors['text']))
        text_rect = text.get_rect()
        text_rect.center = (250, 300)
        self.display.blit(text, text_rect)

        text = self.font.render('r - restart', True, (self.colors['text']))
        text_rect = text.get_rect()
        text_rect.center = (250, 330)
        self.display.blit(text, text_rect)

        self.is_over = 1
        pygame.display.flip()

    def over(self):
        old_matrix = self.matrix.copy()
        for move in self.possible_moves:
            self.move(move)
            if not all((self.matrix == old_matrix).flatten()):
                self.matrix = old_matrix
                return False

        return True

    def restart(self):
        self.weight = 400
        self.height = 400
        self.spacing = 5
        self.score = 0
        self.is_over = 0
        self.matrix = np.zeros((4, 4), dtype=int)
        self.play()

    @staticmethod
    def wait_start_key():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        return 's'
                    elif event.key == K_q:
                        return 'q'
                    elif event.key == K_n:
                        return 'n'

    @staticmethod
    def wait_restart_or_quit():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        return 'r'
                    elif event.key == K_q:
                        return 'q'

    def show_menu(self):
        self.menu()
        while True:
            key = self.wait_start_key()
            if key == 'q':
                return True
            if key == 's':
                return False
            if key == 'n':
                self.nightmode_toggle()
                self.menu()

    def menu(self):
        self.display.fill(self.colors['back'])
        menu = self.font.render('Menu', True, (self.colors['text']))
        wasd = self.font.render('w,a,s,d or arrows - move the tiles', True, (self.colors['text']))
        s = self.font.render('s - start/continue', True, (self.colors['text']))
        n = self.font.render('n - night mode on/off', True, (self.colors['text']))
        i = self.font.render('i - show the menu', True, (self.colors['text']))
        q = self.font.render('q - quit', True, (self.colors['text']))

        text_rect = menu.get_rect()
        text_rect.center = (250, 150)
        self.display.blit(menu, text_rect)

        text_rect = wasd.get_rect()
        text_rect.center = (250, 250)
        self.display.blit(wasd, text_rect)

        text_rect = s.get_rect()
        text_rect.center = (250, 280)
        self.display.blit(s, text_rect)

        text_rect = n.get_rect()
        text_rect.center = (250, 310)
        self.display.blit(n, text_rect)

        text_rect = i.get_rect()
        text_rect.center = (250, 340)
        self.display.blit(i, text_rect)

        text_rect = q.get_rect()
        text_rect.center = (250, 370)
        self.display.blit(q, text_rect)

        pygame.display.flip()

    def show_current_step(self):  # 0 - normal colors, 1 - night mode

        self.display.fill(self.colors['back'])

        text = self.font.render('Score : ' + str(self.score), True, (self.colors['text']))
        text_rect = text.get_rect()
        text_rect.center = (250, 75)
        self.display.blit(text, text_rect)

        text = self.font.render('Mode : ' + self.difficulty_levels[self.difficulty], True, (self.colors['text']))
        text_rect = text.get_rect()
        text_rect.center = (250, 110)
        self.display.blit(text, text_rect)

        for i in range(4):
            for j in range(4):
                x = self.matrix[i][j]

                rect_x = j * self.weight // 4 + self.spacing
                rect_y = i * self.height // 4 + self.spacing
                rect_w = self.weight // 4 - 2 * self.spacing
                rect_h = self.height // 4 - 2 * self.spacing

                pygame.draw.rect(self.display,
                                 self.colors[x],
                                 pygame.Rect(rect_x + 50, rect_y + 150, rect_w, rect_h),
                                 border_radius=8)
                if x == 0:
                    continue
                text_surface = self.font.render(f'{x}', True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(rect_x + 50 + rect_w / 2,
                                                          rect_y + 150 + rect_h / 2))
                self.display.blit(text_surface, text_rect)

    @staticmethod
    def wait_key():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_UP or event.key == K_w:
                        return 'u'
                    elif event.key == K_DOWN or event.key == K_s:
                        return 'd'
                    elif event.key == K_LEFT or event.key == K_a:
                        return 'l'
                    elif event.key == K_RIGHT or event.key == K_d:
                        return 'r'
                    elif event.key == K_i:
                        return 'i'
                    elif event.key == K_n:
                        return 'n'
                    elif event.key == K_q:
                        return 'q'

    def insert_new(self, number_of_new):
        number_of_new = number_of_new + self.difficulty * 1
        free_i = list(zip(*np.where(self.matrix == 0)))
        if len(free_i) < number_of_new:
            number_of_new = len(free_i)

        for i in random.sample(free_i, k=number_of_new):
            if random.random() < (0.2 - 0.1 * self.difficulty):
                self.matrix[i] = 4
            else:
                self.matrix[i] = 2

        self.score = self.sum(self.matrix)

    @staticmethod
    def get_sum(current, mirror):
        current_sum = []
        skip = False
        if mirror:
            current = current[::-1]
        current_not_zeros = current[current != 0]
        n = len(current_not_zeros)
        j = 0

        while j < n:
            if skip:
                skip = False
                j += 1
                continue
            if j != n - 1 and current_not_zeros[j] == current_not_zeros[j + 1]:
                new_n = current_not_zeros[j] * 2
                skip = True
            else:
                new_n = current_not_zeros[j]

            current_sum.append(new_n)
            j += 1

        return np.array(current_sum)

    def move(self, key):  # work on current
        for i in range(4):
            current = self.matrix[i, :]  # for left/right gets current line
            if key == self.possible_moves[0] or key == self.possible_moves[1]:
                current = self.matrix[:, i]  # for up/down gets current column

            mirror = False
            if key == self.possible_moves[1] or key == self.possible_moves[3]:
                mirror = True
            current_s = self.get_sum(current, mirror)

            new = np.zeros_like(current)
            new[:len(current_s)] = current_s

            if mirror:
                new = new[::-1]

            if key == self.possible_moves[0] or key == self.possible_moves[1]:
                self.matrix[:, i] = new
            else:
                self.matrix[i, :] = new

        print(self.matrix)
        self.score = self.sum(self.matrix)

    def play(self):
        self.insert_new(2)
        quit = self.show_menu()

        while quit is False:
            self.show_current_step()
            old_matrix = self.matrix.copy()
            pygame.display.flip()

            key = self.wait_key()

            if key == 'q':
                break

            if key == 'n':
                self.nightmode_toggle()
                continue

            if key == 'i':
                quit = self.show_menu()
                continue

            self.move(key)
            print(self.matrix)

            if self.over():
                self.game_over()
                break

            if not all((self.matrix == old_matrix).flatten()):
                self.insert_new(1)

        if self.is_over == 1:
            key = self.wait_restart_or_quit()
            if key == 'r':
                self.restart()


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 2:
        difficulty = int(sys.argv[1])
    else:
        difficulty = 0
    game = Game2048(difficulty)
    game.play()
