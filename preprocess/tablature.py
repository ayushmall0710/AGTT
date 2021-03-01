import numpy as np

def process_tab_model_out(Y):
    Y = np.array(Y)
    Tabs = []
    Positions = []
    for i in range(Y.shape[1]):
        Tab = np.zeros((6,19), int)
        Pos = [np.argmax(Y[0][i]), np.argmax(Y[1][i]), np.argmax(Y[2][i]), np.argmax(Y[3][i]), np.argmax(Y[4][i]), np.argmax(Y[5][i])]
        Tab[0][Pos[0]] = 1
        Tab[1][Pos[1]] = 1
        Tab[2][Pos[2]] = 1
        Tab[3][Pos[3]] = 1
        Tab[4][Pos[4]] = 1
        Tab[5][Pos[5]] = 1
        Tabs.append(Tab)
        Positions.append("".join(list(map(str, Pos))))
    return (np.array(Tabs), Positions)