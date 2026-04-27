# MERIDIAN INVENTORY MANAGEMENT SYSTEM - SETUP GUIDE

## ✅ Codebase Status

**Setup Date:** April 27, 2026  
**Status:** ✓ READY FOR DEVELOPMENT

### Services Running
- ✓ **FastAPI Server** — http://localhost:8001
- ✓ **Vue 3 Client** — http://localhost:3000
- ✓ **API Mock Data** — Loaded and responding

---

## 🚀 Quick Start

### Option 1: Using Startup Scripts (Recommended)

**Windows PowerShell:**
```powershell
.\start_dev.ps1
```

**Bash/Linux/Mac:**
```bash
./start.sh
```

Both scripts will:
1. ✓ Start the FastAPI server (port 8001)
2. ✓ Start the Vue 3 client (port 3000)
3. ✓ Display URLs and access information

### Option 2: Manual Startup

**Terminal 1 - Server:**
```powershell
Set-Location "server"
python main.py
# Server runs on http://localhost:8001
# API Docs: http://localhost:8001/docs
```

**Terminal 2 - Client:**
```powershell
Set-Location "client"
npm run dev
# Client runs on http://localhost:3000
```

---

## 📋 System Requirements

- **Python:** 3.10+ (check: `python --version`)
- **Node.js:** 16+ (check: `node --version` and `npm --version`)
- **Ports Available:** 3000 (frontend), 8001 (backend)

## 🔧 Environment Details

### Backend (FastAPI)

**Framework:** FastAPI 0.110+  
**Server:** Uvicorn  
**Port:** 8001  
**Data:** JSON files (mock data)

**Installed Packages:**
```
fastapi>=0.110.0
uvicorn>=0.24.0
pydantic>=2.5.0
```

**Key Directories:**
- `server/main.py` — FastAPI application & routes
- `server/mock_data.py` — Mock data generator
- `server/data/` — JSON mock data files
  - `inventory.json` — Inventory items
  - `orders.json` — Customer orders
  - `demand_forecasts.json` — 90-day demand
  - `backlog_items.json` — Backlog items
  - `spending.json` — Spending data
  - `transactions.json` — Recent transactions
  - `purchase_orders.json` — Purchase orders

**API Documentation:**
```
http://localhost:8001/docs          # Swagger UI
http://localhost:8001/redoc         # ReDoc
```

**Available Endpoints:**
- `GET /api/inventory` — Inventory items (filterable by warehouse, category)
- `GET /api/orders` — Customer orders (filterable by warehouse, category, status, month)
- `GET /api/dashboard/summary` — Dashboard summary metrics
- `GET /api/demand` — Demand forecasts (all items)
- `GET /api/backlog` — Backlog items
- `GET /api/spending/*` — Spending endpoints (summary, monthly, categories, transactions)

### Frontend (Vue 3 + Vite)

**Framework:** Vue 3 (Composition API)  
**Bundler:** Vite  
**Port:** 3000  
**Router:** Vue Router  
**HTTP Client:** Axios

**Installed Packages:**
```
vue@^3.4.21
vue-router@^4.3.0
axios@^1.6.7
vite@^5.2.0
@vitejs/plugin-vue@^5.0.4
```

**Key Directories:**
- `client/src/main.js` — Vue app entry point
- `client/src/App.vue` — Root component
- `client/src/views/` — Page components
  - `Dashboard.vue` — Overview page
  - `Inventory.vue` — Inventory management
  - `Orders.vue` — Order management
  - `Spending.vue` — Spending analysis
  - `Reports.vue` — Reports page (HAS KNOWN DEFECTS)
  - `Demand.vue` — Demand forecasting
  - `Backlog.vue` — Backlog management
- `client/src/components/` — Reusable components
- `client/src/composables/` — Vue composition functions
  - `useAuth.js` — Authentication logic
  - `useFilters.js` — Filter state management
  - `useI18n.js` — Internationalization
- `client/src/locales/` — Language files (en.js, ja.js)

**Development Commands:**
```bash
npm run dev      # Start dev server on http://localhost:3000
npm run build    # Build for production
npm run preview  # Preview production build
```

---

## 🔍 Project Structure

```
meridian-workshop/
├── PROPOSAL.md                          # Professional proposal document
├── CAPABILITIES_DECK.md                 # Capabilities presentation (markdown)
├── CAPABILITIES_DECK.pptx               # Capabilities presentation (PowerPoint)
├── CAPABILITIES_DECK_PORTLE_STYLE.pptx # Portle-styled presentation
├── README.md                            # Project overview
├── CLAUDE.md                            # This file
│
├── client/                              # Vue 3 Frontend (Vite)
│   ├── package.json                     # npm dependencies
│   ├── vite.config.js                   # Vite configuration
│   ├── index.html                       # HTML entry point
│   ├── CLAUDE.md                        # Frontend guidelines
│   ├── src/
│   │   ├── main.js                      # Vue app initialization
│   │   ├── App.vue                      # Root component
│   │   ├── api.js                       # Axios API client
│   │   ├── views/                       # Page components
│   │   ├── components/                  # Reusable components
│   │   ├── composables/                 # Vue composition functions
│   │   └── locales/                     # i18n language files
│
├── server/                              # FastAPI Backend
│   ├── main.py                          # FastAPI application & routes
│   ├── mock_data.py                     # Mock data generator
│   ├── requirements.txt                 # Python dependencies
│   ├── pyproject.toml                   # Python project metadata
│   ├── CLAUDE.md                        # Backend guidelines
│   └── data/                            # JSON mock data files
│       ├── inventory.json
│       ├── orders.json
│       ├── demand_forecasts.json
│       ├── backlog_items.json
│       ├── spending.json
│       ├── transactions.json
│       └── purchase_orders.json
│
├── tests/                               # Test Suite
│   ├── pytest.ini                       # Pytest configuration
│   ├── README.md                        # Testing guidelines
│   ├── TEST_SUMMARY.md                  # Test status report
│   └── backend/                         # Backend tests
│       ├── conftest.py                  # Test fixtures
│       ├── test_dashboard.py
│       ├── test_inventory.py
│       └── test_misc_endpoints.py
│
├── docs/                                # Documentation
│   └── rfp/                             # RFP documents
│       ├── MC-2026-0417.md              # RFP specification
│       ├── meridian-background.md       # Client background
│       └── vendor-handoff.md            # Technical handoff notes
│
├── scripts/                             # Utility scripts
│   ├── start.sh                         # Bash startup script
│   ├── stop.sh                          # Bash shutdown script
│   ├── start_dev.ps1                    # PowerShell startup script
│   └── stop_dev.ps1                     # PowerShell shutdown script
│
└── proposal/                            # Proposal artifacts
```

