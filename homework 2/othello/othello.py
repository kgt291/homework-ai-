#-*- coding: cp949 -*-
import gamePlay
import random
from copy import deepcopy

def maxValue(newBoard, alpha, beta, color, depth):
    
    score = float("-inf")
    best = score
    moves = []
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(newBoard, color, (i,j)):
                moves.append((i, j))
    if len(moves) == 0: # ���̻� �� �� �ִ� move�� ���� ��� pass
        return "pass"
    
    if color == "B" : # ���� color ã��
        m = 0
    elif color == "W" :
        m = 1
   
    if gamePlay.gameOver(newBoard) : #game�� �������� �¸��� ����Ǿ��� ���
        return gamePlay.score(newBoard)[m] 
    
    bestMove = moves[random.randint(0,len(moves) - 1)]
    
    for move in moves :
        uBoard = deepcopy(newBoard)
        gamePlay.doMove(uBoard, color, move) 
        if depth == 2 :
            score = gamePlay.score(uBoard)[m] #���� ���� ���
        else :            
            score = minValue(uBoard, alpha, beta, gamePlay.opponent(color), depth) #������� min layer�� �̵�
        if score > best : # ���� ������ ������� ���� �Ǵ� �������� Ŭ ���
            best = score
            bestMove = move
        alpha = max(alpha, score)            
        if score > beta: # ���̻� ū ���� ���� �� �����Ƿ� ����ġ��
            return best   
    if depth == 0 : # ������ action�� ã���� ��
         return bestMove
    else :     # ������ ������ ã���� ��   
         return best    

def minValue(newBoard, alpha, beta, color, depth):
    
    score = float("inf")
    best = score
    moves = []
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(newBoard, color, (i,j)):
                moves.append((i, j))
    if color == "B" : #������� color ã��
        m = 0
    elif color == "W" :
        m = 1
                
    if gamePlay.gameOver(newBoard) : #game�� �������� �¸��� ����Ǿ��� ���
        return gamePlay.score(newBoard)[m]
    
    for move in moves :
        uBoard = deepcopy(newBoard)
        gamePlay.doMove(uBoard, color, move)
        score = maxValue(uBoard, alpha, beta, gamePlay.opponent(color), depth + 1) #���� max layer�� �̵�
        if score < best : # ���� ������ ������� ���� �۾Ҵ� �������� ���� ���
            best = score
        beta = min(beta, score)
        if best < alpha : # �� �̻� ���� ���� ���� �� �����Ƿ� ����ġ��
            return best     
     
    return best
    
def nextMove(board, color, time):
    return maxValue(board, float("-inf"), float("inf"), color, 0) #���� max layer�� �̵�
    
    
