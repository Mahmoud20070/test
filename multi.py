from multiprocessing import process,cpu_count






def test():
    for x in range(1000000): pass
    for z in range(1000000000000): pass
    for a in range(100000000000000000000000):  pass
    for b in range(10000000000000000000000000000000):  pass






ss = process.active_children()



print(ss)