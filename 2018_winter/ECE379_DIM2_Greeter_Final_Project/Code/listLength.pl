/*
 In this code the predicate “list_length” is used to calculate 
 the number of elements in a given list.  List_length([],0) is 
 used for the case of an empty list, while the second rule is 
 used for all lsits that are not equal to zero.  The variable 
 L represents the total length of the list of elements. The 
 final value of L1 is then added to L to account for the extra 
 element present in the head of the list. 

Example queries: list_length([],L).
               : list_lenght([dog,cat,bear,orca],L).
*/


list_length([], 0).
list_length([_|Tail],L) :- 
        list_length(Tail,L1),
        L is L1 +1.

