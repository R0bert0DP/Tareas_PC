$select = 1
while($select -ne 0){
    $select = Read-Host -Prompt "---Bienvenido al sistema de configuración de Firewall---`nQue desea hacer `n[1]Ver Status `n[2]Cambiar Status `n[3]Ver Perfil de red actual `n[4]Cambiar Perfil de Red Actual `n[5]Ver Reglas de Bloqueo `n[6]Agregar Reglas de Bloqueo `n[7]Eliminar Reglas de Bloqueo? `n[0]Salir"
    switch($select){
        1 {
            Ver-StatusPerfil  
        } 2 {
            Cambiar-StatusPerfil
        } 3 {
            Ver-PerfilRedActual
        } 4 {
            Cambiar-PerfilRedActual
        } 5 {
            Ver-ReglasBloqueo
        } 6 {
            Agregar-ReglasBloqueo
        } 7 {
            Eliminar-ReglasBloqueo
        }
    }
}
