# PowerShell shutdown script for Meridian Inventory Management System
# Stops both FastAPI server and Vue 3 client

Write-Host "
╔════════════════════════════════════════════════════════════════╗
║   MERIDIAN INVENTORY MANAGEMENT SYSTEM - SHUTDOWN              ║
║                                                                ║
║   Stopping FastAPI server and Vue 3 client...                 ║
╚════════════════════════════════════════════════════════════════╝
" -ForegroundColor Yellow

# Stop processes on port 3000 (Vue client)
Write-Host "Stopping Vue 3 client on port 3000..." -ForegroundColor Cyan
$port3000 = Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue
if ($port3000) {
    foreach ($connection in $port3000) {
        $process = Get-Process -Id $connection.OwningProcess -ErrorAction SilentlyContinue
        if ($process) {
            Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
            Write-Host "  ✓ Stopped process $(process.ProcessName)" -ForegroundColor Green
        }
    }
}

Start-Sleep -Seconds 1

# Stop processes on port 8001 (FastAPI server)
Write-Host "Stopping FastAPI server on port 8001..." -ForegroundColor Cyan
$port8001 = Get-NetTCPConnection -LocalPort 8001 -ErrorAction SilentlyContinue
if ($port8001) {
    foreach ($connection in $port8001) {
        $process = Get-Process -Id $connection.OwningProcess -ErrorAction SilentlyContinue
        if ($process) {
            Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
            Write-Host "  ✓ Stopped process $($process.ProcessName)" -ForegroundColor Green
        }
    }
}

Write-Host "`n
╔════════════════════════════════════════════════════════════════╗
║                  ✓ SERVICES STOPPED                           ║
╚════════════════════════════════════════════════════════════════╝
" -ForegroundColor Green

Write-Host "All services have been stopped." -ForegroundColor Gray
