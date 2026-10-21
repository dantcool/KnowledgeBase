## Orthogonal 

For a set of vectors to be orthogonal their dot product must equal zero 
for sets greater than 2 all of the dot products of each of the vectors must equal 0 

## Orthonormal
In order for a set to be Orthonormal each vector in the set must have a length of 1

## Basis 
Fastest way to determine if a set is a basis for Rn is to see if the determinant does not equal 0 meaning it is linearly independent 

## Normalization 

Taking each vector and dividing it by its own length 

$$u=\frac{v}{||v||}$$


### Gram-Schmidt Process
Original basis $v_1,v_2,...,v_n$
Orthogonal basis $u_1,u_2,...,u_n$
1. $$u_1=v_1$$
2. $$u_2=v_2-\frac{<v_2,u_1>}{||u_1||}u_1$$
3. $$u_3=v_3-\frac{<v_3,u_1>}{||u_1||}u_1-\frac{<v_3,u_2>}{||u_2||}u_2$$
