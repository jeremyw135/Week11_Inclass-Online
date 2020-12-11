import arcade
import Comp151Window
import types
import random

def update(window, delta_time):
    window.player.center_x +=window.playerDx
    window_size = window.get_size()

    if window.player._get_right() > window_size[0] or window.player._get_left() <0:
        window.playerDx = -window.playerDx

def draw(window_being_updated):
    #update(window_being_updated)
    arcade.start_render()
    window_being_updated.player.draw()
    for gold_pile in window_being_updated.goldList:
        gold_pile.draw()

def setup_window(graphicsWindow):
    gold_list= []
    width, height= graphicsWindow.get_size()
    for gold_count in range (6):
        gold_pot = arcade.Sprite("gold-coins-large.png")
        x_pos= random.randint(0,width)
        y_pos= random.randint(0,height)
        gold_pot.set_position(x_pos,y_pos)
        gold_list.append(gold_pot)
    player= arcade.Sprite("galleon.png")
    player.set_position(175,350)
    graphicsWindow.player= player
    arcade.set_background_color(arcade.color.EGYPTIAN_BLUE)
    graphicsWindow.playerDx = 3
    graphicsWindow.goldList = gold_list


def main():
    graphicsWindow= Comp151Window.Comp151Window(1000,700, "Ship Demo")
    setup_window(graphicsWindow)
    graphicsWindow.on_draw =types.MethodType(draw, graphicsWindow)
    graphicsWindow.on_update = types.MethodType(update, graphicsWindow)
    arcade.run()

main()
    

