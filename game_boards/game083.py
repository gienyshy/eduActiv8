# -*- coding: utf-8 -*-

import os
import pygame
import random

import classes.board
import classes.extras as ex
import classes.game_driver as gd
import classes.level_controller as lc


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self, mainloop, 5, 11)
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 10, 7)

    def create_game_objects(self, level=1):
        self.vis_buttons = [1, 1, 1, 1, 1, 0, 1, 0, 0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        # s = random.randrange(30, 80)
        # v = random.randrange(200, 255)
        h = 230  # random.randrange(0, 255)
        color1 = (255, 255, 255)
        # color2 = ex.hsv_to_rgb(h,150,v)
        color3 = ex.hsv_to_rgb(h, 150, 75)

        self.correct = False
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # data = [0-x_count, 1-y_count, 2-bottom_range1, 3-top_range1, 4-bottom_range2, 5-top_range2, 6-operator, 7-font_size]

        if self.mainloop.m.game_variant == 0:
            self.level.lvl_count = 11
            if self.level.lvl == 1:  # addition - ch0
                data = [20, 14, 1, 5, 1, 5, "+", 2]
            elif self.level.lvl == 2:
                data = [20, 14, 3, 9, 1, 5, "+", 2]
            elif self.level.lvl == 3:
                data = [20, 14, 5, 15, 3, 9, "+", 2]
            elif self.level.lvl == 4:
                data = [20, 14, 5, 15, 5, 15, "+", 2]
            elif self.level.lvl == 5:
                data = [20, 14, 15, 55, 5, 35, "+", 2]
            elif self.level.lvl == 6:
                data = [20, 14, 35, 75, 15, 25, "+", 2]
            elif self.level.lvl == 7:
                data = [20, 14, 55, 99, 55, 99, "+", 2]
            elif self.level.lvl == 8:
                data = [20, 14, 100, 250, 100, 250, "+", 4]
            elif self.level.lvl == 9:
                data = [20, 14, 300, 500, 250, 499, "+", 4]
            elif self.level.lvl == 10:
                data = [20, 14, 400, 650, 150, 349, "+", 4]
            elif self.level.lvl == 11:
                data = [20, 14, 500, 850, 100, 149, "+", 4]
        elif self.mainloop.m.game_variant == 1:
            self.level.lvl_count = 11
            if self.level.lvl == 1:  # subtraction  - ch1
                data = [20, 14, 3, 10, 1, 0, "-", 2]
            elif self.level.lvl == 2:
                data = [20, 14, 5, 10, 3, 0, "-", 2]
            elif self.level.lvl == 3:
                data = [20, 14, 10, 15, 3, 0, "-", 2]
            elif self.level.lvl == 4:
                data = [20, 14, 15, 20, 5, 0, "-", 2]
            elif self.level.lvl == 5:
                data = [20, 14, 20, 49, 9, 0, "-", 2]
            elif self.level.lvl == 6:
                data = [20, 14, 49, 99, 9, 0, "-", 2]
            elif self.level.lvl == 7:
                data = [20, 14, 100, 250, 30, 0, "-", 4]
            elif self.level.lvl == 8:
                data = [20, 14, 100, 250, 30, 0, "-", 4]
            elif self.level.lvl == 9:
                data = [20, 14, 100, 250, 30, 0, "-", 4]
            elif self.level.lvl == 10:
                data = [20, 14, 250, 499, 50, 0, "-", 4]
            elif self.level.lvl == 11:
                data = [20, 14, 499, 999, 99, 0, "-", 4]
        elif self.mainloop.m.game_variant == 2:
            self.level.lvl_count = 7
            if self.level.lvl > 7:
                self.level.lvl = 7
            if self.level.lvl == 1:  # multiplication  - ch2
                data = [20, 14, 1, 3, 1, 3, "*", 2]
            elif self.level.lvl == 2:
                data = [20, 14, 1, 9, 1, 2, "*", 2]
            elif self.level.lvl == 3:
                data = [20, 14, 2, 6, 2, 6, "*", 2]
            elif self.level.lvl == 4:
                data = [20, 14, 2, 7, 3, 7, "*", 2]
            elif self.level.lvl == 5:
                data = [20, 14, 2, 9, 2, 9, "*", 2]
            elif self.level.lvl == 6:
                data = [20, 14, 2, 15, 2, 15, "*", 4]
            elif self.level.lvl == 7:
                data = [20, 14, 2, 20, 2, 20, "*", 4]
        elif self.mainloop.m.game_variant == 3:
            self.level.lvl_count = 7
            if self.level.lvl > 7:
                self.level.lvl = 7
            if self.level.lvl == 1:  # division - ch3
                data = [20, 14, 1, 3, 1, 3, "/", 2]
            elif self.level.lvl == 2:
                data = [20, 14, 1, 9, 1, 2, "/", 2]
            elif self.level.lvl == 3:
                data = [20, 14, 2, 6, 2, 6, "/", 2]
            elif self.level.lvl == 4:
                data = [20, 14, 2, 7, 3, 7, "/", 2]
            elif self.level.lvl == 5:
                data = [20, 14, 2, 9, 2, 9, "/", 2]
            elif self.level.lvl == 6:
                data = [20, 14, 2, 15, 2, 15, "/", 4]
            elif self.level.lvl == 7:
                data = [20, 14, 2, 20, 2, 20, "/", 4]
        # stretch width to fit the screen size
        data[0] = self.get_x_count(data[1], even=True)
        if data[0] < 20:
            data[0] = 20
        self.data = data

        self.layout.update_layout(data[0], data[1])
        scale = self.layout.scale
        self.board.level_start(data[0], data[1], scale)

        self.num_list = []
        self.num_list2 = []

        if data[6] == "+":
            first_num = random.randrange(data[2], data[3] + 1)
            second_num = random.randrange(data[4], data[5] + 1)
            self.solution = first_num + second_num

        elif data[6] == "-":
            first_num = random.randrange(data[2], data[3] + 1)
            second_num = random.randrange(data[4], first_num - 1)
            self.solution = first_num - second_num

        elif data[6] == "*":
            first_num = random.randrange(data[2], data[3] + 1)
            second_num = random.randrange(data[4], data[5] + 1)
            self.solution = first_num * second_num

        elif data[6] == "/":  # reversed multiplication - looking for the first factor
            first = random.randrange(data[2], data[3] + 1)
            second_num = random.randrange(data[4], data[5] + 1)
            first_num = first * second_num
            self.solution = first

        self.num_list.append(first_num)
        self.num_list2.append(second_num)

        # create objects
        if data[6] == "*":
            operator = chr(215)
        elif data[6] == "/":
            operator = chr(247)
        else:
            operator = data[6]

        x = (data[0] - 12) // 2
        y = 1
        i = 0

        scheme = "white"
        if self.mainloop.scheme is not None:
            if self.mainloop.scheme.dark:
                scheme = "black"
                img_bg_col = (0, 0, 0)
        img_src0 = os.path.join("schemes", scheme, "robot0.png")
        img_src1 = os.path.join("schemes", scheme, "robot1.png")

        self.board.add_unit(x, y, 5, 5, classes.board.Label, str(self.num_list[i]), color1, "", 21)
        self.board.add_unit(x + 5, y, 2, 5, classes.board.Label, operator, color1, "", 21)
        self.board.add_unit(x + 7, y, 5, 5, classes.board.Label, str(self.num_list2[i]), color1, "", 21)

        self.board.add_unit(x - 4, y, 4, 5, classes.board.ImgShip, "", color1, img_src0)
        self.board.add_unit(x + 7 + 5, y, 4, 5, classes.board.ImgShip, "", color1, img_src1)

        # adding the edit field for the asnwer
        self.board.add_unit(x + 3, y + 6, 6, 2, classes.board.Letter, "", color1, "", 21)
        self.home_square = self.board.ships[-1]
        self.home_square.immobilize()
        self.home_square.set_outline(color3, 5)

        for each in self.board.units:
            each.font_color = color3
        for each in self.board.ships:
            each.font_color = color3

    def handle(self, event):
        gd.BoardGame.handle(self, event)  # send event handling up
        if self.show_msg == False:
            if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN and not self.correct:
                lhv = len(self.home_square.value)
                self.changed_since_check = True
                if event.key == pygame.K_BACKSPACE:
                    if lhv > 0:
                        self.home_square.value = self.home_square.value[0:lhv - 1]
                else:
                    char = event.unicode
                    if (len(char) > 0 and lhv < 5 and char in self.digits):
                        self.home_square.value += char
                self.home_square.update_me = True
                self.mainloop.redraw_needed[0] = True

            elif event.type == pygame.MOUSEBUTTONUP:
                self.home_square.update_me = True
                if self.board.active_ship == self.home_square.unit_id:
                    self.home_square.perm_outline_width = 5
                    self.home_square = self.ans_h
                    self.board.active_ship = self.home_square.unit_id
                self.home_square.update_me = True
                self.mainloop.redraw_needed[0] = True

    def update(self, game):
        game.fill((255, 255, 255))
        gd.BoardGame.update(self, game)  # rest of painting done by parent

    def check_result(self):
        correct = True
        if len(self.home_square.value) > 0 and int(self.home_square.value) == self.solution:
            self.level.next_board("")
        else:
            self.home_square.value = ""
            self.home_square.update_me = True
