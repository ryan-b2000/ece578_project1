/*
------------------------------------------------------
                 LIST APPEND
------------------------------------------------------
List_memeber(X,[X|_]) states that “X will be a member 
of the list if X is the head element”. Conversely the 
next line states that “X will be a member of the list 
if X belongs to the tail of the list. The line starting 
with list_append(A,T,T) states that “given an item A, 
the list T will be appended to A only if  and only if A 
is not a member of the list T. The result is then 
outputted as the list T”.  The next line then is provided 
as the other option to the line above, ot states that 
“A will remain the head of the list with its tail =TAIL. 

Note the “!” symbol.  This means that is the line with 
list_append(A,T,T) :- list_member(A,T) is true, then 
the line of code following it will not be evaluated. 

Example Query: list_append(apple, [peach, pear,grape],X).
               list_append 

*/


list_member(X,[X|_]).
list_member(X,[_|TAIL]) :- list_member(X,TAIL).

list_append(A,T,T) :- list_member(A,T), !.
list_append(A,TAIL,[A|TAIL]).

