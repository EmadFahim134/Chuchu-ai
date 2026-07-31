# Getting into Modules:
Set-Location Modules

# Insure:
Write-Host "Insure that you (User) Installed uv (Python Virtual Env manager)!"
Start-Sleep -Seconds 3

# Ask for Gemini API Key:
$apiKeyInput = Read-Host "Enter your Google Gemini API Key"

# Check if the key is present
if ([string]::IsNullOrWhiteSpace($apiKeyInput)) {
    Write-Host "Error: No API key provided. Exiting." -ForegroundColor Red
    exit 1
} else {
    Write-Host "API key received successfully!" -ForegroundColor Green
    $env:GEMINI_API_KEY = $apiKeyInput

    # Run Project:
    uv -v run ui.py
}
