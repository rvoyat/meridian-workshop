#!/usr/bin/env python3
"""
Quick Reference Card for Meridian Inventory Management System
Displays important URLs, commands, and status
"""

import subprocess
from datetime import datetime

REFERENCE_CARD = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   MERIDIAN INVENTORY MANAGEMENT SYSTEM - QUICK REFERENCE                     ║
║                                                                               ║
║   Engagement: RFP MC-2026-0417 | Accenture Modernization Practice            ║
║   Setup Date: April 27, 2026 | Status: ✓ READY FOR DEVELOPMENT              ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  🌐 SERVICES & URLS                                                          ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  Frontend (Vue 3 + Vite):              http://localhost:3000                 ║
║  Backend (FastAPI + Uvicorn):          http://localhost:8001                 ║
║  API Documentation (Swagger):          http://localhost:8001/docs            ║
║  API Documentation (ReDoc):            http://localhost:8001/redoc           ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ⚡ QUICK START COMMANDS                                                      ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  PowerShell (Recommended):                                                   ║
║    .\start_dev.ps1                     # Start all services                  ║
║    .\stop_dev.ps1                      # Stop all services                   ║
║                                                                               ║
║  Bash/Linux/Mac:                                                             ║
║    ./scripts/start.sh                  # Start all services                  ║
║    ./scripts/stop.sh                   # Stop all services                   ║
║                                                                               ║
║  Manual Startup:                                                             ║
║    cd server && python main.py         # Terminal 1: Backend                 ║
║    cd client && npm run dev            # Terminal 2: Frontend                ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  📋 KEY ENDPOINTS                                                            ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  GET  /api/dashboard/summary           # Dashboard metrics                   ║
║  GET  /api/inventory                   # Inventory items                     ║
║  GET  /api/orders                      # Customer orders                     ║
║  GET  /api/demand                      # Demand forecasts                    ║
║  GET  /api/spending/summary            # Spending overview                   ║
║  GET  /api/backlog                     # Backlog items                       ║
║                                                                               ║
║  Filter Parameters:                                                          ║
║    ?warehouse=SF|London|Tokyo          # Filter by warehouse                 ║
║    ?category=sensors|controllers|...   # Filter by product category          ║
║    ?status=pending|completed           # Filter by order status              ║
║    ?month=2025-04|Q2-2025              # Filter by month/quarter             ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  📁 PROJECT STRUCTURE                                                        ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  /client                  Vue 3 frontend (Vite bundler)                      ║
║  /server                  FastAPI backend                                    ║
║  /tests                   Test suite (Pytest + Cypress)                      ║
║  /docs/rfp                RFP documentation                                  ║
║  /scripts                 Startup/shutdown scripts                           ║
║                                                                               ║
║  Key Files:                                                                  ║
║    SETUP_GUIDE.md                     Comprehensive setup guide              ║
║    SETUP_COMPLETE.md                  Setup completion summary               ║
║    PROPOSAL.md                        Engagement proposal                    ║
║    CAPABILITIES_DECK*.pptx            Presentation decks                     ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  🔧 DEVELOPMENT COMMANDS                                                     ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  Frontend:                                                                   ║
║    npm run dev            # Start development server                         ║
║    npm run build          # Build for production                             ║
║    npm run preview        # Preview production build                         ║
║                                                                               ║
║  Backend:                                                                    ║
║    python main.py         # Start FastAPI server                             ║
║    python mock_data.py    # Generate mock data                               ║
║                                                                               ║
║  Testing:                                                                    ║
║    pytest -v              # Run all backend tests                            ║
║    pytest -k keyword      # Run tests matching keyword                       ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  📊 ENGAGEMENT ROADMAP (May 1–31, 2026)                                     ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  Phase 1 (Week 1): Reports Module Fixes + Test Framework                    ║
║    • Cypress E2E test framework setup                                         ║
║    • Audit & fix 8 Reports module defects                                     ║
║    • CI/CD pipeline configuration (GitHub Actions)                            ║
║    ✓ Checkpoint: IT approval of test framework                               ║
║                                                                               ║
║  Phase 2 (Week 2): Restocking Recommendations Engine                         ║
║    • Design recommendation algorithm                                          ║
║    • Build /api/recommendations endpoint                                      ║
║    • Create Restocking.vue component                                          ║
║    • E2E test coverage for Restocking                                         ║
║    ✓ Checkpoint: R. Tanaka validates feature                                 ║
║                                                                               ║
║  Phase 3 (Week 3): Architecture & Documentation                              ║
║    • Architecture overview documentation                                      ║
║    • Maintenance manual & operations runbook                                  ║
║    • Technology roadmap & improvement recommendations                         ║
║    • Optional enhancements (i18n, UI, dark mode)                              ║
║    ✓ Delivery: Complete system ready for IT handoff                          ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ⚠️  KNOWN ISSUES (Reports Module)                                          ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  1. Filter Behavior — Date range filters not persisting                      ║
║  2. Category Filter — Some categories missing from dropdown                   ║
║  3. Warehouse Filter — London data sometimes missing                          ║
║  4. Internationalization — Japanese labels incomplete                         ║
║  5. Data Aggregation — Inconsistent spending calculations                     ║
║  6. Export Function — CSV export missing columns                              ║
║  7. Loading State — UI not displaying loading indicator                       ║
║  8. Pagination — Page navigation broken on large datasets                     ║
║                                                                               ║
║  ➜ All issues will be fixed in Phase 1 with test-driven approach             ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  📚 DOCUMENTATION                                                            ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  SETUP_GUIDE.md            Complete setup & architecture guide               ║
║  client/CLAUDE.md          Frontend development guidelines                    ║
║  server/CLAUDE.md          Backend development guidelines                     ║
║  docs/rfp/MC-2026-0417.md  RFP specification                                 ║
║  docs/rfp/vendor-handoff.md Technical handoff notes                          ║
║  tests/TEST_SUMMARY.md      Test status report                               ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  💰 ENGAGEMENT DETAILS                                                       ║
║  ────────────────────────────────────────────────────────────────────────    ║
║                                                                               ║
║  Investment:     $78,000 fixed-fee                                            ║
║  Duration:       3 weeks (May 1–31, 2026)                                    ║
║  Client:         Meridian Components, Inc.                                    ║
║  Team:           Lead Engineer, QA Automation, Junior Dev, Engagement Mgr    ║
║  Locations:      San Francisco (HQ), London, Tokyo (3 warehouses)            ║
║                                                                               ║
║  Payment Schedule:                                                            ║
║    • 33% ($25,740) — May 1 (engagement start)                                ║
║    • 33% ($25,740) — End of Week 2 (Restocking complete)                     ║
║    • 34% ($26,520) — May 31 (final delivery)                                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

TIP: Save this file for quick reference during development!
For more details, see SETUP_GUIDE.md or PROPOSAL.md
"""

if __name__ == "__main__":
    print(REFERENCE_CARD)
    print(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Status: ✓ System ready for development")
