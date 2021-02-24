import numpy as np

def process_tab_model_out(Y):
    Y = np.array(Y)
    Tabs = []
    for i in range(Y.shape[1]):
        Tab = np.zeros((6,19), int)
        Tab[0][np.argmax(Y[0][i])] = 1
        Tab[1][np.argmax(Y[1][i])] = 1
        Tab[2][np.argmax(Y[2][i])] = 1
        Tab[3][np.argmax(Y[3][i])] = 1
        Tab[4][np.argmax(Y[4][i])] = 1
        Tab[5][np.argmax(Y[5][i])] = 1
        Tabs.append(Tab)
    return(Tabs)