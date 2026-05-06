#  Auditoría de Seguridad Ofensiva – Caso NovaShop

 Proyecto realizado en entorno controlado con fines académicos.
 --

##  Rol
Network Security Tester

---

## Objetivo
Ejecutar una auditoría de seguridad simulando un atacante ético para identificar vulnerabilidades en la infraestructura lógica y aplicación web de la empresa NovaShop S.A.

---

## Gestión y Cumplimiento
- Definición de alcance enfocada en infraestructura lógica y aplicación web (autenticación y transacciones).
- Participación en la estructuración de contrato de servicios con cláusulas de:
  - Confidencialidad
  - Pruebas no destructivas
  - Manejo seguro de la información
- Aplicación de principios éticos en pruebas de penetración.

---

## Metodología PTES Y Cyber Kill Chain
Fases aplicadas:
- Reconocimiento
- Escaneo
- Enumeración
- Explotación controlada
- Remediación

---

## Herramientas utilizadas
- Nmap
- Kali Linux
- Wireshark

---

## Hallazgos relevantes

###  Inyección SQL
- Vulnerabilidad en campo de autenticación.
- Manipulación de consultas permitió acceso a credenciales administrativas.

###  Movimiento lateral
- Fallas en segmentación de red.
- Reutilización de credenciales.
- Riesgo de escalamiento de privilegios.

###  Análisis de infraestructura
- Mapeo de activos
- Identificación de puertos y servicios expuestos
- Evaluación de configuraciones de red

---

##  Plan de mitigación
- Implementación de consultas preparadas (prevención de SQL Injection)
- Segmentación de red mediante VLANs
- Endurecimiento de seguridad en capa 2
- Aplicación del principio de mínimo privilegio
- Creacion de ACL ,reforzamiento de autenticacion
- Plan de remediacion mediante herramientas Cisco como ISE/SDA Y CISCO TALOS 

---

## Entregables
- Reporte ejecutivo (enfocado en negocio)
- Reporte técnico (detallado)
- Plan de mitigación
- Bitácora de trabajo

---

## Trabajo colaborativo
- Coordinación con equipo técnico para asegurar consistencia metodológica
- Mejora continua basada en retroalimentación
- Presentación de resultados a empresa tutora (CISCO)

---

##  Aprendizaje
Este proyecto fortaleció habilidades en:
- Análisis de vulnerabilidades reales
- Pensamiento ofensivo y defensivo
- Comunicación técnica a nivel empresarial
- Trabajo en equipo en entornos de ciberseguridad

## Aprendizaje
Este proyecto permitió desarrollar habilidades en análisis de vulnerabilidades, pensamiento crítico y documentación técnica orientada a negocio.
