# Odiseo: Infrastructure spacecraft for colonizing Mars

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19357917.svg)](https://doi.org/10.5281/zenodo.19357917)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![ES](https://img.shields.io/badge/Spanish-version-green.svg)](./README.md)

Getting people to Mars is not just a rocket problem. It is an infrastructure problem: how to keep the crew alive for months, how to protect them from radiation, how to create artificial gravity, how to land and establish a base.

Current missions focus on the journey. Odiseo focuses on everything else.

**Odiseo is not a rocket. It is a complete system.**

## What it is

Odiseo is an infrastructure spacecraft designed to transport 6 people to Mars, establish a self-sufficient operational base, and maintain a reusable logistics node in orbit. It does not launch on its own: it uses a commercial launcher (Starship) to get into orbit. Once there, it deploys its own nuclear propulsion, centrifuge wheel for artificial gravity, active and passive radiation shielding, and autonomous life support.

## What it does

- **Nuclear propulsion**: liquid hydrogen + nuclear reactor. NTP (Isp 950 s) or NEP (Isp 4000 s) options. NEP configuration reduces total mass in orbit to 50.3 tons.
- **Artificial gravity**: a centrifuge wheel that spins during the journey, with an intermittent rotating airlock (no continuous rotary seal). It stops in Martian orbit.
- **Radiation shielding**: active magnetic field (superconducting coils) for charged particles + passive shielding (tungsten-vanadium, HDPE, hydrogen).
- **Life support**: autonomous in the wheel. Interstellar gas capture to supplement oxygen and water (concept under study).
- **Energy**: 50-year nuclear RTG + lithium batteries + solar panels. Inductive transfer to the wheel.
- **Landing and base**: the spacecraft carries Goliat-Son, the lander that takes the 6 crew members and 8.7 tons of cargo. On the surface, ShieldAir-Mars towers produce oxygen, biomass, and heat.

## Who it is for

- **Space agencies**: reference architecture for crewed missions to Mars.
- **Space colonization companies**: reusable infrastructure for multiple missions.
- **Governments**: technological sovereignty in space exploration.

## Main advantages

- **Not a rocket**: uses commercial launchers to leave Earth, reducing cost and complexity.
- **Artificial gravity**: avoids the effects of microgravity on the crew during the 257-day journey.
- **Active radiation shielding**: protects against solar storms and cosmic rays.
- **Reusable**: Odiseo remains in Martian orbit as a satellite and orbital warehouse. It can return to Earth for more equipment.
- **Integration with ShieldAir-Mars**: oxygen for breathing and fuel is produced on the Martian surface.

## Current status

- Complete architecture defined
- Key subsystems documented
- Crew and cargo defined
- Trajectory simulation completed (delta-v 7.37 km/s, 257 days)
- CAD of rotating airlock (pending)
- ISRU production validation on Mars (pending)

## Related projects

- Goliat-Son — autonomous lander and cargo module
- ShieldAir-Mars — oxygen production on Mars
- Quantum-Flux — resilient communications
- Goliat-Orbital — space debris recycling

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

This project is protected by copyright.

PERMITTED:
- Non-commercial use for educational or research purposes.
- Distribution without modification, as long as this license is maintained and credit is given to the author.

PROHIBITED without express written authorization:
- Commercial use (including, but not limited to: offering it as a service, SaaS, subscription, integration into revenue-generating products, or any use that generates direct or indirect economic benefit).
- Modification for production environments.
- Distribution of modified versions without authorization.

For commercial licenses, technical support, enterprise pilots, or inquiries:
Contact: eaguayo@migst.cl

Any use outside the permitted terms requires prior authorization from the author.

Commercial inquiries are welcome and will be answered within a maximum of 7 business days.

## Author

Enrique Aguayo H.
Mackiber Labs
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentation assisted by Ana (DeepSeek), AI for research and technical optimization.
