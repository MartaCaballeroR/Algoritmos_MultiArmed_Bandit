# Algoritmos Multi-Armed Bandit: Estudio y aplicación al diseño de circuitos lógicos

### Descripción del proyecto

Este trabajo se centra en el estudio, implementación y evaluación de algoritmos de aprendizaje por refuerzo del tipo Multi-Armed Bandit (MAB), aplicados al análisis 
de circuitos lógicos con recompensas estocásticas. Se compara el rendimiento de tres algoritmos representativos: epsilon-greedy, Upper Confidence Bound (UCB) y Thompson 
Sampling, con el objetivo de analizar sus diferencias en términos de exploración, explotación y eficiencia de aprendizaje.

En primer lugar, se realiza una revisión teórica del problema bandit, analizando los conceptos fundamentales de exploración y explotación, agente y entorno, que 
sirven como base conceptual del estudio. Posteriormente, se diseñan y ejecutan pruebas experimentales en distintos escenarios configurables, lo que permite evaluar 
el comportamiento de los algoritmos bajo diferentes condiciones.

En la fase experimental se analizan métricas como la recompensa acumulada y la convergencia hacia la opción óptima, así como la influencia de los parámetros de cada 
algoritmo.

Finalmente, se desarrolla una simulación final en Python que modela el problema planteado y permite la experimentación interactiva por parte del usuario. Esta 
herramienta integra los algoritmos implementados y facilita la visualización de sus métricas de rendimiento. Los resultado obtenidos muestran diferencias 
significativas entre los enfoques estudiados y evidencian la aplicabilidad de los métodos MAB en problemas de decisión discreta.

### Algoritmos implementados

* __Epsilon-greedy__: estrategia que implementa la exploración y la explotación mediante un parámetro de probabilidad.
* __Upper Confidence Bound (UCB)__: algoritmo que utiliza un índice de confianza para seleccionar las opciones.
* __Thompson Sampling__: método probabilístico que utiliza distribuciones de probabilidad para tomar decisiones.

### Documentación
El documento completo del Trabajo de Fin de Grado está disponible en formato PDF: [Consultar TFG Completo](https://burjcdigital.urjc.es/items/5de3effd-ed30-4f49-8245-96fe195cac78)
