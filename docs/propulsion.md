# Propulsión de Odiseo

Odiseo utiliza un sistema de propulsión **nuclear de alta eficiencia** para el tránsito interplanetario.

## Configuración

| Componente | Especificación |
|------------|----------------|
| **Reactor** | NTP (Nuclear Thermal Propulsion) o NEP (Nuclear Electric Propulsion) |
| **Combustible nuclear** | Uranio altamente enriquecido (HALEU) |
| **Propulsante** | Hidrógeno líquido (LH₂) |
| **Isp (NTP)** | 900–1,000 s |
| **Isp (NEP)** | 3,000–5,000 s |
| **Empuje (NTP)** | 50–250 kN |
| **Empuje (NEP)** | 5–20 kN |

## Protección térmica y radiológica

| Capa | Material | Función |
|------|----------|---------|
| **Aislamiento de vacío** | MLI (50 capas, 2 cm) | Mantiene hidrógeno líquido, protege estructura del calor del reactor |
| **Blindaje radiológico** | Plomo (10 cm) | Atenuación de rayos gamma y neutrones |
| **Blindaje pasivo** | Tanques de H₂ (ubicados entre reactor y cabina) | Blindaje adicional contra neutrones |

## Seguridad nuclear

- El reactor se lanza **apagado** y solo se activa en órbita segura.
- Blindaje de plomo + tungsteno-vanadio + tanques de H₂ protegen a la tripulación.
- Cumple con los principios de seguridad de la ONU para reactores espaciales.

## Modos de vuelo

| Fase | Modo | Propulsante | Notas |
|------|------|-------------|-------|
| **Despegue Tierra** | Lanzador comercial | — | Odiseo se lanza plegada dentro de Starship o similar |
| **Tránsito Tierra-Marte** | Nuclear (NTP/NEP) | LH₂ | Aceleración continua, viaje de 3–6 meses |
| **Inserción orbital marciana** | Nuclear | LH₂ | Frenado para captura orbital |
| **Maniobras orbitales** | Químico (respaldo) | LH₂ + LOX | Pequeños ajustes, acoplamiento con Goliat-Son |

## Reabastecimiento en Marte

En superficie, Goliat-Son puede reabastecer sus tanques de O₂ con oxígeno producido por las torres **ShieldAir**. Para detalles sobre la producción, ver:

🔗 [ShieldAir - Marte](https://github.com/enriqueherbertag-lgtm/ShieldAir-Mars)

## Referencias

- NASA (2024). *DRACO: Demonstration Rocket for Agile Cislunar Operations*
- DARPA (2025). *Nuclear Thermal Propulsion Program*
- NRC (2023). *Lead Shielding in Nuclear Applications*
