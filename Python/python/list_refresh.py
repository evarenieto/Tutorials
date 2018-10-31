>> cosas_chulas = ['purpurina', 'helados', 'banana']
>>> cosas_chulas
['purpurina', 'helados', 'banana']
>>> cosas_chulas + ['alpacas']
['purpurina', 'helados', 'banana', 'alpacas']
>>> cosas_chulas
['purpurina', 'helados', 'banana']
>>> cosas_chulas += ['bananas']
>>> cosas_chulas
['purpurina', 'helados', 'banana', 'bananas']
>>> cosas_chulas.append(["no se que saldrá"])
>>> cosas_chulas
['purpurina', 'helados', 'banana', 'bananas', ['no se que saldrá']]
>>> del cosas_chulas[-1]
>>> cosas_chulas
['purpurina', 'helados', 'banana', 'bananas']
>>> cosas_chulas.append("no se que saldrá")
>>> cosas_chulas
['purpurina', 'helados', 'banana', 'bananas', 'no se que saldrá']
>>> cosas_chulas.extend(["ponis"])
>>> cosas_chulas
['purpurina', 'helados', 'banana', 'bananas', 'no se que saldrá', 'ponis']
>>> a = [1,2,3,]
>>> a.extend('abc')
>>> a
[1, 2, 3, 'a', 'b', 'c']
>>> del cosas_chulas[1]
>>> cosas_chulas
['purpurina', 'banana', 'bananas', 'no se que saldrá', 'ponis']
>>> del cosas_chulas[2]
>>> cosas_chulas
['purpurina', 'banana', 'no se que saldrá', 'ponis']
>>> we used insert() to add items in a specific order. Let´s
see:
>>> cosas_chulas.insert(0, 'pelota')
>>> cosas_chulas = ['hola', 'adios']
>>> cosas_chulas
['hola', 'adios']
>>> cosas_chulas.insert(0, 'hasta luego')
>>> cosas_chulas
['hasta luego', 'hola', 'adios']


##remove and del

>>> books = [1,2,3,4,5]
>>> books
[1, 2, 3, 4, 5]
>>> del books[2]
>>> books
[1, 2, 4, 5]
>>> books.remove(4)
>>> books
[1, 2, 5]
