(From pauls online notes)

## Tangent Lines 

A Tangent line to a function such as f(x) at a point x=a is a line that just touches the line of a graph while being parallel at that point.

![[Pasted image 20260512162806.png]]

The second point where the line crosses the line of the graph is sometimes called a secant line 

Problem Example #1
Find the tangent line to 
$f(x)=15-2x^2$ at x=1

To find the equation of a line we need either two points on the line or a single point on the line and the slope of the line. 

Since we are after a tangent line we do have a point that is on the line. 
The tangent line and the graph of the function MUST touch at x=1 plugging this into our function (1,f(1)) = (1,13) must be on the line 

That is all we know about the tangent line which is the problem. To find the tangent line we need either a second point or the slope of the tangent line. The only reason for needing a second point is to allow us to find the slope of the tangent line. 

starting with our first point which well call P=(1,13) well pick another point that lies on the graph of the function which well call Q = (x,f(x)).

Lets take x=2 so our second point will be Q = (2,7). Figure shown below is the graph of the function, the tangent line and the secant line that connect P and Q

![[Pasted image 20260512180102.png]]

We can see the the secant line and the tangent line are somewhat similar. so the slope of the secant line should be close to the actual slope of the tangent line. We can estimate the slope of the tangent line by using the slope of the secant line which well call m$_{PQ}$ which is 

$m_{PQ} = \frac{(f(2)-f(1)}{2-1} = \frac{7 - 13}{1} = -6$

this isn't super accurate but good enough to use as an estimate of the slope of the tangent line. However a better estimate is possible we can take our x and bring it closer to x=1 instead of x=2 and even take a third value of x even closer and get a better estimate. 

Other words bring our Q closer and closer to P and the slope of our secant line connecting Q and P will get closer to the slope of the tangent line. Visualization below. 

![This graph is similar to the graph above except it is “animated” when viewed with a web browser.  The point P is still (1,13) and the point Q starts at (2,7) and moves along the graph of \(f\left( x \right)\) getting closer and closer to the point P.  As Q moves closer to P the secant line through P and Q also adjusts and starts looking more and more like the tangent line.](https://tutorial.math.lamar.edu/Classes/CalcI/Tangents_Rates_Files/image003.gif)

As Q gets closer and closer to P the secant line starts to look like our tangent line.

in the figure we looked at Q's that were on the right side of P but we can also use Q's that are on the lefts side of P and will receive the same results. Its always important to look on both sides of P because this will not always be the case. 

Now well work on getting an estimation of the slop of the tangent line. TO simplify the process well use a formula for the slope of the line between P and Q, $m_{PQ}$ that will work with any x we plug in. We can get a formula by find the slope between P and Q using the general from of Q = (x,f(x))

$m_{PQ} = \frac{f(x) - f(1)}{x-1} =  \frac{15-2x^2 -13}{x-1} = \frac{2-2x^2}{x-1}$


Now well plug in values of x getting closer and closer to x=1 

| x      | $m_{PQ}$ | x      | $m_{PQ}$ |
| ------ | -------- | ------ | -------- |
| 2      | -6       | 0      | -2       |
| 1.5    | -5       | 0.5    | -3       |
| 1.1    | -4.2     | 0.9    | -3.8     |
| 1.01   | -4.02    | 0.99   | -3.98    |
| 1.001  | -4.002   | 0.999  | -3.998   |
| 1.0001 | -4.0002  | 0.9999 | -3.9998  |

so if we take x's to the right of 1 and approach very close to 1 it appears the slope of the secant lines approach -4 likewise taking x's to the left of 1 and move them closer to 1 the slope of the secant line appear to be approaching -4

we can infer that the slope of the secant lines are approaching -4 as we move towards x=1 so we will estimate that the slope of the tangent line is also -4.

now for the equation of the line that goes through 

(a,f(a))

is given by 

y = f(a)+m(c-a)

Therefore the equation of the tangent line to $f(x) = 15-2x^2$ at x=1 is 

y = 13-4(x-1) = ==-4x+17== 


## Rates of change 



