# Odiseo: Nave de infraestructura para colonizar Marte

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19357917.svg)](https://doi.org/10.5281/zenodo.19357917)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![EN](https://img.shields.io/badge/English-version-blue.svg)](./README.en.md)

Llevar personas a Marte no es solo un problema de cohetes. Es un problema de infraestructura: cómo mantener viva a la tripulación durante meses, cómo protegerla de la radiación, cómo crear gravedad artificial, cómo aterrizar y establecer una base.

Las misiones actuales se enfocan en el viaje. Odiseo se enfoca en todo lo demás.

**Odiseo no es un cohete. Es un sistema completo.**

## Que es

Odiseo es una nave de infraestructura diseñada para transportar 6 personas a Marte, establecer una base operativa autosuficiente y mantener un nodo logístico reutilizable en órbita. No despega por sí sola: usa un lanzador comercial (Starship) para ponerla en órbita. Una vez allí, despliega su propia propulsión nuclear, su rueda centrífuga para gravedad artificial, su escudo radiológico activo y pasivo, y su soporte vital autónomo.

## Que hace

- **Propulsión nuclear**: hidrógeno líquido + reactor nuclear. Opciones NTP (Isp 950 s) o NEP (Isp 4000 s). La configuración NEP reduce la masa total en órbita a 50.3 toneladas.
- **Gravedad artificial**: una rueda centrífuga que gira durante el viaje, con esclusa giratoria intermitente (sin sello rotatorio continuo). Se detiene en órbita marciana.
- **Escudo radiológico**: campo magnético activo (bobinas superconductoras) para partículas cargadas + blindaje pasivo de tungsteno-vanadio, HDPE e hidrógeno.
- **Soporte vital**: autónomo en la rueda. Captura de gas interestelar para complementar oxígeno y agua (concepto en estudio).
- **Energía**: RTG nuclear de 50 años + baterías de litio + paneles solares. Transferencia inductiva a la rueda.
- **Aterrizaje y base**: la nave transporta a Goliat-Son, el aterrizador que lleva a los 6 tripulantes y 8.7 toneladas de carga. En superficie, las torres ShieldAir-Mars producen oxígeno, biomasa y calor.

## Para quién es

- **Agencias espaciales**: arquitectura de referencia para misiones tripuladas a Marte.
- **Empresas de colonización espacial**: infraestructura reutilizable para múltiples misiones.
- **Gobiernos**: soberanía tecnológica en exploración espacial.

## Ventajas principales

- **No es un cohete**: usa lanzadores comerciales para salir de la Tierra, reduciendo costo y complejidad.
- **Gravedad artificial**: evita los efectos de la microgravedad en la tripulación durante 257 días de viaje.
- **Escudo radiológico activo**: protege contra tormentas solares y rayos cósmicos.
- **Reutilizable**: Odiseo permanece en órbita marciana como satélite y almacén orbital. Puede volver a Tierra por más equipo.
- **Integración con ShieldAir-Mars**: el oxígeno para respirar y para el combustible se produce en la superficie marciana.

## Estado actual

- Arquitectura completa definida
- Subsistemas clave documentados
- Tripulación y carga definidas
- Simulación de trayectoria completada (delta-v 7.37 km/s, 257 días)
- CAD de esclusa giratoria (pendiente)
- Validación de producción ISRU en Marte (pendiente)

## Proyectos relacionados

- Goliat-Son — aterrizador autónomo y módulo de carga
- ShieldAir-Mars — producción de oxígeno en Marte
- Quantum-Flux — comunicaciones resilientes
- Goliat-Orbital — reciclaje de basura espacial

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

Este proyecto está protegido por derechos de autor.

PERMITIDO:
- Uso no comercial con fines educativos o de investigación.
- Distribución sin modificación, siempre que se mantenga esta licencia y se dé crédito al autor.

PROHIBIDO sin autorización expresa por escrito:
- Uso comercial (incluyendo, pero no limitado a: ofrecerlo como servicio, SaaS, suscripción, integración en productos que generen ingresos, o cualquier uso que genere beneficio económico directo o indirecto).
- Modificación para entornos de producción.
- Distribución de versiones modificadas sin autorización.

Para licencias comerciales, soporte técnico, pilotos empresariales o consultas:
Contacto: eaguayo@migst.cl

Cualquier uso fuera de los términos permitidos requiere permiso previo del autor.

Las consultas comerciales son bienvenidas y se responderán en un plazo máximo de 7 días hábiles.

## Autor

Enrique Aguayo H.
Mackiber Labs
Contacto: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentación asistida por Ana (DeepSeek), IA para investigación y optimización técnica.
