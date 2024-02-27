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