import numpy as np

def initialize_state():
    """Initializes a qubit in the computational basis state |0>."""
    return np.array([1.0, 0.0])

def apply_u(U, state):
    """Applies a unitary matrix U to a quantum state vector."""
    return np.dot(U, state)

def measure_state(state, num_meas):
    """Simulates quantum measurement based on the Born Rule."""
    probs = np.abs(state)**2
    return np.random.choice([0, 1], size=int(num_meas), p=probs)

def quantum_algorithm(U):
    """Executes the full simulation pipeline: Init -> Transform -> Measure."""
    state = initialize_state()
    final_state = apply_u(U, state)
    return measure_state(final_state, 20)
