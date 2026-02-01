# inputs
import math
import pandas as pd
import numpy as np

# Muestras

# Muestra de sodio a 1 muCi
# masa incial de la muestra en g
mass=1.6E-10
# masa molar (NA 22)
molarmass=21.99
# numero de átomos en la muestra inicial = masa / masa molar * NA
N=mass/molarmass*6.022E23
# constante de tiempo en segundos = segundos por hora * horas por dia * dias por año * vida media en años / log2
Tau=3600*24*365.25*2.6/math.log(2)
# tiempo de observacion en segundos
T=1.0
# distancia del detector a la muestra cm
D=10
# área efectiva de detección cm2
A=100

# Muestra de Rodio a 1 muCi
# masa incial de la muestra en g
mass=1.22E-11
# masa molar (Rh 99)
molarmass=98.91
# numero de átomos en la muestra inicial = masa / masa molar * NA
N=mass/molarmass*6.022E23
# constante de tiempo en segundos = segundos por hora * horas por dia * vida media en dias / log2
Tau=3600*24*16.1/math.log(2)
# tiempo de observacion en segundos
T=1.0
# distancia del detector a la muestra cm
D=10
# área efectiva de detección cm2
A=100


# funciones
def contador(n0,days,tau,d,a,t=1.0,poiss=True):
    # simula el conteo de una muestra puntual
    # n0 = número inicial de partículas
    # days = dias de antiguedad al momento de la observación
    # tau = constante de tiempo
    # d = distancia del detector a la fuente
    # a = área efectiva de detección
    # t = tiempo de toma de datos
    # poiss = boolan True = poisson, False = binomial
    # la función regresa el número de cuentas que recibe el detector
    rng = np.random.default_rng()
    nt=n0*math.exp(-days*3600*24/tau)
    if(poiss):
        cuentas=int(rng.poisson(lam=nt*t/tau)*(a/(4*math.pi*d**2)))
    else:
        cuentas=int(rng.binomial(nt,(1-math.exp(-t/tau)))*(a/(4*math.pi*d**2)))
    return(cuentas)

def toma_muestras(fechas_obs=[],t_obs=[]):
    # simula la toma de varias muestras
    # fechas_obs = antiguedad de la muestra en días
    # t_obs = tiempo de observación en segundos para cada toma de datos
    # len(fechas_obs) debe ser igual a len(t_obs)
    if(len(fechas_obs) != len(t_obs)) : return('Error!: Los arreglos no tienen la misma longitud')
    # definición de la muestra. en esta versión se hace a mano:
    # Muestra de Rodio a 1 muCi
    # masa incial de la muestra en g
    mass=1.22E-11
    # masa molar (Rh 99)
    molarmass=98.91
    # numero de átomos en la muestra inicial = masa / masa molar * NA
    N=mass/molarmass*6.022E23
    # constante de tiempo en segundos = segundos por hora * horas por dia * vida media en dias / log2
    Tau=3600*24*16.1/math.log(2)
    # tiempo de observacion en segundos
    T=1.0
    # distancia del detector a la muestra
    D=10
    # área efectiva de detección
    A=100
    cuentas=[]
    for i in range(len(fechas_obs)):
        cuentas.append((contador(N,fechas_obs[i],Tau,D,A,t=t_obs[i],poiss=False)))
    return(pd.DataFrame({'fecha_obs_dias':fechas_obs,'t_obs_s':t_obs,'cuentas':cuentas}))
