# Odiseo — Extracto Técnico Ejecutivo

**Una nave de infraestructura para colonizar Marte. No es un cohete. Es un sistema completo.**

---

## Resumen

Odiseo es una nave de infraestructura diseñada para transportar 6 personas a Marte, establecer una base autosuficiente, y mantener un nodo logístico reutilizable en órbita. A diferencia de los cohetes tradicionales, Odiseo es un sistema modular que incluye:

- **Núcleo orbital** (propulsión nuclear, energía, escudo radiológico)
- **Rueda centrífuga** (gravedad artificial, hábitat de tránsito)
- **Goliat-Son** (aterrizador y carguero con 8.7 toneladas de carga)

---

## Arquitectura

| Módulo | Función |
|--------|---------|
| **Odiseo (núcleo)** | Propulsión, energía, escudo radiológico. Permanece en órbita marciana como satélite y almacén orbital. |
| **Rueda centrífuga** | Gravedad artificial durante el viaje. Autónoma, con esclusa giratoria intermitente. Se detiene en órbita. |
| **Goliat-Son** | Aterrizador y carguero. 6 personas + 8.7 toneladas de carga. Despliega base en superficie. |

---

## Propulsión

| Sistema | Especificación |
|---------|----------------|
| **Principal** | Hidrógeno líquido + reactor nuclear (NTP/NEP) |
| **Isp** | 900–5,000 s (según configuración) |
| **Viaje Tierra-Marte** | 3–6 meses |
| **Estado** | Tecnología en desarrollo activo (NASA DRACO, 2027) |

---

## Energía

| Fuente | Función |
|--------|---------|
| **Reactor nuclear** | Propulsión + generación eléctrica durante tránsito |
| **RTG nuclear (50 años)** | Energía de respaldo para sistemas críticos |
| **Paneles solares** | Generación adicional en núcleo y rueda |
| **Baterías de litio** | Almacenamiento y respaldo |

---

## Protección Radiológica

| Capa | Material | Función |
|------|----------|---------|
| **1. Escudo magnético activo** | Bobinas superconductoras | Desvía partículas cargadas (tormentas solares, rayos cósmicos) |
| **2. Blindaje pasivo exterior** | Tungsteno-vanadio (W-V) | Estructural, calor, micrometeoritos |
| **3. Blindaje intermedio** | HDPE + tanques de hidrógeno | Absorbe neutrones y fragmentos de impacto |
| **4. Cabina** | Aluminio compuesto | Presurizada, última capa |

---

## Gravedad Artificial

| Componente | Especificación |
|------------|----------------|
| **Rueda centrífuga** | 12 m de diámetro, 3 m de ancho |
| **Gravedad simulada** | 0.3–0.4 g (ajustable por rotación) |
| **Conexión con núcleo** | Esclusa giratoria intermitente (sin sello rotatorio continuo) |
| **Uso** | Durante tránsito; se detiene en órbita marciana |

---

## Producción en Marte (ISRU)

| Recurso | Método de producción |
|---------|----------------------|
| **Oxígeno** | Torres ShieldAir adaptadas (algas + CO₂ atmosférico + energía nuclear) |
| **Agua** | Extracción de hielo subterráneo + derretimiento con calor recuperado |
| **Combustible (CH₄ + O₂)** | Reactor Sabatier + electrólisis (para Goliat-Son y retorno) |
| **Biomasa** | Algas → alimento, plásticos para impresión 3D |

**Ventaja:** Odiseo no necesita llevar combustible de regreso desde Tierra.

---

## Tripulación

| Rol | Cantidad | Funciones principales |
|-----|----------|----------------------|
| Ingeniero químico | 2 | Producción de recursos, operación de torres ShieldAir, reactor nuclear |
| Ingeniero mecánico | 2 | Mantenimiento de sistemas, hábitats, impresión 3D |
| Astrofísico | 1 | Navegación, comunicaciones, monitoreo de radiación |
| Médico cirujano | 1 | Salud, emergencias, psicología |

**Total:** 6 personas.

---

## Carga Útil (Goliat-Son)

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

---

## Operación en Marte

| Fase | Acción |
|------|--------|
| **Llegada** | Odiseo frena en órbita baja. Rueda se detiene. |
| **Aterrizaje** | Goliat-Son desciende con tripulación y carga. |
| **Despliegue base** | Paneles solares → hábitats → torres ShieldAir → O₂, agua, calor. |
| **Operación orbital** | Odiseo actúa como satélite de comunicaciones, observación y nodo logístico. |
| **Retorno o reabastecimiento** | Odiseo puede volver a Tierra por más equipo. Goliat-Son puede reabastecerse con combustible producido en Marte. |

---

## Estado Actual

| Área | Estado |
|------|--------|
| Arquitectura | ✅ Definida |
| Subsistemas | ✅ Documentados |
| Tripulación y carga | ✅ Definidas |
| Simulación de trayectoria | 🔲 En desarrollo |
| Diseño CAD (esclusa) | 🔲 Pendiente |
| Validación ISRU | 🔲 Pendiente |

---

## Diferenciadores Clave

| Concepto | Odiseo |
|----------|--------|
| **No es un cohete** | Lanzador comercial (Starship) para despegue |
| **Propulsión espacial** | Hidrógeno + nuclear (tecnología real en desarrollo) |
| **Energía** | Nuclear de larga duración (50 años) |
| **Protección radiológica** | Pasiva (W-V + HDPE + H₂) + magnética complementaria |
| **Gravedad artificial** | Rueda centrífuga con esclusa giratoria intermitente |
| **Producción en Marte** | Torres ShieldAir adaptadas (O₂, biomasa, calor desde CO₂) |
| **Reutilización** | 100% — Odiseo puede volver a Tierra por más equipo |

---

## Frases para Comunicación

> *"Odiseo no es un cohete. Es una nave de infraestructura que convierte Marte en una segunda Tierra."*

> *"La torre que limpiaba el smog en Delhi ahora produce oxígeno, alimento y calor en Marte."*

> *"Lanzada plegada, vive en el espacio, toca tierra solo cuando llega a su destino."*

---

## Autor

**Enrique Aguayo H.**  
Investigador independiente, Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)

---

*Documento confidencial — Propiedad intelectual registrada en GitHub con fecha 2026-03-24*
