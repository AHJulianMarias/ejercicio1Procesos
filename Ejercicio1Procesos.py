import psutil

notepadPid = None
# Iteramos para encontrar el proceso del bloc de notas
# fmt:off
print(f"\nImprimiendo procesos con el formato NOMBRE , PID")
# fmt:on
for proc in psutil.process_iter(["name", "pid", "memory_percent", "cpu_times"]):
    # fmt:off
    #No estoy muy seguro de que sea cpu times
    print(f"Name: {proc.info["name"]}\tPID: {proc.info["pid"]}\tMemory usage:{round(proc.info["memory_percent"],2)}%\tCPU usage: {round(proc.info["cpu_times"].system,2)}")
    # fmt:on
    if proc.info["name"].lower() == "notepad.exe":
        # Al encontrarlo, asignamos el pid a la variable declarada anteriormente como None
        notepadPid = proc.info["pid"]

# Si notepadPid es None, significa que el bloc de notas no esta en ejecución
if notepadPid != None:
    # fmt:off
    print(f"\nEl bloc de notas esta en ejecucion con el id {notepadPid}")
else:
    # fmt:off
    print(f"\nEl bloc de notas no se encuentra en ejecución")
    # fmt : on

# dentro de un while True para obligar a que se cumple correctamente esta parte del codigo
while True:
    pidTerminar = None
    try:
        # Si introduces un string en vez de un numero, salta la excepción
        pidTerminar = int(input("\n¿Qué proceso quieres terminar?\n"))
        # Si no salta la excepción salimos del bucle
        break
    except ValueError:
        # El comentario que incluye fmt: off/on es para desactivar el formatter que me hace cosas raras si no
        # fmt: off
        print(f"El valor introducido es diferente a un numero, introduce un número por favor.")
        # fmt: on

    except Exception as e:
        # Si es un error diferente a ValueError, capturamos la excepcion para poder realizar mejor control en un futuro
        # fmt:off
        print(f"Error inesperado {e}")

# Mismo proceso de antes, nombre del proceso en None si en algun momento dentro del bucle capturamos el nombre, es por que se ha podido terminar el proceso
procName = None
for proc in psutil.process_iter(["name", "pid"]):
    if proc.info["pid"] == pidTerminar:
        try:
            proc.terminate()
            procName = proc.info["name"]
            # Una vez encontrado y parado el proceso, frenamos la ejecucion del bucle, no lo necesitamos mas
            break
        except Exception as e:
            # fmt:off
            print(f"No se ha podido parar el proceso, ERROR: {e}")
# Si hemos terminado el proceso, el nombre del proceso sera diferente a None, en caso de que no hayamos termiando el proceso es por que no se encontraba ese pid
if procName != None:
    # fmt:off
    print(f"Proceso {procName}, con pid {pidTerminar} parado correctamente.")
else:
    # fmt:off
    print(f"Numero de proceso ({pidTerminar}) no encontrado.")
