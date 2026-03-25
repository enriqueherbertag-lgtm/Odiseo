"""
Transferencia Lambert Tierra-Marte con poliastro
Cálculo de delta-v, masa de propelente y exportación de resultados
Versión corregida - manejo correcto de vectores de velocidad
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
import pandas as pd
from poliastro.bodies import Sun, Earth, Mars
from poliastro.ephem import Ephem
from poliastro.maneuver import Maneuver
from poliastro.plotting import OrbitPlotter3D
from poliastro.twobody import Orbit

# ============================================================================
# PARÁMETROS DE LA MISIÓN
# ============================================================================

# Ventana de lanzamiento (ajustar según necesidad)
date_launch = Time("2026-12-01", scale="tdb")
date_arrival = Time("2027-08-15", scale="tdb")

# Masa seca estimada de Odiseo (kg) - actualizar con diseño final
M_DRY = 41700 * u.kg  # estructura + rueda + Goliat-Son + carga útil

# Impulso específico según tipo de motor
ISP_NTP = 950 * u.s      # Nuclear Thermal Propulsion
ISP_NEP = 4000 * u.s     # Nuclear Electric Propulsion

g0 = 9.80665 * u.m / u.s**2

# ============================================================================
# CÁLCULO DE TRAYECTORIA (LAMBERT)
# ============================================================================

print("=" * 60)
print("SIMULACIÓN DE TRAYECTORIA ODISEO - TIERRA A MARTE")
print("=" * 60)
print(f"Fecha de lanzamiento: {date_launch.iso}")
print(f"Fecha de llegada: {date_arrival.iso}")
print(f"Tiempo de vuelo: {(date_arrival - date_launch).to(u.day):.1f}")
print()

# Órbitas de salida y llegada
earth = Ephem.from_body(Earth, date_launch)
mars = Ephem.from_body(Mars, date_arrival)

orb_earth = Orbit.from_ephem(Sun, earth, date_launch)
orb_mars = Orbit.from_ephem(Sun, mars, date_arrival)

# Solución Lambert
man_lambert = Maneuver.lambert(orb_earth, orb_mars)

# Extraer delta-v correctamente
# Los impulsos son una lista de tuplas (tiempo, vector_delta_v)
# Cada impulso es (t, dv_vector)
impulses = man_lambert.impulses
dv_departure_vector = impulses[0][1]  # vector de delta-v en salida
dv_arrival_vector = impulses[1][1]    # vector de delta-v en llegada

# Calcular magnitud de los vectores
dv_departure = np.linalg.norm(dv_departure_vector.value) * dv_departure_vector.unit
dv_arrival = np.linalg.norm(dv_arrival_vector.value) * dv_arrival_vector.unit
dv_total = dv_departure + dv_arrival

print("RESULTADOS DE TRAYECTORIA:")
print(f"  Delta-v salida (Tierra): {dv_departure:.3f}")
print(f"  Delta-v llegada (Marte): {dv_arrival:.3f}")
print(f"  Delta-v total: {dv_total:.3f}")
print()

# ============================================================================
# CÁLCULO DE MASA DE PROPELENTE (ECUACIÓN DE TSIOLKOVSKY)
# ============================================================================

def calculate_propellant_mass(dv, isp, m_dry):
    """Calcula masa de propelente usando ecuación de Tsiolkovsky"""
    mass_ratio = np.exp((dv / (isp * g0)).decompose())
    m_prop = m_dry * (mass_ratio - 1)
    return m_prop, mass_ratio

# NTP
m_prop_ntp, mass_ratio_ntp = calculate_propellant_mass(dv_total, ISP_NTP, M_DRY)

# NEP
m_prop_nep, mass_ratio_nep = calculate_propellant_mass(dv_total, ISP_NEP, M_DRY)

print("CÁLCULO DE MASA DE PROPELENTE (HIDRÓGENO):")
print(f"  Masa seca (estructura + carga): {M_DRY:.0f}")
print()
print("  NTP (Nuclear Thermal Propulsion, Isp = 950 s):")
print(f"    Relación de masas (Mi/Mf): {mass_ratio_ntp:.3f}")
print(f"    Masa de hidrógeno necesaria: {m_prop_ntp:.0f}")
print(f"    Masa total en órbita: {(M_DRY + m_prop_ntp):.0f}")
print()
print("  NEP (Nuclear Electric Propulsion, Isp = 4000 s):")
print(f"    Relación de masas (Mi/Mf): {mass_ratio_nep:.3f}")
print(f"    Masa de hidrógeno necesaria: {m_prop_nep:.0f}")
print(f"    Masa total en órbita: {(M_DRY + m_prop_nep):.0f}")

# ============================================================================
# EXPORTAR RESULTADOS A CSV
# ============================================================================

# Crear carpeta results si no existe
import os
os.makedirs("results", exist_ok=True)

results = {
    "parametro": [
        "fecha_lanzamiento",
        "fecha_llegada",
        "tiempo_vuelo_dias",
        "delta_v_salida_km/s",
        "delta_v_llegada_km/s",
        "delta_v_total_km/s",
        "masa_seca_kg",
        "isp_ntp_s",
        "masa_propelente_ntp_kg",
        "masa_total_ntp_kg",
        "isp_nep_s",
        "masa_propelente_nep_kg",
        "masa_total_nep_kg"
    ],
    "valor": [
        date_launch.iso,
        date_arrival.iso,
        (date_arrival - date_launch).to(u.day).value,
        dv_departure.to(u.km / u.s).value,
        dv_arrival.to(u.km / u.s).value,
        dv_total.to(u.km / u.s).value,
        M_DRY.value,
        ISP_NTP.value,
        m_prop_ntp.value,
        (M_DRY + m_prop_ntp).value,
        ISP_NEP.value,
        m_prop_nep.value,
        (M_DRY + m_prop_nep).value
    ]
}

df = pd.DataFrame(results)
df.to_csv("results/trajectory_results.csv", index=False)
print("\n✅ Resultados exportados a results/trajectory_results.csv")

# ============================================================================
# GRÁFICO DE TRAYECTORIA (OPCIONAL)
# ============================================================================

try:
    plotter = OrbitPlotter3D()
    plotter.plot(orb_earth, label="Tierra (lanzamiento)")
    plotter.plot(orb_mars, label="Marte (llegada)")
    plotter.plot_maneuver(orb_earth, man_lambert, color="red", label="Trayectoria Odiseo")
    plt.title("Trayectoria Tierra-Marte - Odiseo")
    plt.savefig("results/trajectory_plot.png", dpi=150)
    print("✅ Gráfico guardado en results/trajectory_plot.png")
    plt.show()
except Exception as e:
    print(f"⚠️ No se pudo generar el gráfico: {e}")

# ============================================================================
# RESUMEN FINAL
# ============================================================================

print("\n" + "=" * 60)
print("RESUMEN EJECUTIVO")
print("=" * 60)
print(f"""
Odiseo puede realizar la transferencia Tierra-Marte con:
- Delta-v total: {dv_total.to(u.km / u.s):.2f}
- Tiempo de vuelo: {(date_arrival - date_launch).to(u.day):.1f}

Con NTP (Isp 950 s):
- Masa de hidrógeno: {m_prop_ntp:.0f}
- Masa total en órbita: {(M_DRY + m_prop_ntp):.0f}

Con NEP (Isp 4000 s):
- Masa de hidrógeno: {m_prop_nep:.0f}
- Masa total en órbita: {(M_DRY + m_prop_nep):.0f}

PRÓXIMOS PASOS:
- Validar masa seca (41,700 kg) con diseño detallado
- Optimizar trayectoria para reducir delta-v
- Calcular capacidad de lanzador comercial (Starship)
""")
