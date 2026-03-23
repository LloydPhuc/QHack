Challenge 03 | Mid-Circuit Measurements & Conditional Logic

=============================================================

[ OBJECTIVE ]
Demonstrate the implementation of non-deferred measurements and classical
control flow within a quantum circuit using PennyLane's qml.measure
and qml.cond operators.

[ LOGIC FLOW ]

State Preparation:
Apply $RX(\theta_i)$ to wires 0, 1, and 2 to create initial states.

Mid-Circuit Measurement:
Capture the classical outcomes $m_0, m_1, m_2$ of the first three qubits.

Conditional Unitary Evolution:
Apply rotations to wire 3 based on the classical bits:

If $m_0 = 1 \implies RX(\theta_3)$

If $m_1 = 1 \implies RY(\theta_3)$

If $m_2 = 1 \implies RZ(\theta_3)$

[ KEY CONCEPTS ]

Dynamic Circuits: Circuits where future operations depend on real-time
measurement outcomes.

Deferred Measurement Principle: While most measurements can be pushed
to the end, mid-circuit measurements are essential for hardware
efficiency and error correction protocols.

Hybrid Workflow: Integration of classical boolean logic into
quantum gate sequences.

Status: COMPLETED | Hardware Target: Default Qubit Simulator
