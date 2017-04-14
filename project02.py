"""
Author: Soumana Sylla
Description: This program creates a matching game using the graphics package.
Users click on cards one at a time, to flip them over to find pairs.
"""
from match_graphics import *
from random import seed, shuffle
import random

def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name of the card in
    row i and column j. It is a 5x5 grid comprised of 12 card pairs and one extra card.

    TODO: Takes no parameters and returns cards
    '''
    # seed the random number generator
    seed()



    random.shuffle(images)
    deck = []                           # Contains a deck of 25 cards; there are 12 pairs
    for i in range(len(images) - 1):
        deck.append(images[i])
        deck.append(images[i])
    deck.append(images[-1])
    random.shuffle(deck)

    cards = []
    count = 0

    for i in range(5):
        row = []
        for j in range(5):
            item = deck[count]
            row.append(item)
            count += 1
        cards.append(row)
    return cards




def show_card(win, cards, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.

    TODO: Takes a window, cards, and row i and column j as parameters and return None
    '''

    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_HEIGHT, YMARGIN+CARD_WIDTH)

    x_left = i * 125 + 25
    y_left = j * 125 + 25
    width = 125
    height = 125
    rec_top_left = Point(x_left, y_left)
    rec_bottom_right = Point(x_left + width, y_left + height)
    rectangle = Rectangle(rec_top_left, rec_bottom_right)
    rectangle.setFill('lightGreen')
    rectangle.setOutline('Yellow')
    rectangle.setWidth(5)
    rectangle.draw(win)
    card = Image(Point(x_left + 62.5, y_left + 62.5), cards[j][i])  # Places the images at the center of each rectangle
    card.draw(win)


    return


def hide_card(win, cards, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.

    TODO: Takes a window, cards, and row i and column j as parameters and return None
    '''
    x_left = i * 125 + 25
    y_left = j * 125 + 25
    width = 125
    height = 125
    rec_top_left = Point(x_left, y_left)
    rec_bottom_right = Point(x_left + width, y_left + height)
    rectangle = Rectangle(rec_top_left, rec_bottom_right)
    rectangle.setFill('lightGreen')
    rectangle.setOutline('Yellow')
    rectangle.setWidth(5)
    rectangle.draw(win)

    return



def mark_card(win, cards, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j with a red X.

    This function takes a window, cards, row i and column j as parameters and returns None
    '''
    x_left = i * 125 + 25
    y_left = j * 125 + 25
    width = 125
    height = 125
    top_left_point = Point(x_left, y_left)
    bottom_right_point = Point(x_left + width, y_left + height)
    line = Line(top_left_point, bottom_right_point)
    line.setOutline('red')
    line.setWidth(5)
    line.draw(win)

    top_right_point = Point(x_left + width, y_left)
    bottom_left_point = Point(x_left, y_left + width)
    line = Line(top_right_point, bottom_left_point)
    line.setOutline('red')
    line.setWidth(5)
    line.draw(win)

    return



def get_col(x):
    '''
    Takes the x-coordinate and returns the column.
    It the x coordinate is outside the board, returns -1.

    This functions takes x-coordinate and either return column number or -1

    '''
    column_num = (x - XMARGIN) // (CARD_WIDTH)
    if (0 <= column_num <= 4):
        return column_num
    if x < XMARGIN or x > (BOARD_HEIGHT - XMARGIN):
        return -1


def get_row(y):
    '''
    Takes the y-coordinate and returns the row.
    If it it outside the board, returns -1.

    This functions takes y-coordinate and either return column number or -1
    '''


    row_num = (y - YMARGIN) // (CARD_HEIGHT)
    if (0 <= row_num <= 4):
        return row_num
    if y < YMARGIN or y > (BOARD_WIDTH - YMARGIN):
        return -1



def main():
    '''
    Creates game window, then shuffle cards and places them face down in the grid.
    Accepts clicks on each card and if two images are identical, they will remain face up with an x drawn on it.
    After all pairs are matched the game window will flash different colors.
    '''

    # generate game window
    win = create_board()


    # shuffle the cards
    cards = shuffle_cards()


    # place all the cards, face down
    for i in range(5):
        for j in range(5):
            hide_card(win, cards, i, j)



    # get a mouse click
    pairs = []
    UserClicks = 0
    while True:
        try:
            c_point = win.getMouse()
            x_point = c_point.getX()
            y_point = c_point.getY()
            row_one = int(get_row(y_point))
            col_one = int(get_col(x_point))
            if (col_one, row_one) in pairs:
                continue
            if row_one == -1 or col_one == -1:
                continue
            show_card(win, cards, col_one, row_one)

            if UserClicks == 0:
                row_two = row_one
                col_two = col_one
            UserClicks += 1

            if UserClicks >= 2:

                if row_one == row_two and col_one == col_two:
                    continue
                game_delay(1)   # Pause for 1 second and decide if first pick and the second pick are a match.

                if cards[row_two][col_two] == cards[row_one][col_one]:  # If first and second pick match, leave face up
                    image_one = (col_one, row_one)
                    image_two = (col_two, row_two)
                    pairs.append(image_one)
                    pairs.append(image_two)
                    mark_card(win, cards, col_two, row_two)
                    mark_card(win, cards, col_one, row_one)
                else:
                    hide_card(win, cards, col_one, row_one)
                    hide_card(win, cards, col_two, row_two)
                if len(pairs) == 24:
                    you_won(win, delay = 0.2)  # When all pairs are matched, game ends with the board flashing colors
                    win.close()

                UserClicks = 0
        except GraphicsError:
            sys.exit(-1)



main()
























