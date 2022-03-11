#Universidad del Valle de Guatemala
#Algoritmos y Estructuras de Datos - Sección 20
#Mario Antonio Guerra Morales - Carné: 21008
#Fecha de entrega: 11 de marzo de 2022
#Programa de simulación de procesos en intervalos de 10.

import simpy
import random

def Simulacion(env, proceso, RAM, CPU, duracionproceso, tiempo):
    yield env.timeout(tiempo)
    
    print('%s iniciando instruccion en %d' % (proceso, env.now))
    
    with CPU.request() as cpu:
        yield cpu
    
        print('%s iniciando proceso en %s' % (proceso, env.now))
        yield env.timeout(duracionproceso)
        print('%s terminando proceso en %s' % (proceso, env.now))

env = simpy.Environment()
CPU = simpy.Resource(env, capacity=1)
RAM = simpy.Container(env, init=100, capacity=100)
intervalo = 10
procesos = 25

for i in range(procesos):
    env.process(Simulacion(env, 'Proceso %d' % i, RAM, CPU, random.expovariate(1.0/ intervalo), i*intervalo))

env.run()