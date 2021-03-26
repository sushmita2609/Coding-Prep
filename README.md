# Coding-Interview-Prep

1. Binary Array Sorting-

       Input: 
            5
            1 0 1 1 0
            
       Output:
            0 0 1 1 1
            
2.  Sum of numbers in string

        Input:
           str = abc12yu8it4
           
        Output: 24
    
    Explanation: 1 and 23 are numbers in the string which is added to get the sum as 24.

3. check for sum of pair in array

       arr[] = {1, -2, 1, 0, 5}
   
       sum = 0
   
       Input: 1 -2 1 0 5
              0
          
       Output: Array doesnt have two elements with the given sum     Explaination:(No valid pair exists.)

4. Sum of all nodes present in binary tree

             15
            /  \
           6    8
               / \
              3   4
        o/p- 36
              
5. Print the index values of pair which meets the target
           
       i/p- array:  [3,4,11,7]
         
            target:   7
        
            o/p-  0 1    (3+4=7)
            
6. Merge array

         input:  arr1= [1 3 5 7]
         
                 arr2= [0 2 6 8 9]
         
        output:  [0 1 2 3 5 6 7 8 9 ]
     
7. Reverse an array 

         Input: 2
                4
                7 3 4 6
         Output: 6 4 3 7
         
 8. Reversing string without affecting the special characters
         
         Input: a?nm@6
         Output: 6?mn@a
       
 9. Rotate a Linked List
         
         Input:
                N = 5
                value= 2 4 7 8 9
                k = 3
         Output: 8 9 2 4 7
         
 10. Sum of array
 
         Input:3
                4
                8
                9
         Output:
                21
            
11. check string is a Palindrome or not

        Input: mama
        Output: not a palindrome
        
12. Bubble sort (optimal solution)
        
         Input: 89 40 21 42  10  60
         output: 10 21 20 40 42 60 89
         
13. printing the no's in same line without space
         
         Input: 5
         Output: 12345
  
14. Print all the substring which are palindrome within a given string

        Input: clariebobgmama
        Output: bob
                mama

15. Counting no of pairs

         Input: 5
               10 20 50 20 10
         output: 2
        
16. Book problem

          Input: 6 
                 3
          Output: 1
          explaination:  [ |1] [2|3] [4|5] [6|]
                         if started from 1 then it will take only 1 move to reach to 3
                         if started from 6 then it will take 2 moves to reach 3
                         so, minimum moves required are 1 (started from 1)
      
17. Cats and a mouse

        x: Cat A's position
        y: Cat B's position
        z: Mouse C's position
        Input :
                     2
                     1 2 5
                     1 3 2
        Output:   Cat B
                  Mouse C
        explaination: The positions of the cats and mouse are shown below:
                      A--B--C
                      1  2  5
                     Cat B  will catch the mouse first, so we print Cat B on a new line.
         
18. Height of binary tree

              input=   10
                       /\
                     20   11
                     /\    \
                    8  1    3
               output: 3

19. No of paths in matrix

              Input: 3 3
              output: 6
              explaination: 3*3 matrix
                            A B C
                            D E F
                            G H I
                            The possible paths which exists to reach 'I' from 'A' following above conditions are as follows:ABCFI, ABEHI, ADGHI, ADEFI, ADEHI, ABEFI
