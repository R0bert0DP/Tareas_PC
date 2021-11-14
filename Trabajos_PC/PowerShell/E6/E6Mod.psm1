function Get-IPConfig {
    Get-NetIPConfiguration -All | Select-Object InterfaceAlias,InterfaceDescription,IPv4Address
}

function Port-Scan {
    param([Parameter(Mandatory)] [string] $network) 
    $portrange = 1..1000
    foreach ($port in $portrange){ 
        Write-Progress “Scanning Ports” $port -PercentComplete (($port/$portrange.Count)*100)
        if(Test-Connection –BufferSize 32 –Count 1 –quiet –ComputerName $network){ 
            $socket = New-Object System.Net.Sockets.TCPClient($network, $port) -ErrorAction "Ignore"
        if($socket.Connected) { 
            “$ip port $port open”
        $socket.Close()
        }
        else { 
            “$ip port $port not open ” 
        }
        }      
    } 
}

function Change-NetworkProfile {
    param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil) 
	$status = Get-NetFirewallProfile -Name $perfil 
	Write-Host "Perfil:" $perfil 
	if($status.enabled){ 
		Write-Host "Status actual: Activado" 
		$opc = Read-Host -Promt "Deseas desactivarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){ 
			Set-NetFirewallProfile -Name $perfil -Enabled False 
		} 
	} else{ 
		Write-Host "Status: Desactivado" 
		$opc = Read-Host -Promt "Deseas activarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){ 
			Write-Host "Activando perfil" 
			Set-NetFirewallProfile -Name $perfil -Enabled True 
		} 
	} 
}