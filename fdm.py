# FDM - String oscillations

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

# ------------------- PARAMETER -------------------
L = 1.0       # Länge der Saite
c = 1.0       # Wellengeschwindigkeit
nx = 100      # Anzahl der Punkte im Raum
dx = L / nx
x = np.linspace(0, L, nx+1)

dt = 0.001    # Zeitschritt
T = 2         # Gesamte Simulationszeit
nt = int(T / dt)

courant = c * dt / dx
if courant > 1:
    raise ValueError("Courant-Bedingung verletzt: verringern Sie dt oder erhöhen Sie nx.")

# ------------------- ANFANGSBEDINGUNGEN -------------------
def startbedingung(modus):
    if modus == "Sinus":
        u0 = np.sin(np.pi * x)
        v0 = np.zeros_like(x)
    elif modus == "Dreieck":
        u0 = np.where(x <= 0.5, 2*x, 2*(1-x))
        v0 = np.zeros_like(x)
    elif modus == "Doppel-Sinus":
        u0 = np.sin(2*np.pi * x)
        v0 = np.zeros_like(x)
    elif modus == "Running-Wave":
        u0 = np.where(x < 0.33, np.sin(3*np.pi * x), 0)
        v0 = np.zeros_like(x)
    elif modus == "Gauß":
        u0 = np.exp(-200*(x-0.5)**2)
        v0 = np.zeros_like(x)
    elif modus == "Schlag":
        u0 = np.zeros_like(x)
        v0 = np.exp(-200*(x-0.5)**2) * 5
    else:
        u0 = np.zeros_like(x)
        v0 = np.zeros_like(x)
    return u0, v0

# ------------------- WELLENGLEICHUNG LÖSEN -------------------
def wellen_loesen(u0, v0):
    u = np.zeros((nt, nx+1))
    u[0, :] = u0
    # Erster Zeitschritt
    for i in range(1, nx):
        u[1, i] = u0[i] + dt*v0[i] + 0.5 * courant**2 * (u0[i+1] - 2*u0[i] + u0[i-1])
    # Haupt-Zeitschleife
    for n in range(1, nt-1):
        for i in range(1, nx):
            u[n+1, i] = (2*u[n, i] - u[n-1, i] +
                         courant**2 * (u[n, i+1] - 2*u[n, i] + u[n, i-1]))
    return u

# ------------------- GRAFIK -------------------
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Platz für die Buttons
linie, = ax.plot([], [], lw=2)
ax.set_xlim(0, L)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("x")
ax.set_ylabel("u(x, t)")

# Animationsdaten
aktueller_modus = "Sinus"
u_daten = wellen_loesen(*startbedingung(aktueller_modus))

def animieren(frame):
    linie.set_data(x, u_daten[frame])
    titel = ax.set_title(f"{aktueller_modus}")
    return linie, titel


ani = animation.FuncAnimation(fig, animieren, frames=range(0, nt, 10), interval=20, blit=False)

# ------------------- BUTTONS -------------------
ax_sin = plt.axes([0.05, 0.1, 0.1, 0.075])
ax_tri = plt.axes([0.16, 0.1, 0.13, 0.075])
ax_dbl = plt.axes([0.30, 0.1, 0.16, 0.075])
ax_hlf = plt.axes([0.47, 0.1, 0.17, 0.075])
ax_gau = plt.axes([0.65, 0.1, 0.1, 0.075])
ax_hit = plt.axes([0.76, 0.1, 0.1, 0.075])

btn_sin = Button(ax_sin, "Sinus")
btn_tri = Button(ax_tri, "Dreieck")
btn_dbl = Button(ax_dbl, "Doppel-Sinus")
btn_hlf = Button(ax_hlf, "Running-Wave")
btn_gau = Button(ax_gau, "Gauß")
btn_hit = Button(ax_hit, "Schlag")

def modus_setzen(modus):
    global aktueller_modus, u_daten
    aktueller_modus = modus
    u_daten = wellen_loesen(*startbedingung(modus))
btn_sin.on_clicked(lambda event: modus_setzen("Sinus"))
btn_tri.on_clicked(lambda event: modus_setzen("Dreieck"))
btn_dbl.on_clicked(lambda event: modus_setzen("Doppel-Sinus"))
btn_hlf.on_clicked(lambda event: modus_setzen("Running-Wave"))
btn_gau.on_clicked(lambda event: modus_setzen("Gauß"))
btn_hit.on_clicked(lambda event: modus_setzen("Schlag"))

plt.show()
