function random_text {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}

$path_current = pwd

$path = "$env:TEMP"
$folder = random_text

cd $path
mkdir $folder
cd $folder







