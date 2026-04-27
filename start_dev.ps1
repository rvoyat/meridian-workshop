# PowerShell startup script for Meridian Inventory Management System
# Run from root directory: .\start_dev.ps1

Write-Host "
╔════════════════════════════════════════════════════════════════╗
║   MERIDIAN INVENTORY MANAGEMENT SYSTEM - DEVELOPMENT SETUP     ║
║                                                                ║
║   Starting FastAPI server and Vue 3 client...                 ║
╚════════════════════════════════════════════════════════════════╝
" -ForegroundColor Cyan

# Check if Node.js is installed
try {
    $nodeVersion = npm --version
    Write-Host "✓ Node.js/npm is installed (version: $nodeVersion)" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js is not installed. Please install Node.js 16+ and try again." -ForegroundColor Red
    exit 1
}

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "✓ Python is installed ($pythonVersion)" -ForegroundColor Green
} catch {
    Write-Host "✗ Python is not installed. Please install Python 3.10+ and try again." -ForegroundColor Red
    exit 1
}

# Check if required ports are available
$portsOK = $true
$ports = @(3000, 8001)

foreach ($port in $ports) {
    $netstat = netstat -ano | findstr ":$port"
    if ($netstat) {
        Write-Host "⚠ Port $port is already in use." -ForegroundColor Yellow
        $portsOK = $false
    }
}

if (-not $portsOK) {
    Write-Host "`nTo stop existing processes, run: .\stop_dev.ps1" -ForegroundColor Yellow
    Write-Host "Or continue at your own risk..." -ForegroundColor Yellow
}

Write-Host "`n📂 Project Structure:" -ForegroundColor Cyan
Write-Host "  • Frontend: client/ (Vue 3 + Vite)"
Write-Host "  • Backend: server/ (FastAPI + Uvicorn)"
Write-Host "  • Tests: tests/ (Pytest + Cypress)"

Write-Host "`n🚀 Starting services...`n" -ForegroundColor Cyan

# Create two new terminals/processes for server and client
Write-Host "1️⃣  Starting FastAPI Server on http://localhost:8001" -ForegroundColor Green
$serverPath = Join-Path (Get-Location) "server"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$serverPath'; Write-Host 'FastAPI Server starting...'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "2️⃣  Starting Vue 3 Client on http://localhost:3000" -ForegroundColor Green
$clientPath = Join-Path (Get-Location) "client"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$clientPath'; Write-Host 'Vue 3 Client starting...'; npm run dev" -WindowStyle Normal

Start-Sleep -Seconds 3

Write-Host "`n
╔════════════════════════════════════════════════════════════════╗
║                    ✓ SERVICES STARTED                         ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  🌐 Frontend:  http://localhost:3000                          ║
║  📡 Backend:   http://localhost:8001                          ║
║  📖 API Docs:  http://localhost:8001/docs                     ║
║                                                                ║
║  📁 Mock Data:  server/data/*.json                            ║
║  🧪 Tests:      pytest tests/                                 ║
║                                                                ║
║  ⚙️  To stop services, close the terminal windows or run:      ║
║     .\stop_dev.ps1                                            ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
" -ForegroundColor Green

Write-Host "Press Ctrl+C in this window to exit." -ForegroundColor Gray
