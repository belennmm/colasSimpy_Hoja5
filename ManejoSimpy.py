import simpy
import random

# semilla para generar  la misma secuencia  de numeros aleatorios en cada ejecución 
RANDOM_SEED = 0
random.seed(RANDOM_SEED)

cpuDisp = 1 # cantidad de procesadores

# número de instrucciones por tiempo
InstructionsxTime = 3

numInterval = 10

processNum = 25 # cantidad de procesos que van a ser 

RAMcapacity = 100

# simulación de los procesos
def simulador(env, processNum):
   




# establecer el environment
env = simpy.Environment()