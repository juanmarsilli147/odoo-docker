# Odoo Custom Addons (v18)

Este repositorio contiene 3 módulos personalizados para Odoo, desarrollados con un enfoque en la extensibilidad del estándar y la integridad de los datos de negocio. Los módulos fueron probados en la version **Community** del sistema.

## Tecnologías y Conceptos Aplicados

* **ORM de Odoo:** Uso de `@api.depends`, `@api.constrains`, y `@api.model`.
* **Herencia (Inheritance):** Extensión del modelo base `res.partner` mediante herencia de clase y de vista (XPath).
* **UX/UI:** Implementación de **Wizards** (`TransientModel`) para flujos de trabajo dinámicos y widgets modernos como `boolean_toggle`.
* **Seguridad:** Lógica de validaciones (`ValidationError`) para evitar estados de cuenta inconsistentes y duplicidad de registros.

---

## Módulos Incluidos

### 1. Gestión de Billetera Virtual

Módulo para la gestión de saldos y transacciones financieras internas vinculadas a contactos.

* **Modelo Core:** `wallet.account` vinculado a `res.partner`.
* **Lógica de Transacciones:** Sistema de depósitos y transferencias con validación de saldo en tiempo real mediante campos computados almacenados (`store=True`).
* **Seguridad Financiera:** * Restricción mediante `_sql_constraints` para asegurar una única billetera por contacto.
* Validación dinámica para impedir transferencias si el saldo disponible es insuficiente.
* **Automatización:** Al realizar una transferencia, el sistema genera automáticamente el asiento de "ingreso" espejo en la cuenta del destinatario.

### 2. Gestión de Miembros de Gimnasio

Sistema para el control de membresías, planes y estados de actividad de socios.

* **Cálculo Automático de Fechas:** Uso de `timedelta` para determinar la fecha de vencimiento basada en la duración del plan seleccionado.
* **Gestión de Planes:** Modelo paramétrico `gym.plan` que permite definir precios, monedas y duraciones personalizadas.
* **Validaciones de Identidad:** * `@api.constrains` para asegurar que el DNI sea numérico y único en la base de datos.
* Control de duplicados para evitar múltiples membresías activas para el mismo contacto.
* **Acciones de UX:** Botón de "Renovación Rápida" que extiende la membresía actual manteniendo la continuidad del socio.

### 3. Extensión de Contactos Estándar

Módulo "puente" para demostrar entendimiento en la capacidad de heredar y expandir módulos base de Odoo sin alterar el código original.

* **Herencia de Modelo:** Se extiende `res.partner` para integrar el estado de socio de forma nativa.
* **Lógica Cross-Module:** Campo computado que analiza todas las membresías vinculadas para determinar si el socio está "Activo" en la vista principal de Contactos.
* **Herencia de Vista (XML):** * Uso de `xpath` para inyectar una nueva pestaña ("Gimnasio") en el `notebook` de la ficha de contactos.
* Implementación de atributos condicionales (`invisible`, `readonly`) para mejorar la interfaz del usuario.
