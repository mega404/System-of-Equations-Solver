# System-of-Equations-Solver
We use different methods to solve equations

## Phase 1
### Overview
We implemented methods used for solving system of linear equations:
- Gauss Elimination.
- Gauss Jordan.  
- LU Decomposition.
- Gauss Seidil.
- Jacobi Iteration.

  
### Description
Implemented linear system of equation program which takes as
an input system of linear equations, the method to use and its required
parameters if exists for this method.


### Specification
Implemented an interactive GUI application the does the following:
1. Accepts an input for a system of linear equations:
a. The equations can be of any format.
c. Number of variables must equal the number of equations.
d. Coefficients must be numbers (0 or non-existing is allowed).
2. Choose any of the previously mentioned methods to solve the given equation via
a drop-down list.
3. Parameters -if it applicable for the chosen solving method
4. A way to enter the precision. (If user chooses not to provide it, a default value must be applied)
5. A Solve button to display the output if exists, a the run time must be displayed.
6. Always apply partial pivoting if applicable.

The following table summarizes the required methods and their input parameters:
 
| Method                | Input                      | Parameters |
| -------------         |:-------------:             | :-----    |
| Gauss Elimination     | System of Linear Equations | None       |
| Gauss-Jordan          | System of Linear Equations | None |
| LU Decomposition      | System of Linear Equations |Drop-down list for the format of L & U: <ul><li> Downlittle Form </li><li>Crout Form</li><li>Cholesky Form</li><li>Initial Guess</li></ul>|
| Gauss-Seidil          | System of Linear Equations | <ul><li> Initial Guess </li><li> Stopping Condition:<ul><li> Number of Iterations </li><li> Absolute Relative Error </li></ul></li></ul>|
| Jacobi-Iteration      | System of Linear Equations | <ul><li> Initial Guess </li><li> Stopping Condition:<ul><li> Number of Iterations </li><li> Absolute Relative Error </li></ul></li></ul>|

link of demo video [here](https://youtu.be/umC4FxwZ_PA)

## Phase 2
### Overview
We implemented methods used for calculating the roots of equations:
- Bisection
- False-Position
- Fixed point
- Newton-Raphson
- Secant Method.

### Description
Implemented a root finder program which takes as an input the
equation, the technique to use and its required parameters (e.g. interval for the
bisection method).

### Specification
built upon the GUI application of phase 1, to include the following:
1. Accepts a free-text input for a non-linear equation:
a. The equations containing different function: {poly, exp, cos, sin}.
b. The variable used is “x”
2. plot of the function with the boundary functions in case of bisection
and false position, g(x) with y = x in case of fixed point, f’(x) in the remaining
cases.
3. Choose any of the previously mentioned methods to solve the given equation via
a drop-down list.
4. Parameters, if it applicable for the chosen solving method.
5. A way to enter the precision (Number of significant figures), EPS and the max
number of iterations otherwise default values are used; Default #SFs = System
Default, Default Epsilon = 0.00001, and Default Max Iterations = 50.
6. A Solve button to display the output if exists, the run time must be displayed.


## Team
- Ahmed Hisham
- Abdelrahman Yousry
- Salah Eltenehy
- Mahmoud Gad
