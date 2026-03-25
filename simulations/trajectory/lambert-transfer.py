"""
Transferencia Lambert Tierra-Marte con poliastro
Basado en recomendación de Grok
"""

from astropy import units as u
from astropy.time import Time
import matplotlib.pyplot as plt
from poliastro.bodies import Sun, Earth, Mars
from poliastro.ephem import Ephem
from poliastro.maneuver import Maneuver
from poliastro.plotting import OrbitPlotter3D
from poliastro.twobody import Orbit

# Ventana de lanzamiento (ajustar según necesidades)
date_launch = Time("2026-12-01", scale="tdb")
date_arrival = Time("2027-08-15", scale="tdb")

# Órbitas heliocéntricas
earth = Ephem.from_body(Earth, date_launch)
mars = Ephem.from_body(Mars, date_arrival)

orb_earth = Orbit.from_ephem(Sun, earth, date_launch)
orb_mars = Orbit.from_ephem(Sun, mars, date_arrival)

# Solución Lambert
man_lambert = Maneuver.lambert(orb_earth, orb_mars)

# Resultados
dv_departure, dv_arrival = man_lambert.impulses
print(f"Delta-v de salida (Tierra): {dv_departure[1].norm():.3f}")
print(f"Delta-v de llegada (Marte): {dv_arrival[1].norm():.3f}")
print(f"Delta-v total: {man_lambert.get_total_cost():.3f}")
print(f"Tiempo de vuelo: {man_lambert.get_total_time().to(u.day):.1f}")

# Ecuación de Tsiolkovsky para masa de propelente
Isp = 450 * u.s  # hidrógeno líquido
g0 = 9.81 * u.m / u.s**2
dv_total = man_lambert.get_total_cost()
mass_ratio = (dv_total / (Isp * g0)).decompose()
m_dry = 41700 * u.kg  # masa seca estimada
m_prop = m_dry * (mass_ratio - 1)

print(f"\nMasa seca: {m_dry:.0f}")
print(f"Masa de propelente (hidrógeno): {m_prop:.0f}")
print(f"Masa total en órbita: {(m_dry + m_prop):.0f}")

# Plot (opcional)
plotter = OrbitPlotter3D()
plotter.plot(orb_earth, label="Tierra (lanzamiento)")
plotter.plot(orb_mars, label="Marte (llegada)")
plotter.plot_maneuver(orb_earth, man_lambert, color="red")
plt.show()
