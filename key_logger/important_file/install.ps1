function random_text {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}

$folder = random_text
$path = "$env:TEMP/$folder"
$inital_path = $pwd


mkdir $path
cd $path
echo " " > test.txt

cd $inital_path
