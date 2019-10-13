/*
----------------------------------------------------------------------
                       LIST CONCATENATION
----------------------------------------------------------------------

[X|L1] =   [ X |-------------L1---------------]  [------L2-----]
                       After concatenation:
[X|L3] =   [ X | -------------------L3--------------------------]

Note: X remains as the head of the final list. Concatenation is the 
clause name. The first line of code translates to “if we concatenate 
a an empty list with the list L, then the output list will be L”.  
The second line translates to “if we concatenate a list with head=X1 
and tail=L1 with the list L2, we get a new list with X1=head and L3=tail. 
So after concatenation of lists L1 and L2, the output will be a list L3. 

Example Queries:  concatenation([cat,dog,bear,orca],[snail,beattle,fish],L).
                  concatenation([],[snail,beattle,fish],L].
*/

concatenation([],L,L).
concatenation([X1|L1], L2, [X1|L3]) :- concatenation(L1,L2,L3).



