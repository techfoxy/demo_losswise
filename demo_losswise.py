import losswise
import time
import random

losswise.set_api_key("B4N1RQR1K")
session = losswise.Session(tag='my_special_lstm', params={'rnn_size': 512}, max_iter=10)
graph = session.graph('loss', kind='min')
for x in range(10):
    train_loss = 1. / (0.1 + x + 0.1 * random.random())
    test_loss = 1.5 / (0.1 + x + 0.2 * random.random())
    graph.append(x,{'train_loss': train_loss, 'test_loss': test_loss})
    time.sleep(1.)
session.done()
