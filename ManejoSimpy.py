import simpy
import random
import statistics

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
    

    
    totalTiem = []
    
    for i in range(processNum):
        neededRAM = random.randint(1, 10)
        instructions = random.randint(1, 10)
        timeLlegada = random.expovariate(1.0 / numInterval)
        env.process(proceso(env, f"Proceso { i+1 }", memoria_ram, neededRAM, instructions, timeLlegada, cpuDisp, totalTiem))
     
    env.run()
    
    # calcular el tiempo promedio y la desviación estándar 
    promTime = statistics.mean(totalTiem)
    desVest = statistics.stdev(totalTiem)
    
    print(f"\n\033[1;34m     -------------------------------------------\033[0m")
    print(f"        Tiempo promedio: {promTime:.2f} seconds")
    print(f"        Desviación Estándar: {desVest:.2f} (seconds)")
    print(f"\033[1;34m     -------------------------------------------\033[0m\n")



# establecer el environment
env = simpy.Environment()
memoria_ram = simpy.Container(env, capacity=RAMcapacity, init=RAMcapacity)
cpu = simpy.Resource(env, capacity=cpuDisp)
