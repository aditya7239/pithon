import matplotlib.pyplot as mp
animals = ['Bada wala gadha','Gadha','Oggy','Bob','Penguin']
candidates = [19,21,16,13,18]
mp.bar(animals,candidates)
mp.title('Animal Species found in AlphaBetaGamma Sanctuary')
mp.xlabel('Animals')
mp.ylabel('Number of specimen')
mp.show()
