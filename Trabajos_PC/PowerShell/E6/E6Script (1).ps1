# Integrantes:
# Alejandro Cavazos Valdés
# Luis Roberto Díaz Pineda
#El siguiente script tiene como objetivo mostrar tu Ip, encontrar puertos abiertos de los equipos conectados a la red y cambiar el perfil de red
#Le envie la tarea por mensaje en Teams, agregue este comentario para que este enterada y no afecte nuestra calificacion. Saludos y gracias 

$cond = 1

while($cond -ne 0){
    Read-Host -Prompt "Que función deseas usar? [1]IP Configuration [2]Scaner de Puertos [3]Cambiar Perfil de Red [0]Exit"
    if($cond -eq 1){
        Get-IPConfig
    }elseif($cond -eq 2){
        Port-Scan
    }elseif($cond -eq 3){
        Change-NetworkProfile
    }
}

# Fuentes:

# https://techcommunity.microsoft.com/t5/itops-talk-blog/powershell-basics-how-to-scan-open-ports-within-a-network/ba-p/924149
# https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.tcpclient?view=net-5.0
# https://mcpmag.com/articles/2015/05/14/port-checking-using-powershell.aspx