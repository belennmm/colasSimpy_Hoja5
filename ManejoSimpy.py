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
    print(f"\n\033[36m     •••••••••••• SIMULACIÓN CON {processNum} PROCESOS ••••••••••••\033[0m\n")

    
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
    
def proceso(env, nombre, ramCapacidad, neededRAM, instructions, timeLlegada, velocidad, totalTiem):
    tiempo_inicial = env.now  # el tiempo inicial
    yield env.timeout(timeLlegada)
    

    print(f"{nombre} - requiere {neededRAM} de RAM en el segundo {tiempo_inicial}")  
    
    yield ramCapacidad.get(neededRAM)

    
    instructions_faltantes = instructions
    
    while instructions_faltantes > 0:
        with cpu.request() as req:
            yield req
            
            if instructions_faltantes >= velocidad:
                execute = velocidad
            else:
                execute = instructions_faltantes
            
            yield env.timeout(1)  # tiempo de CPU 
            instructions_faltantes -= execute
    
    yield ramCapacidad.put(neededRAM)
    
    totalTiem.append(env.now - tiempo_inicial)  # el tiemmpo total




# establecer el environment
env = simpy.Environment()
memoria_ram = simpy.Container(env, capacity=RAMcapacity, init=RAMcapacity)
cpu = simpy.Resource(env, capacity=cpuDisp)

# correr la simulación con las siguientes cantidades de procesos
for Numprocesos in [25, 50, 100, 150, 200]:
    simulador(env, Numprocesos)

