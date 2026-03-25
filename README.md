# Odiseo

**Una nave de infraestructura para colonizar Marte. No es un cohete. Es un sistema completo.**

## Misión

Transportar 6 personas a Marte, establecer una base operativa autosuficiente, y mantener un nodo logístico reutilizable en órbita.

## Arquitectura

| Módulo | Función |
|--------|---------|
| **Odiseo (núcleo)** | Propulsión, energía, escudo radiológico. Permanece en órbita marciana como satélite y almacén orbital. |
| **Rueda centrífuga** | Gravedad artificial durante el viaje. Autónoma, con esclusa giratoria intermitente. Se detiene en órbita. |
| **Goliat-Son** | Aterrizador y carguero. 6 personas + 8.7 toneladas de carga. Despliega base en superficie. |

## Subsistemas Clave

| Sistema | Solución |
|---------|----------|
| **Despegue** | Lanzador comercial (Starship) — Odiseo no es un cohete |
| **Propulsión espacial** | Hidrógeno líquido + reactor nuclear (NTP/NEP) |
| **Energía** | RTG nuclear (50 años) + baterías litio + paneles solares. Transferencia inductiva a rueda. |
| **Gestión térmica** | Hidrógeno circulante + válvulas de no retorno + empuje térmico adicional |
| **Escudo radiológico** | Campo magnético activo (bobinas superconductoras) para partículas cargadas + blindaje pasivo (W-V + HDPE + H₂) |
| **Protección pasiva** | Tungsteno-vanadio exterior + capa HDPE + tanques de hidrógeno como blindaje |
| **Gravedad artificial** | Rueda centrífuga con esclusa giratoria intermitente (sin sello rotatorio continuo) |
| **Soporte vital** | Autónomo en rueda. Captura de gas interestelar para complementar O₂/H₂O (concepto en estudio) |
| **Producción en Marte** | Torres ShieldAir adaptadas producen O₂, biomasa y calor usando CO₂ atmosférico (95%) + energía nuclear |
| **Comunicaciones** | Redundancia en rueda (antenas, transceptores) |
| **Navegación** | Redundancia en rueda (INS, sensores estelares) |
| **Emergencias** | Cápsulas de escape, rutas de evacuación, detección temprana, protocolos |

## Tripulación

| Rol | Cantidad |
|-----|----------|
| Ingeniero químico | 2 |
| Ingeniero mecánico | 2 |
| Astrofísico | 1 |
| Médico cirujano | 1 |

**Total:** 6 personas.

## Capacidad de Carga (Goliat-Son)

| Categoría | Peso (kg) |
|-----------|-----------|
| Hábitats inflables | 2,000 |
| Paneles solares + baterías | 1,500 |
| Torres ShieldAir (versión Marte) | 2,000 |
| Equipos de agua + reciclaje | 500 |
| Alimentos + semillas | 1,000 |
| Herramientas + impresoras 3D | 1,000 |
| Equipos científicos + rover | 500 |
| Kit médico + emergencias | 200 |
| **Total** | **8,700** |

## Operación en Marte

1. **Odiseo** frena en órbita baja. Rueda se detiene.
2. **Goliat-Son** aterriza con tripulación y carga.
3. **Despliegue base** (primera semana):
   - Paneles solares → energía
   - Hábitats inflables → presurización
   - Torres ShieldAir → O₂, biomasa, calor
4. **Odiseo** actúa como satélite de comunicaciones y observación.
5. **Retorno o reabastecimiento:** Odiseo puede volver a Tierra por más equipo. Goliat-Son puede reabastecerse con combustible producido en Marte.

## Estado actual

 Arquitectura completa  
 Subsistemas definidos  
 Tripulación y carga definidas  
 Simulación de trayectoria (en desarrollo)  
 Diseño CAD de esclusa giratoria  
 Validación de producción ISRU en Marte

## Proyectos hermanos

- **Goliat-Orbital** — captura y reciclaje de basura espacial  
  [Repositorio](https://github.com/enriqueherbertag-lgtm/Goliat-Orbital)
- **Quantum-Flux** — enlace satelital resiliente independiente de cables submarinos  
  [Repositorio](https://github.com/enriqueherbertag-lgtm/quantum-flux)

## Licencia

Apache 2.0 con restricción de uso comercial.  
*Este es un framework base open-source. El que quiera más precisión, menor latencia o features avanzadas… que lo modifique y contribuya.*

## Autor

**Enrique Aguayo H.**  
Investigador independiente, Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)
