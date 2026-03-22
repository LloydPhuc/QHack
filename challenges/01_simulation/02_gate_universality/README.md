# Challenge 02 | Universality of Single-Qubit Gates
===================================================

[ THEORETICAL BACKGROUND ]
Any single-qubit unitary operation $U \in U(2)$ can be expressed using 
four real parameters. This challenge demonstrates the "Universality" 
by training a parameterized matrix $M(\theta)$ to match a target $U$.

[ MATHEMATICAL MODEL ]
The universal rotation is modeled as:
$$M = e^{i\phi} R_z(\beta) R_y(2\alpha) R_z(\gamma)$$
In this implementation, we use a direct element-wise parameterization.

[ OPTIMIZATION STRATEGY ]
+ Optimizer : Vanilla Gradient Descent
+ Loss Function : Frobenius Norm (MSE of complex matrix elements)
+ Framework : PennyLane Autograd (Automatic Differentiation)

