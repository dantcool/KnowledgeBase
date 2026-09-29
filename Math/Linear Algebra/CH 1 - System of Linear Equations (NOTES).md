# 1.1-INTRODUCTION TO SYSTEMS OF LINEAR EQUATIONS 

- RECOGNIZE A LINEAR EQUATION IN N VARIABLES 
- FOND A PARAMETRIC REPRESENTATION OF A SOLUTION SET 
- DETERMINE WETHER A SYSTEM OFLINEAR EWAUTONS IS CONSISTEN OR INCONSISTENT
- USE BACK SUBSTITUTION AND GAUSSIAN ELIMINATION TO SOLVE A SYSTEM OF LINEAR EQUATIONS
## Definition of a linear Equation in n Variables
a linear equation in n variables such as $x_1,x_2,x_3...x_n$ has the form $a_1x_1+a_2x_2+a_3x_3+...+a_nx_n=b$
where the coefficients a are real number and the constant term b is a real number the first a is the leading coefficient and the first x is the leading variable. 

## Linear and Nonlinear equations 
Linear equations have no products or roots of variables and no variables involved in trigonometric, exponential, or logarithmic function. Variable appear only to the first power 

#### EXAMPLES

LINEAR EQUATIONS
a.$3x+2y=7$              b.$\frac{1}{2}x+y-\pi z=\sqrt{2}$            c.$(sin \pi)x_1-4x_2=e^2$

NON LINEAR EQUATIONS 
a.$xy+z=2$                b.$e^x-2y=4$                       c.$sinx_1+2x_2-3x_3=0$

## Solutions and Solution Sets 
A solution of a linear equation in n variable is a sequence of n real numbers such as $s_1,s_2,s_3...s_n$ that satisfy the equation when you substitute the values. 
$x_1=s_1,x_2=s_2,x_3=s_3,..., x_n=s_n$ For Example in the equation $x_1+2x_2=4$ a solution to this equation could be $x_1=2,x_2=1$ but some other solutions could be $(x_1=-4,x_2=4),(x_1=0,x_2=2),(x_1=-2,x_2=3)$. The set of ALL solutions of a linear equation is called its **solution set** and when found you have **solved** the equation. In order to describe the entire solution set of a linear equation we us a ==**PARAMETRIC REPRESENTATION**==. (Examples Below)

#### EXAMPLES 
1.$x_1+2x_2=4$ 
**Two variable equation** you solve for one term in terms of the other variable letting the other be a **free** variable which means that it can take on any real value. 

$x_1=4-2x_2$

$x_1$ here would not be a free because it is dependant on what value is assigned to $x_2$. To represent the infinetley many solutions of this equation we introduce a thir variable $t$ called a **parameter**. Letting $x_2=t$ the solution can be represented as 

$x_1=4-2t, x_2=t$  t being any real number. 

Then to obtain solutions we assign values to the parameter t  such as. $t=1$ gives us $(x_1=2)(x_2=1)$. And when $t=4$ we get $(x_1=-4)(x_2=4)$ 

Another way to parametrically represent the solutions of this example would be to have chose $x_1$ as the free variable leading to the parametric solution set looking like this.

$(x_1=s)(x_2=2-\frac{1}{2}s)$ where s is any real number. 

2.$3x+2y-z=3$
**Three variable equation** same process except you have 2 **free** variables that can take on any real values. 

$$3x=3-2y+z$$
$$x=1-\frac{2}{3}y+\frac{1}{3}z$$
Remembering that we use $t$ or $s$ for parameters we let $y=s$ and $z=t$, we then obtain the parametric representation 

$$x=1-\frac{2}{3}s+\frac{1}{3}t,(y=s)(z=t)$$
Two particular solutions are $(x=1),(y=0),(z=0)$ and $(x=1),(y=1),(z=2)$




## Homogenoues Systems of Linear Equations
A ssytem of linear eqautions is said to be **Homogeneous** if it is of the form

$$a_{11}x_1+a_{12}x_2+...+a_mx_n=0$$
$$a_{21}x_1+a_{22}x_2+...+a_{2n}x_n=0$$
in words if all the coeffecients on the right side are zero. 

They can have trivial or non-trivial solutions.

the solution (0,0) is the trivial solution 

