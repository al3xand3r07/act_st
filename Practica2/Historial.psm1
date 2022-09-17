#Este modulo solo funciona en Sistema Operativo Windows
function Get-LogHistorial {
    #Esta funcion tiene como objetivo dividir los logs del sistema y colocarlos en un archivo txt para su posterior revision
    $t = Get-TiempoEpoch
    if (-not (Test-Path "$env:USERPROFILE\Documents\SystemLogs")){
        New-Item "$env:USERPROFILE\Documents\SystemLogs" -ItemType Directory | Out-Null
    }
    Get-Eventlog system -Newest 30 | Where-Object { $_.entrytype -eq "warning" } | Format-Table -AutoSize | Out-File "$env:USERPROFILE\Documents\SystemLogs\Warning-$t.txt"
    Get-Eventlog system -Newest 30 | Where-Object { $_.entrytype -eq "error" } | Format-Table -AutoSize | Out-File "$env:USERPROFILE\Documents\SystemLogs\Error-$t.txt"
    Get-Eventlog system -Newest 30 | Where-Object { $_.entrytype -eq "information" } | Format-Table -AutoSize | Out-File "$env:USERPROFILE\Documents\SystemLogs\Information-$t.txt"
}
