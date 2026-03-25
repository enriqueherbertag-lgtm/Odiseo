# Esclusa Giratoria Intermitente - Odiseo

## Concepto

La esclusa giratoria intermitente permite la transferencia de tripulación entre el núcleo fijo de Odiseo y la rueda centrífuga giratoria, **sin necesidad de un sello rotatorio continuo**.

### ¿Cómo funciona?

1. La tripulación ingresa a la esclusa desde el núcleo (esclusa quieta, alineada con la compuerta A)
2. Se cierra la compuerta trasera
3. La esclusa gira 180° sobre su eje (motores eléctricos de precisión)
4. Se alinea con la entrada de la rueda centrífuga
5. Se abre la compuerta delantera y la tripulación pasa a la rueda
6. El proceso se invierte para volver al núcleo

### Ventajas

| Ventaja | Descripción |
|---------|-------------|
| **Sin sello rotatorio continuo** | Los sellos solo se activan cuando la esclusa está en posición estática. Mayor confiabilidad y menor desgaste. |
| **Tecnología mecánica simple** | Rodamientos industriales, motores eléctricos estándar, compuertas herméticas probadas. |
| **Redundancia** | Dos esclusas (una en cada sentido) o una con doble mecanismo de giro. |
| **Seguridad** | Si falla el giro, la tripulación queda en un lado u otro, pero nunca despresurizada. |

## Dimensiones

| Parámetro | Valor |
|-----------|-------|
| Diámetro exterior | 2.0 m |
| Longitud | 2.5 m |
| Diámetro de paso (compuerta) | 1.2 m |
| Peso estimado (estructura + mecanismos) | 800 kg |
| Velocidad de giro | 1–2 rpm (giro completo en 15–30 segundos) |

## Materiales propuestos

| Componente | Material |
|------------|----------|
| Estructura | Aluminio 7075-T6 o composite de fibra de carbono |
| Compuertas | Aluminio con sellos de elastómero de vacío |
| Mecanismo de giro | Rodamientos de acero inoxidable, motores eléctricos con freno |
| Sellado estático | Metal sobre metal (en interfaz núcleo/esclusa) |

## Modelos CAD

| Archivo | Descripción |
|---------|-------------|
| `esclusa_giratoria.fcstd` | Modelo 3D en FreeCAD (versión actual) |
| `esclusa_giratoria.stl` | Exportación STL para visualización rápida |
| `renders/` | Capturas de pantalla del diseño |

## Estado actual

🔲 Modelo básico (cilindro + compuertas)  
🔲 Mecanismo de giro detallado  
🔲 Integración con núcleo y rueda  
🔲 Análisis estructural en FreeCAD

## Referencias

- NASA (2018). *Airlock Designs for Deep Space Missions*
- ESA (2020). *Docking Systems and Transfer Mechanisms*
- Diseño propio de Odiseo — esclusa intermitente (patente en estudio)
