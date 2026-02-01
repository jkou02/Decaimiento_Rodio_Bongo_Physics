# 📊 Análisis de Decaimiento Radiactivo - Rodio-99

Proyecto de análisis computacional del decaimiento radiactivo del isótopo Rodio-99 (Rh-99) mediante técnicas de regresión lineal y visualización de datos.

**Curso**: El Bongo Physics - Curso Cero  
**Autor**: Jkou  
**Fecha**: Enero 2026

---

## 🎯 Objetivo

Determinar experimentalmente la constante de decaimiento (λ) y el tiempo de vida media (T₁/₂) de un isótopo radiactivo a partir de datos simulados de conteo de partículas.

## 📁 Estructura del Proyecto

``` Plaintext
Decaimiento_cursoCero/
├── data/
│   └── muestras.csv          # Datos crudos o generados
├── scripts/
│   └── decaimiento.py        # Funciones y lógica matemática
├── notebooks/
│   └── Adquirir_datos.ipynb  # Análisis, gráficas y resultados
├── .gitignore                # Excluye entornos virtuales y archivos temporales
├── README.md                 # Documentación del proyecto
└── requirements.txt          # Lista de librerías (numpy, matplotlib, etc.)
```

## 🔬 Metodología

### 1. Generación de Datos
Se simulan mediciones de decaimiento radiactivo utilizando el módulo `decaimiento.py`:
- Muestra inicial: Rodio-99 (1 µCi)
- Intervalo de observación: 0-90 días
- Tiempo de medición: 10 segundos por muestra

### 2. Análisis Matemático
El decaimiento radiactivo sigue la ley exponencial:

```
A(t) = A₀ · e^(-λt)
```

Aplicando logaritmo natural para linearizar:

```
ln(A(t)) = ln(A₀) - λt
```

### 3. Regresión Lineal
Se utiliza `scipy.stats.linregress` para determinar:
- **Pendiente (m)**: Constante de decaimiento λ
- **Intercepto (b)**: ln(A₀)
- **R²**: Calidad del ajuste

### 4. Cálculo de Vida Media

```
T₁/₂ = ln(2) / λ
```

## 📊 Resultados

| Parámetro | Valor Obtenido |
|-----------|----------------|
| λ (constante de decaimiento) | 0.04304 ± 0.00005 día⁻¹ |
| T₁/₂ (vida media) | 16.10 días |
| R² (ajuste) | 0.999994 |
| **Isótopo identificado** | **Rodio-99** |

> **Nota**: Valor teórico de T₁/₂ para Rh-99 = 16.1 días

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.12 o superior
- pip (gestor de paquetes)

### 1. Clonar el repositorio

```sh
git clone [URL_del_repositorio]
cd Decaimiento_cursoCero
```

### 2. Crear entorno virtual (recomendado)

```sh
python -m venv venv-Bongo
source venv-Bongo/bin/activate  # Linux/macOS
# venv-Bongo\Scripts\activate  # Windows
```

### 3. Instalar dependencias

```sh
pip install -r requirements.txt
```

### 4. Ejecutar análisis

```sh
jupyter notebook Adquirir_datos.ipynb
```

## 📦 Dependencias Principales

- **NumPy**: Operaciones matemáticas y logaritmos
- **Pandas**: Manipulación de datos tabulares
- **Matplotlib**: Visualización de gráficos
- **SciPy**: Regresión lineal y análisis estadístico
- **Jupyter**: Entorno de notebooks interactivos

Ver `requirements.txt` para versiones específicas.

## 📈 Visualizaciones Generadas

1. **Gráfico de datos simulados**: Decaimiento exponencial en escala normal
2. **Gráfico logarítmico**: Linearización de datos para regresión
3. **Curva de ajuste**: Comparación entre datos y modelo teórico

## 🧪 Estructura del Notebook

```python
1. Importación de librerías
2. Configuración de parámetros físicos
3. Generación de datos simulados
4. Transformación logarítmica
5. Regresión lineal
6. Cálculo de vida media
7. Visualización de resultados
```

## 📝 Notas Importantes

- Los datos son **simulados** mediante `decaimiento.py`, no mediciones experimentales reales
- El modelo asume decaimiento puro sin factores de corrección
- La incertidumbre estadística sigue distribución de Poisson
- Se recomienda usar este código con fines educativos

## 🔍 Validación de Resultados

El valor obtenido (T₁/₂ = 16.10 días) coincide con el valor de referencia del Rodio-99, validando:
- ✅ Correcta implementación del modelo
- ✅ Precisión de la regresión lineal
- ✅ Identificación correcta del isótopo

## 🛠️ Posibles Mejoras

- [ ] Implementar análisis de incertidumbre propagada
- [ ] Añadir comparación con múltiples isótopos
- [ ] Incluir correcciones por tiempo muerto del detector
- [ ] Implementar método de Monte Carlo para validación

## 📧 Contacto

Para preguntas o sugerencias sobre este proyecto:
- **Email**: jstb2720@gmail.com

## 📄 Licencia

Este proyecto es de uso educativo.

---

**Última actualización**: Enero 2026  
**Versión**: 1.0.0