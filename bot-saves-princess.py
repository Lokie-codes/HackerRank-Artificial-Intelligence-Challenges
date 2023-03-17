#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    block = [list(row) for row in grid]
    for index, rows in enumerate(block):
        if 'p' in rows:     # Row where princess is present
            # print("Princess is in", index)
            p_index = index
        if 'm' in rows:     # Row where bot is present
            # print("Bot is in ", index)
            m_index = index
    for rows in block:
        if m_index < p_index: # bot is above princess
            m_index += 1 # move bot below
            print('DOWN')
        elif m_index > p_index: # bot is below princess
            m_index -= 1 # move bot above
            print('UP')
        else :  # bot and princess are in same row
            pass
    for rows in block:
        for index, cells in enumerate(rows):
            if 'p' == cells: # princess is in the cell
                p_cell = index # get position of princess
            if 'm' == cells: # bot is in the cell
                m_cell = index  # get position of the bot
    # print("Princess in ", p_cell)
    # print("Bot in", m_cell)
    for rows in block:
        for cells in rows:
            if m_cell > p_cell: # bot is front of princess
                m_cell -= 1 # move bot backward
                print('LEFT')
            elif m_cell < p_cell: # bot is back of princess
                m_cell += 1 # move bot forward
                print('RIGHT')
            else: # bot and princess are in the same cell
                pass # Success
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
