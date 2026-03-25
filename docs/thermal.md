# Gestión Térmica

## Aislamiento de vacío (MLI)

El reactor nuclear y los tanques de hidrógeno están envueltos en mantas de aislamiento multicapa (MLI) que:
- Reducen la transferencia de calor por radiación.
- Mantienen el hidrógeno líquido a temperatura criogénica (-253°C).
- Aíslan térmicamente la estructura del calor residual del reactor.

| Parámetro | Valor |
|-----------|-------|
| Número de capas | 50 |
| Espesor total | 2 cm |
| Conductividad efectiva | 0.0001 W/m·K |
| Masa | ~50 kg para área de 10 m² |

## Integración con el blindaje de plomo

El plomo de 10 cm se coloca **detrás** del aislamiento de vacío, para que:
1. El aislamiento proteja los tanques de hidrógeno del calor del reactor.
2. El plomo absorba la radiación que escapa del reactor.
3. Los tanques de hidrógeno (fríos) ayuden a disipar el calor del plomo.

## Conversión de calor residual en empuje

Odiseo aprovecha el calor residual de sus sistemas (reactor nuclear, motores, bobinas superconductoras) para generar empuje adicional sin consumo extra de combustible.

| Componente | Calor recuperado | Uso |
|------------|------------------|-----|
| Reactor nuclear | Alto | Calienta hidrógeno que circula por válvulas de no retorno |
| Motores NTP/NEP | Medio | Precalienta propelente antes de inyección |
| Bobinas superconductoras | Bajo | Calor residual se transfiere al hidrógeno circulante |

### Sistema de válvulas de no retorno

El hidrógeno líquido circula por un sistema cerrado que:
1. **Absorbe calor** de las zonas calientes (reactor, motores, electrónica).
2. **Se expande** al calentarse, aumentando su presión.
3. **Pasa por válvulas de no retorno** que dirigen el flujo hacia toberas de baja presión.
4. **Genera empuje adicional** sin consumo extra de combustible.

| Parámetro | Valor |
|-----------|-------|
| Empuje adicional estimado | 2–5 kN (depende del régimen térmico) |
| Ahorro de propelente | 5–10% en maniobras de larga duración |
| Temperatura de entrada hidrógeno | -253°C (tanques) |
| Temperatura de salida | 500–1,000°C (según fuente de calor) |

### Ventajas

- **Enfriamiento pasivo:** El calor se extrae de los sistemas críticos sin radiadores adicionales.
- **Empuje gratis:** El hidrógeno caliente se expande y se convierte en empuje útil.
- **Simplicidad:** Válvulas mecánicas de no retorno, sin partes móviles complejas.
- **Redundancia:** Si falla una bomba, el sistema puede operar por diferencia de presión.

## Flujo del sistema térmico
