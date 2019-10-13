/*
---------------------------------------------------------------
                       LIST PERMUTATIONS
---------------------------------------------------------------

list_permutation is the name of the predicate that we will use 
to get all permutations of a given list. List_permutation([],[]) 
provides for the case of an empty list; the permutation of an empty 
list is an empty list.The definition that follows states that 
“we will delete the item x from the list L to get a new list L1 
which does not contain X, then we call list permutation recursively 
to get the permutations out of L1. The remove function is being used 
to eliminate combinations which have already occurred.

Example Query:  permutation([red,green,blue],X).
*/



remove(X,[X|LIST1],LIST1).
remove(X,[Y|LIST], [Y|LIST1]) :- remove(X,LIST,LIST1).

list_permutation([],[]).
list_permutation(L,[X|P]) :-remove(X,L,L1), list_permutation(L1,P).
