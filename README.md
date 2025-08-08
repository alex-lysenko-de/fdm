
# FDM - Finite Difference Method (Wave Equation)

Finite Difference Method (FDM) solver for the one-dimensional wave equation modeling vibrating string dynamics.  
This Python-based simulation provides interactive visualization of string oscillations with multiple selectable initial conditions using Matplotlib.

---

## Abstract

This project numerically solves the classical one-dimensional wave equation using the finite difference method (FDM).  
The wave equation governs the transverse vibrations of a stretched string fixed at both ends.  
Various initial displacement and velocity profiles can be selected to observe different modes of string oscillations.  

The simulation demonstrates wave propagation, reflection at fixed boundaries, and interference patterns inherent to the wave equation.

---

## Methodology

The wave equation is discretized in space and time using a second-order accurate finite difference scheme:  

\[
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
\]

with boundary conditions \( u(0,t) = u(L,t) = 0 \), and specified initial conditions \( u(x,0) \) and \( \frac{\partial u}{\partial t}(x,0) \).

Stability is ensured by respecting the Courant-Friedrichs-Lewy (CFL) condition:  

\[
c \frac{\Delta t}{\Delta x} \leq 1
\]

The solver advances the solution in time using explicit finite difference formulas.

---

## Features

- Multiple selectable initial conditions including sinusoidal, triangular, Gaussian, and localized velocity "hit" profiles.  
- Real-time interactive visualization with Matplotlib animation and GUI buttons to switch initial conditions.  
- Demonstrates fundamental wave phenomena: propagation, reflection, superposition.

---

## Requirements

- Python 3.x  
- numpy  
- matplotlib

Install dependencies via pip if needed:

```bash
pip install numpy matplotlib
````

---

## Usage

Run the simulation script:

```bash
python fdm.py
```

An interactive window will open showing the vibrating string.
Use the buttons to change initial displacement and velocity conditions dynamically.

![img/Screenshot1.png](img/Screenshot1.png)

![img/Screenshot2.png](img/Screenshot2.png)

![img/Screenshot3.png](img/Screenshot3.png)

![img/wave.gif](img/wave.gif)


