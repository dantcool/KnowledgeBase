# Concept of Sets in Computer Graphics 

as we know from basic math, the set is a collection of distinct objects. In computer graphics, sets are used to group data elements like points, vectors, or colors. Sets help in defining Boundaries, handling data points, and performing various operations like union, intersection, and difference. 

## Elements and Membership in Sets

In Mathematics and computer graphics, the membership of an element in a set is denoted by the symbol $\epsilon$ or epsilon . For Instance -
$$a \epsilon S$$
the notation means that the element "a" is part of the set S. in computer graphics sets can be represented in a variety of objects, such as points in a 2D or 3D space. 

Common sets are as follows - 

- $R$ - the set of all real numbers
- $R^2$ - the set of all ordered pairs in 2D space
- $R^3$ - the set of all points in 3D space
- $Z$ - the set of integers

## Cartesian products in Sets 
When we talk about sets, there is another concept called the Cartesian product. This is an operation on two sets, denoted as A x B, which results in a set of ordered pairs from set A and set B.

For example if set A contains points on a plane and set B contains colors, the Cartesian product can map each point to a unique color, such as -
$$A *B = (a1,b1),(a2,b2),(a3,b3),...$$
this is particularly useful in texture mapping, where each point on a 3D model is mapped to a color or texture value. 

# Mappings and Functions in Computer Graphics 

From two sets, if we want to find a relation, then it brings the concept of mapping. In computer graphics it has great roles for transforming sets.

A mapping or function assigns elements from one set (the domain) to elements in another set (the co-domain). this can be expressed as - 
$$f:A\rightarrow B$$
this notation means that there is a function f that maps elements of set A to elements of set B. 

![[Pasted image 20260716164630.png]]

In this example set d contains {a,c,e} and D contains {Q,M,R}. for the function $f : d \rightarrow D$
the relation is being made as given in the diagram. 

# Domain and Range 
the term domain is very common in set theory and relation. the domain of a function is the set of all possible input values, and the range is the set of all possible output values. 

For instance, in a mapping where 3D coordinates (x,y,z) are transformed into 2D screen coordinates (u,v) the domain consists of the 3D points, and the range consists of the 2D screen points. the function transforms each 3D point to its 2D equivalent. 


# Inverse Mappings
An inverse mapping $f^-1$ undoes the original function. if $f(a) = b$ then $f^-1(b)=a$
However inverse mappings only exist if each element of B is mapped by exactly one element of A, meaning the function must be bijective (both injective an surjective )

![[Pasted image 20260716182704.png]]

For this function, there is no inverse since it is not bijective function, and M is image of both a and e 

![[Pasted image 20260716182826.png]]

Another example of inverse mapping. Supposes we have the function $f(x) = x^3$ then its inverse would be $f^-1(x)=\sqrt[3]{x}$. This is because f assigns a unique cube to each real number, so we can "undo" the function by taking the cube root 

# Types of mappings 
functions can be categorized based on how they map elements between set

## Injective (One-to-One) function 

a function is injective if no two elements in the domain map to the same element in the target. For example, $f(x) = 2x$ for $x \epsilon Z$ is injective, because each x produces a unique value 
![[Pasted image 20260716184039.png]]

## Surjective (Onto) Function 

A function is surjective if every element in the target has at least one element in the domain mapping to it. For example, $f(x) = x^2$ for $X \epsilon R$ is not surjective onto R, because no real number squared gives a negative result.
![[Pasted image 20260716184230.png]]


## Bijective Function 

a function is bijective if it is both injective and surjective. Bijective functions have inverses, which makes them particularly useful in many mathematical application. 
![[Pasted image 20260716184451.png]]
