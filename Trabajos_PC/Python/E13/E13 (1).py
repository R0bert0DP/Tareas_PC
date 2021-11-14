import subprocess

print("Get-Command\nGet-Process\nGip")

comando = input("Escriba el comando a utilizar: ")
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())

x = input("¿desea utilizar otro comando? Y/N").lower()
while x == 'y':
    comand = input("Escribe el comando: ")
    linePS = "powershell -Executionpolicy ByPass -Command "+ comand
    runningProcesses = subprocess.check_output(linePS)
    print(runningProcesses.decode())

    x = input("¿desea utilizar un comando de aqui? Y/N").lower()
else:
    print("HASTA LUEGO!!!")