---

## 🐛 Known Issues (Current State)

### Reports Module Defects (8 documented issues)
1. **Filter Behavior** — Date range filters not persisting across navigation
2. **Category Filter** — Some product categories missing from dropdown
3. **Warehouse Filter** — London warehouse data sometimes missing in reports
4. **Internationalization** — Japanese labels incomplete in Reports view
5. **Data Aggregation** — Spending summary calculations showing inconsistent totals
6. **Export Function** — CSV export missing columns
7. **Loading State** — UI not displaying proper loading indicator
8. **Pagination** — Page navigation broken on large datasets

### Test Coverage
- ⚠️ **No automated browser tests** (E2E/Cypress)
- ⚠️ **No unit test coverage** for existing components
- ⚠️ **Limited backend test coverage**

See `tests/TEST_SUMMARY.md` for detailed test status.

---

## 📝 Engagement Roadmap (May 1–31, 2026)

### Phase 1 (Week 1) — Testing & Reports Remediation
- Set up Cypress E2E test framework
- Audit & fix all 8 Reports module defects
- Establish CI/CD pipeline
- **Checkpoint:** IT approval of test framework

### Phase 2 (Week 2) — Restocking Engine
- Design & implement Restocking recommendations algorithm
- Build `/api/recommendations` endpoint
- Create Restocking.vue component
- Add E2E test coverage for Restocking flows
- **Checkpoint:** R. Tanaka's team validates feature

### Phase 3 (Week 3) — Documentation & Handoff
- Document architecture overview
- Create maintenance manual & operations runbook
- Prepare technology roadmap
- Implement optional enhancements (i18n, UI, dark mode)
- **Delivery:** Complete system ready for IT handoff

---

## 🛠️ Development Workflow

### Adding a New Feature

1. **Create component** in `client/src/components/`
2. **Add API endpoint** in `server/main.py`
3. **Update mock data** in `server/data/` if needed
4. **Add E2E test** (Cypress, post-Phase 1)
5. **Document** in corresponding CLAUDE.md file

### Debugging

**Frontend Issues:**
```
http://localhost:3000 → Browser DevTools → Network/Console tabs
Check client/src/api.js for API calls
```

**Backend Issues:**
```
http://localhost:8001/docs → Swagger UI (test endpoints interactively)
Check server/main.py for route definitions
Check server/mock_data.py for data structure
```

### Running Backend Tests

```powershell
Set-Location tests
pytest -v                    # Run all tests
pytest test_dashboard.py -v  # Run specific test file
pytest -k "inventory" -v     # Run tests matching keyword
```

---

## 🚦 Health Check

**Verify system is running:**

```powershell
# Check backend
curl http://localhost:8001/api/dashboard/summary

# Check frontend (in browser)
http://localhost:3000

# Check API docs
http://localhost:8001/docs
```

Expected responses:
- ✓ Backend returns JSON summary data
- ✓ Frontend loads without errors
- ✓ Swagger docs page loads

---

## 📞 Support & Documentation

- **RFP Specification:** See `docs/rfp/MC-2026-0417.md`
- **Technical Handoff:** See `docs/rfp/vendor-handoff.md`
- **Frontend Guide:** See `client/CLAUDE.md`
- **Backend Guide:** See `server/CLAUDE.md`
- **Test Status:** See `tests/TEST_SUMMARY.md`

---

## ⚡ Next Steps

1. **✓ Codebase Setup Complete** — Ready for development
2. **→ Phase 1 Tasks:**
   - [ ] Set up Cypress test framework
   - [ ] Audit Reports module defects
   - [ ] Implement test-driven fixes
   - [ ] Configure CI/CD pipeline

3. **Phase 2 Tasks:**
   - [ ] Design Restocking algorithm
   - [ ] Build API endpoint
   - [ ] Create Restocking UI component
   - [ ] E2E test coverage

4. **Phase 3 Tasks:**
   - [ ] Architecture documentation
   - [ ] Maintenance manual
   - [ ] Operations runbook
   - [ ] Optional feature implementation

---

**Setup Date:** April 27, 2026  
**Last Updated:** April 27, 2026  
**Status:** ✓ READY FOR DEVELOPMENT

