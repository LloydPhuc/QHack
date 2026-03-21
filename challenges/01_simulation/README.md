# Challenge 01 | My First Quantum Simulation
============================================

[ OBJECTIVE ]
Implement a basic state-vector simulator from scratch using NumPy to 
understand the mathematical foundations of quantum operations before 
utilizing high-level frameworks like PennyLane.

[ MATHEMATICAL FORMULATION ]
1. State Initialization:
   The system starts in the ground state |0>, represented as:
   $$|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

2. Unitary Evolution:
   Quantum gates are represented by Unitary matrices $U$. The state evolution 
   is computed via matrix-vector multiplication:
   $$|\psi_{out}\rangle = U |\psi_{in}\rangle$$

3. Measurement (Born Rule):
   The probability of observing outcome $i$ is given by the square of the 
   probability amplitude:
   $$P(i) = |\langle i | \psi \rangle|^2$$

[ IMPLEMENTATION NOTES ]
+ Uses `np.dot` for linear transformations.
+ Implements stochastic sampling using `np.random.choice` based on the 
  calculated probability distribution.
+ Optimized for 2-dimensional Hilbert space (Single Qubit).

--------------------------------------------
Status: COMPLETED (Passed all public test cases)
