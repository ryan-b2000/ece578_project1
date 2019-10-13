from pyswip import Prolog
dest = input()
prolog = Prolog()
prolog.consult("fabBasementMap.pl")

for res in prolog.query("shortest(1,"+x,"Path,Length)."):
    print(res)

    # output:
   # {'X': [1, 2, 3, 4, 5]}
