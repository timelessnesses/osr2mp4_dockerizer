# fetch chocolately install script

echo "Fetching chocolately install script..."

# set policy to bypass certificate check

Set-ExecutionPolicy Bypass -Scope Process -Force 
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072

# execute installation
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

echo "Done"