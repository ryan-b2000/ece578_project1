/* Map of Fab Basement 
shortest(1,5,Path,Length).https://www.tutorialspoint.com/prolog_in_artificial_intelligence/artificial_intelligence_graph_structures_and_paths.asp
https://stackoverflow.com/questions/17806614/output-or-input-in-prolog
*/

edge(1,2,22).
edge(2,20,34).
edge(6,21,20).
edge(2,21,22).
edge(21,5,16).
edge(5,22,33).
edge(22,4,24).
edge(2,23,32).
edge(23,3,28).
edge(4,3,42).
edge(6,14,32).
edge(6,13,32).
edge(14,24,20).
edge(24,15,24).
edge(15,17,32).
edge(15,25,36).
edge(25,16,32).
edge(16,13,48).
edge(18,141,16).
edge(13,18,32).
edge(7,19,60).
edge(21,7,24).
edge(19,26,28).
edge(26,12,24).
edge(12,11,72).
edge(11,10,32).
edge(10,9,16).
edge(9,27,28).
edge(27,8,32).
edge(8,1,40).
edge(3,28,38).
edge(28,29,60).
edge(29,31,8). 
edge(29,30,35).
edge(31,32,24).
edge(32,61,20). 
edge(33,61,34).
edge(61,60,24).
edge(60,59,28).
edge(59,58,24).
edge(62,57,24).
edge(58,57,24).
edge(43,62,28).
edge(41,62,16).
edge(62,63,24).
edge(33,51,12).
edge(51,44,25).
edge(51,42,16). 
edge(42,43,46).
edge(43,41,32).
edge(41,40,16). 
edge(40,39,12).
edge(39,36,30).
edge(39,37,12).
edge(37,38,14). 
edge(36,35,34).
edge(35,34,36). 
edge(4,45,13).
edge(45,46,16).
edge(46,47,46). 
edge(47,48,40).
edge(47,49,32).
edge(49,50,26).
edge(52,53,40). 
edge(53,54,48).
edge(54,55,46).
edge(31,55,40). 
edge(50,56,48).
edge(56,17,16).
edge(48,64,14).
edge(64,30,14).
edge(30,34,24).
edge(20,92,8).
edge(92,93,22).
edge(12,73,32).
edge(73,94,28).
edge(73,84,16).
edge(84,80,30).
edge(80,81,32).
edge(80,83,26).
edge(83,76,30).
edge(81,82,22).
edge(76,11,32).
edge(76,103,30).
edge(103,104,12).
edge(103,77,22).
edge(104,105,14).
edge(105,102,28).
edge(102,101,36).
edge(101,87,24).
edge(11,87,29).
edge(87,88,20).
edge(88,89,20).
edge(89,90,22).
edge(90,91,28).
edge(91,27,30).
edge(94,95,14).
edge(94,74,14).
edge(74,130,24).
edge(74,100,24).
edge(95,96,24).
edge(96,97,28).
edge(97,98,30).
edge(97,131,24).
edge(130,131,20).
edge(130,75,16).
edge(75,98,14).
edge(75,99,16).
edge(100,110,28).
edge(110,111,22).
edge(111,86,16).
edge(86,85,26).
edge(84,85,36).
edge(77,78,18).
edge(78,79,24).
edge(79,136,16).
edge(78,132,30).
edge(132,133,40).
edge(133,134,22).
edge(134,135,30).
edge(35,107,12).
edge(107,108,14).
edge(108,109,24).
edge(26,137,34).
edge(137,139,16).
edge(139,140,24).
edge(137,138,32).



/*  
    X and Y are connected with a distance of L
    if an edge exists between X and Y.
    Can be thought of like such: X and Y are 
    the inputs and L is the ouput paramater.
*/
linked(X,Y,L) :- edge(X,Y,L). 

/*
    X and Y are connected with a distance of L
    if an edge exists between Y and X. L is 
    the output paramater.
*/

linked(X,Y,L) :- edge(Y,X,L).

/*
    Paths are comprised of the list of nodes 
    that must be travesed to get from Start to End.
    Stated more clearly, a path from Start to End exists 
    if Start and End are connected by a series of edges.
    Path is the list of all posible paths that satisfy this. 
    [Start] is a new list of the path taken
    
    Inputs for this function can be thought of as Start, End,
    and the ouput as Len.
    
    reverse(input list,result of reversing list).
    
*/
path(Start,End,Path,Len) :-
       walk(Start,End,[Start],Q,Len), 
       reverse(Q,Path).



/*
    walk is defined the collectin of length 
    betweeen the path from End to Start, where End is 
    the head of the list and P is the tail of the list. 
    this tail contains the path that is composed of edges
    
*/ 
walk(Start,End,P,[End|P],L) :- linked(Start,End,L).


/*
+member(c,visited) = C is a member of the list visited: 
C is an intermidiate point along the path
Vited is a list used to ensure that we dont walk in circles.
L is D+L1 because we need to account for the head by adding 1.
*/

walk(Start,End,Visited,Path,L) :-
    linked(Start,C,D),           
    C \== End,
    \+member(C,Visited),  
    walk(C,End,[C|Visited],Path,L1),
    L is D+L1.  



shortest(Start,End,Path,Length) :-
    setof([P,L],path(Start,End,P,L),Set),
    Set = [_|_], % fail if empty
    minimal(Set,[Path,Length]).

minimal([F|R],M) :- min(R,F,M).


/*  [],M,M -> case for finding the min between an empty 
    list and a list M.  Out put is then M.
*/
min([],M,M).
min([[P,L]|R],[_,M],Min) :- L < M, !, min(R,[P,L],Min). 
min([_|R],M,Min) :- min(R,M,Min).

