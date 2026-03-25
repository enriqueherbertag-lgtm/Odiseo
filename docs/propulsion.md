# Propulsión de Odiseo

## Sistema Principal: Hidrógeno Líquido + Reactor Nuclear

Odiseo utiliza un sistema de propulsión combinado basado en **hidrógeno líquido como combustible** y un **reactor nuclear** como fuente de energía. Esta configuración ofrece un equilibrio entre empuje y eficiencia, utilizando tecnologías que están en desarrollo activo por NASA, DARPA y empresas privadas.

## Opciones Técnicas

| Sistema | Empuje | Eficiencia (Isp) | Estado actual |
|---------|--------|------------------|---------------|
| **NTP (Nuclear Thermal Propulsion)** | Alto | 900–1,000 s | Probado en tierra (NERVA, 1960-70s). En desarrollo por NASA/DARPA (DRACO, vuelo previsto 2027) |
| **NEP (Nuclear Electric Propulsion)** | Bajo | 3,000–5,000 s | En desarrollo (VASIMR, sistemas de energía nuclear espacial) |

## Configuración de Odiseo

| Componente | Especificación |
|------------|----------------|
| **Combustible** | Hidrógeno líquido (LH₂), almacenado en tanques criogénicos de doble pared |
| **Oxidante** | No requiere (motor nuclear térmico o eléctrico) |
| **Tanques de hidrógeno** | Ubicados estratégicamente entre el reactor nuclear y la rueda de gravedad, actuando como blindaje radiológico pasivo |
| **Gestión térmica** | El hidrógeno circula por las zonas calientes (reactor, electrónica, escudo magnético) antes de ser inyectado al motor, aprovechando el calor residual para precalentamiento y empuje adicional mediante válvulas de no retorno |

## Rendimiento Estimado

| Parámetro | Valor NTP | Valor NEP |
|-----------|-----------|-----------|
| Isp (específico) | 900–1,000 s | 3,000–5,000 s |
| Empuje | 50–250 kN | 5–20 kN |
| Delta-v total (Tierra-Marte) | ~5–7 km/s | ~5–7 km/s (aceleración continua) |
| Consumo de hidrógeno | Alto | Bajo (requiere más tiempo de aceleración) |

## Ventajas

| Ventaja | Descripción |
|---------|-------------|
| **Tecnología real** | En desarrollo activo por NASA, DARPA, y empresas privadas. DRACO (NTP) previsto para vuelo en 2027 |
| **Alto rendimiento** | Isp muy superior a motores químicos (450 s) |
| **Redundancia energética** | El reactor nuclear también alimenta los sistemas de energía de la nave (baterías, paneles solares como respaldo) |
| **Blindaje pasivo** | Los tanques de hidrógeno se colocan estratégicamente entre el reactor y la tripulación, actuando como escudo radiológico |
| **Gestión térmica integrada** | El hidrógeno circula por zonas calientes antes de quemarse, convirtiendo calor residual en empuje adicional |

## Desventajas y Mitigaciones

| Desventaja | Mitigación |
|------------|------------|
| **Masa del reactor y blindaje** | El tungsteno-vanadio del fuselaje y los tanques de hidrógeno actúan como blindaje, reduciendo peso extra |
| **Complejidad regulatoria** | Reactor solo se activa en órbita terrestre, no durante despegue |
| **Disipación térmica** | El hidrógeno circulante extrae calor y lo convierte en empuje, reduciendo la necesidad de radiadores |
| **Desarrollo pendiente** | Odiseo está diseñado para ser compatible con NTP o NEP cuando estén disponibles comercialmente |

## Modos de Vuelo

| Fase | Modo | Combustible | Notas |
|------|------|-------------|-------|
| **Despegue Tierra** | Lanzador comercial | — | Odiseo se lanza plegada dentro de Starship o similar |
| **Inserción orbital** | Químico (respaldo) | LH₂ + LOX | Solo si es necesario para maniobras iniciales |
| **Tránsito Tierra-Marte** | Nuclear (NTP/NEP) | LH₂ | Aceleración continua, viaje de 3–6 meses |
| **Inserción orbital marciana** | Nuclear | LH₂ | Frenado para captura orbital |
| **Maniobras orbitales** | Químico (respaldo) | LH₂ + LOX | Pequeños ajustes, acoplamiento con Goliat-Son |

## Próximos Pasos

- [ ] Simular delta-v total con GMAT/poliastro
- [ ] Calcular masa de hidrógeno necesaria
- [ ] Evaluar opción NTP vs NEP según masa total y tiempo de viaje
- [ ] Diseñar integración térmica con válvulas de no retorno

## Referencias

- NASA (2024). *DRACO: Demonstration Rocket for Agile Cislunar Operations*
- DARPA (2025). *Nuclear Thermal Propulsion Program*
- Ad Astra Rocket Company (2024). *VASIMR® Engine Development*
- NASA (2023). *Kilopower Project* (reactores para superficie)
