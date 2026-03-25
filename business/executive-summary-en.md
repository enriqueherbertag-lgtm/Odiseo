# Odiseo — Executive Technical Summary

**An infrastructure spacecraft to colonize Mars. Not a rocket. A complete system.**

---

## Overview

Odiseo is an infrastructure spacecraft designed to transport 6 people to Mars, establish a self-sufficient base, and maintain a reusable orbital logistics node. Unlike traditional rockets, Odiseo is a modular system that includes:

- **Orbital Core** (nuclear propulsion, power, radiation shielding)
- **Centrifuge Ring** (artificial gravity, transit habitat)
- **Goliat-Son** (lander and cargo carrier with 8.7 tons of payload)

---

## Architecture

| Module | Function |
|--------|----------|
| **Odiseo (Core)** | Propulsion, power, radiation shielding. Remains in Mars orbit as a satellite and orbital warehouse. |
| **Centrifuge Ring** | Artificial gravity during transit. Autonomous, with intermittent rotating airlock. Stops in Mars orbit. |
| **Goliat-Son** | Lander and cargo carrier. 6 people + 8.7 tons of cargo. Deploys base on surface. |

---

## Propulsion

| System | Specification |
|--------|---------------|
| **Primary** | Liquid hydrogen + nuclear reactor (NTP/NEP) |
| **Isp** | 900–5,000 s (depending on configuration) |
| **Earth-Mars transit** | 3–6 months |
| **Status** | Actively developing technology (NASA DRACO, 2027) |

---

## Power

| Source | Function |
|--------|----------|
| **Nuclear reactor** | Propulsion + electrical generation during transit |
| **RTG (50-year life)** | Backup power for critical systems |
| **Solar panels** | Additional generation on core and ring |
| **Lithium batteries** | Storage and backup |

---

## Radiation Protection

| Layer | Material | Function |
|-------|----------|----------|
| **1. Active magnetic shield** | Superconducting coils | Deflects charged particles (solar storms, cosmic rays) |
| **2. Passive outer shielding** | Tungsten-vanadium (W-V) | Structural, thermal, micrometeoroids |
| **3. Intermediate shielding** | HDPE + hydrogen tanks | Neutron absorption, impact fragments |
| **4. Crew cabin** | Aluminum composite | Pressurized, final layer |

---

## Artificial Gravity

| Component | Specification |
|-----------|---------------|
| **Centrifuge ring** | 12 m diameter, 3 m width |
| **Simulated gravity** | 0.3–0.4 g (adjustable via rotation) |
| **Core connection** | Intermittent rotating airlock (no continuous rotary seal) |
| **Operation** | Active during transit; stops in Mars orbit |

---

## Mars In-Situ Resource Utilization (ISRU)

| Resource | Production Method |
|----------|-------------------|
| **Oxygen** | ShieldAir towers adapted (algae + atmospheric CO₂ + nuclear power) |
| **Water** | Subsurface ice extraction + melting with recovered heat |
| **Fuel (CH₄ + O₂)** | Sabatier reactor + electrolysis (for Goliat-Son and return) |
| **Biomass** | Algae → food, plastics for 3D printing |

**Advantage:** Odiseo does not need to carry return fuel from Earth.

---

## Crew

| Role | Quantity | Primary Functions |
|------|----------|-------------------|
| Chemical Engineer | 2 | Resource production, ShieldAir tower operation, nuclear reactor |
| Mechanical Engineer | 2 | Systems maintenance, habitats, 3D printing |
| Astrophysicist | 1 | Navigation, communications, radiation monitoring |
| Surgeon | 1 | Health, emergencies, psychology |

**Total:** 6 people.

---

## Payload (Goliat-Son)

| Category | Weight (kg) |
|----------|-------------|
| Inflatable habitats | 2,000 |
| Solar panels + batteries | 1,500 |
| ShieldAir towers (Mars version) | 2,000 |
| Water extraction + recycling | 500 |
| Food + seeds | 1,000 |
| Tools + 3D printers | 1,000 |
| Scientific equipment + rover | 500 |
| Medical + emergency kit | 200 |
| **Total** | **8,700** |

---

## Mars Operations

| Phase | Action |
|-------|--------|
| **Arrival** | Odiseo brakes into low Mars orbit. Ring stops. |
| **Landing** | Goliat-Son descends with crew and cargo. |
| **Base deployment** | Solar panels → habitats → ShieldAir towers → O₂, water, heat. |
| **Orbital operations** | Odiseo acts as communications satellite, observation platform, and logistics node. |
| **Return or resupply** | Odiseo can return to Earth for more equipment. Goliat-Son can refuel with locally produced propellant. |

---

## Current Status

| Area | Status |
|------|--------|
| Architecture | ✅ Defined |
| Subsystems | ✅ Documented |
| Crew and cargo | ✅ Defined |
| Trajectory simulation | 🔲 In development |
| CAD design (airlock) | 🔲 Pending |
| ISRU validation | 🔲 Pending |

---

## Key Differentiators

| Concept | Odiseo |
|---------|--------|
| **Not a rocket** | Commercial launcher (Starship) for Earth ascent |
| **Space propulsion** | Hydrogen + nuclear (real technology in development) |
| **Power** | Long-duration nuclear (50 years) |
| **Radiation protection** | Passive (W-V + HDPE + H₂) + magnetic complement |
| **Artificial gravity** | Centrifuge ring with intermittent rotating airlock |
| **Mars production** | ShieldAir towers adapted (O₂, biomass, heat from CO₂) |
| **Reusability** | 100% — Odiseo can return to Earth for more cargo |

---

## Messaging

> *"Odiseo is not a rocket. It's infrastructure that turns Mars into a second Earth."*

> *"The tower that cleaned Delhi's smog now produces oxygen, food, and heat on Mars."*

> *"Launched folded, lives in space, touches ground only at its destination."*

---

## Author

**Enrique Aguayo H.**  
Independent Researcher, Mackiber Labs  
Contact: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)

---

*Confidential document — Intellectual property registered on GitHub as of 2026-03-24*
