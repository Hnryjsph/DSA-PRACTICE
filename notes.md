# Data Structures
 ## Types of data structures
    1. mutable 
    2. Unmutable

- A data structure models an object

Linear Structure 
- The elements arranged one after the other 
## Examples 
- Arrays
- Queues
- Lists 

## Memory leak
# None linear Structure
- These strutures donot allow traversing the data in one smooth path
### Examples 
- Graphs
- Trees

Ann object has both a state and a behaivour

# Lists and Sets 

- Lists are represented as objects and have inbuilt methods

- Lists are implemented by Arrays or Linked Lists

- Lists that have dynamic size have it beacuse at intialtion the list size is given when the end of the list is reached it is copied and hence increasing the  size

- Sets only hold unique information
- Sets are fast at search (Because it uses harsh tables)
- sets apply the mapping function
- perfomance of sets reduces when data grows beacuse of  Clashing will occur,
- Clashing is when the hashing function returns the same mapping for two different data


# STACKS AND QUEUES

## Stacks 
- uses LIFO
- stack functions 
    - Push ()
    - Pop (Get the top item in the stack and remove it form the stack)
    - IsEmpty
    - isFull
    - Peek (Allows you view the top item without removing it form the stack)

## Queues
- Uses FIFO
- Queue functions 
    - Push ()
    - Pop (Get the top item in the stack and remove it form the stack)
    - IsEmpty
    - isFull
    - Peek (Allows you view the top item without removing it form the stack)

# TREES

- **Node** with no children called leaf nodes
- **Root** - top level node
- **Child** node connected to the root
- **Sibling** nodes have the same parent
- **Path** is a series of connected nodes
- **Depth of node** - How many edges are there from the parent to the root or the longest path
- **Height of nodes** - Refers to the number of edges between the topmost node to the Deepest node 
- **Edge** - is the line connecting two nodes
- **Size of tree**- Refers to how many nodes are there 
- **Left node** is a less value 
- **Right node** is a greated value 
    ## Implemetation of trees
        - Binary Trees
        - B-trees
        - B-plus trees
        - Quad Trees
        - AVL trees
    
    ## Advantages of Using a binary tree
        - Many ways of traversing the data structure
        - can model file systems 

- **Depth First Search** is visting every node in the binary tree from to bottom 
- **Breadth First Search** -  searching every node at the same level before assending to the next   level

-Breadth First you start from the depth to the root
-Depth First you start from the root to the depth

# HASH TABLES
- Has several slots(buckets) to hold key value pairs
- It require a hashing fucntion to determine the correct bucket to put the data into
- Hashing fucntion is any algorithm that is applied to a key to generate a unique number

    ## Hashing function
        - Compression algorithms
        - MD5

- Hash table priotize speed over space and retrieve data in O(1) time 

- used in caches, dictionary

    **clashing** - 
    **Collisons** - if the results of two harshes is the same you get a collison 

    ## solutions to collsions 
        - Where the collsion occurs use linked list at the points of collision
        - Groe the table every time a collsion occurs and increase the complexity of hash fucntion and redistribute the values to new addresses

# HEAPS


# DYNAMIC PRGRAMMING
     - What is the story behind the technique

    ## Climbing stairs
        - Where you a dp table where you use which is an array where each index is a point on the sub problem, where the if the last two sub problem summation gives you the solution to the next two sub problems, but you need to have a base case for the problem

    ## Andrey Grehov

        - Dynamic programming is a technique to solve a certain type of problem

        - for a problem to be solved by DP is has to have some properties 

        - Dp exists tp solve many problems in polynomial time {O(n^c)} instead of exponetial time {O(2^n)}

        - DP is an optimization technqiue 

        - Properties that accept DP 
            - Optimal Substructure
            - Overlapping Subproblems
        
        - A substructure is a subproblem of the main problem

        - When it is possible to break a problem and when the a subproblem can solve the next problem then the problem has optimal substructure 

        - Overlapping subproblem - is when a subproblem is being dependened on by many subproblem


        - DP problems can be used to solve
            - Combinatoric problems 
            - Optimization problems 

        
        - Combinatoric problems answer the question how many
            - Examples
                - how many ways to make a change 
                - how many ways to traverse a graph
                - how many ways to get from point A to B
        
        - Optimization problems - Intrested in finding a strategy which minimizes or maximizes some function

            - Examples
                 -What is the minimum number of steps needed to get from point A to point B
                 - What is the maximum profit gained by buying ans selling a stock
                 - What is the minimum cost to travel from New York to Mumbai 

        DP is an algorthmic technique to solve combinatoric and optimization problems utilizing the fact optimal solution to the overall problem depends on the optimal solution to its overlapping subproblems



# Climbing stair problem

    - Memoization - is where the result of a computation is cached and used latter in the computation

    - Climbing stairs wants to know how many ways to climb to the top,

    - Break down the problem to the goal, the position actions they can take and each action you cann give it a value of 1,

    - Then after that ask your self the question what is the objective, and the objective in this case is to reach the top so how ways from my possble ways can i reach the top, In simple terms when am at my objective,from that point of view how can i reach the objective with the action i have available, then after findout if the relation of the ways follow the rule of sum or the rule of product. 



    - Express the goal as an objective function

    - Objective function is one that you want to minimize or maximize

    - F(i)-the number of steps to reach the ith stair

    - Write an objective function with its definition

    - Break down the problem into small subproblems and identify base case

    - Base Cases
        - F(2) = 2
        - F(1) = 1
        - F(0) = 1 (Is equal to one beacuse there is one way to get to the ith stair by doing nothing)

    - Write down the recurrence relation for the optimized pobjective relation

    - Sometimes you can observe the pattern by solvingthe problem for a few input values

    - F(n) = F(n-1) + F(n-2)

    - It seems that when you go to the top of the stair you find out that the options you have to complete your final task of reaching the top stair are two and you pick scenario where you have only one option to complete you task and find out where in the hirechary you can complete that task and then do that for all actions you have to complete the task and then determine if the actions follow the rule of sum or product annd then each action should be expressed as an action complete to rerach that point in the hireachy


    ## Steps to solve a dp problem

        1. Define objective fucntion
        2. Identify base cases 
            - Base cases ar ethe starting points of the problem
        3. Recurrence Relation
            - It is the transition function that enables youy to move from one sub problem to another
        4. Order of Computation 

            - In order to solve the problem you have start to solve subproblems from some order either from the bottop-up
            or top-down

            - the top/up means the point where you have found the solution

        5. Location of the answer
            - You have to find out where in the sub problem hierachy the solution is, is it in the top or is it in the bottom of the hireachy 

        - Transition function takes the problem from one state to another 


    - **Rule of Sum** - State taht if there are n choices for one action 
    and m choice for another action and the two actions cannot be done at tthe same time then there are n+m ways to choose one of theses adctions

    - **Rule of Product** - If there are n options for doing one thing and m options for doing another thing and they can be done together then the total combinations are nxm
    
        