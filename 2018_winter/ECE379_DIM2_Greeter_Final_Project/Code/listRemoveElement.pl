/*
----------------------------------------------------
              REMOVING ELEMENT FROM LIST
----------------------------------------------------
When deleting an element from a given list, the 
element can be in one of two places: the head of 
the list or the tail of the list. The first clause 
states “if we want to remove Y  from a list where 
Y is the only element, then after removing Y, the 
resulting list will be an empty list”. The second 
clause states “if we want to remove X from a list, 
where X is the first element of the list, and LIST1 
is the tail of the list, then the resulting list 
LIST1 will only contain the tail elements”.  The 
third cost states “if we want to remove X from the 
list LIST, which has head=Y, then in this case X is 
in the tail of LIST, and the resulting list will be 
LIST1 where Y is still the head and X has been removed 
from the tail.

Example Query:  remove(apple,[apple],X).
                remove(apple,[pear,peach,grape,apple],X).
                remove(apple,[apple,peach,grape,pear],X).

*/

remove(Y,[Y],[]).
remove(X,[X|LIST1],LIST1).
remove(X,[Y|LIST], [Y|LIST1]) :- remove(X,LIST,LIST1).

