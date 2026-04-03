Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"
$screenshotPath = Join-Path $projectRoot "llm_conversation.png"

$process = Start-Process `
    -FilePath "cmd.exe" `
    -ArgumentList "/k", "`"$pythonExe`" LLM.py" `
    -WorkingDirectory $projectRoot `
    -PassThru

Start-Sleep -Seconds 5

$shell = New-Object -ComObject WScript.Shell
$null = $shell.AppActivate($process.Id)
Start-Sleep -Milliseconds 800

[System.Windows.Forms.SendKeys]::SendWait("Hello{ENTER}")
Start-Sleep -Seconds 25
[System.Windows.Forms.SendKeys]::SendWait("quit{ENTER}")
Start-Sleep -Seconds 2

$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
$bitmap.Save($screenshotPath, [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose()
$bitmap.Dispose()

if (-not $process.HasExited) {
    $process.CloseMainWindow() | Out-Null
    Start-Sleep -Seconds 1
}

if (-not $process.HasExited) {
    Stop-Process -Id $process.Id
}

Write-Output "Saved screenshot to $screenshotPath"
