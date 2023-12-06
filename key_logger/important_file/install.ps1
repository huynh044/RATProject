function random_text {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}

$folder = random_text
$path = $env:TEMP
$inital_path = pwd

cd $path
mkdir $folder
cd $folder
echo " " > test.txt

cd $inital_path
del install.ps1

