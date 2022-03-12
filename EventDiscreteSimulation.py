#Universidad del Valle de Guatemala
#Algoritmos y Estructuras de Datos - Sección 20
#Mario Antonio Guerra Morales - Carné: 21008
#Fecha de entrega: 11 de marzo de 2022
#Programa de simulación de procesos en intervalos de 10, 5 y 1.

import simpy
import random

def Simulacion(env, proceso, RAM, CPU, duracionproceso, tiempo): #Función para la simulación de procesos.
    global totalProceso #Variable global para el tiempo total de procesos.
    yield env.timeout(tiempo) #Ciclo de reloj para el procesador.
    tiempoActual = env.now #Se graba el tiempo de llegada.
    
    print('%s iniciando instruccion en %d' % (proceso, env.now)) #Inicia la instrucción para el proceso en cuestión.
    
    with CPU.request() as cpu: #Pide el procesador.
        yield cpu 
    
        print('%s iniciando proceso en %s' % (proceso, env.now)) #Inicia a ejecutarse el proceso.
        yield env.timeout(duracionproceso)
        print('%s terminando proceso en %s' % (proceso, env.now)) #Termina de ejecutarse el proceso.
        
        tiempoFinal = env.now - tiempoActual 
        print('%s se tardo %f' % (proceso, env.now)) #Muestra el tiempo promedio.
        totalProceso = totalProceso + tiempoFinal #Tiempo promedio del proceso.

env = simpy.Environment() #Crea el entorno para la simulación.
CPU = simpy.Resource(env, capacity=1) #Se crea el procesador.
RAM = simpy.Container(env, init=10, capacity=100) #Se crea la memoria.
intervalo = 10 #Crea el intervalo.
procesos = 25 #Cantidad de procesos.
totalProceso = 0 #Inicializa el proceso.

for i in range(procesos): 
    env.process(Simulacion(env, 'Proceso %d' % i, RAM, CPU, random.expovariate(1.0/ intervalo), i)) #Crea el proceso.

env.run() #Se ejecuta el proceso.
print('El tiempo promedio es: %d ' % (totalProceso / procesos)) #Imprime el tiempo promedio del proceso.