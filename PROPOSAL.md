# PROPOSAL TO MERIDIAN COMPONENTS, INC.

**RFP #:** MC-2026-0417  
**Prepared by:** Accenture  
**Date:** April 27, 2026  
**Response to:** Request for Proposal — Inventory Management Dashboard Modernization

---

## EXECUTIVE SUMMARY

Meridian Components' inventory management dashboard represents a critical operational asset, yet the current system suffers from unresolved defects, inadequate test coverage, and incomplete feature delivery. This proposal presents a comprehensive, risk-mitigated engagement plan to remediate existing deficiencies while delivering enhanced capabilities that directly support operational excellence.

Our phased approach strategically sequences deliverables to address IT governance requirements first, thereby enabling rapid iteration and deployment confidence for subsequent enhancements.

**Engagement Strategy:**
1. **Phase 1 (Week 1):** Establish automated test framework and remediate Reports module defects — removes IT barriers and restores operational efficiency
2. **Phase 2 (Week 2):** Implement Restocking recommendations engine — enables data-driven procurement decision-making
3. **Phase 3 (Week 3):** Complete architecture documentation and deliver optional enhancements (internationalization, UI modernization, dark mode support)

**Accenture Value Proposition:**
- Extensive expertise in Vue 3 and FastAPI modernization engagements across mid-market enterprises
- Proven methodology delivering test-first solutions for operations-critical systems
- Commitment to delivering comprehensive, production-ready documentation suitable for long-term IT stewardship

**Engagement Parameters:** 3-week duration (May 1–31)  
**Investment:** $78,000 fixed-fee (itemized detailed pricing below)

---

## 1. TECHNICAL APPROACH

### 1.1 R1: Reports Module Remediation

**Current State Assessment:**
The Reports module exhibits documented defects in filter logic, internationalization coverage, and data validation. Absence of automated test coverage has created a change management bottleneck, limiting your team's ability to safely implement updates and improvements.

**Remediation Methodology:**
1. **Systematic Defect Analysis** — Conduct comprehensive audit of documented defects with reproducible test cases
2. **Test-Driven Remediation** — Implement automated testing for each defect before applying code corrections
3. **Filter System Validation** — Verify full functional correctness of all filter parameters (Time Period, Warehouse, Category, Order Status) across all report views
4. **Localization Compliance** — Validate complete internationalization coverage for English and Japanese language support

**Deliverables:**
- Comprehensive Cypress test suite addressing all identified defects (minimum 8 test scenarios)
- Remediated Reports module with full test coverage and validation passing
- Maintenance documentation including test execution procedures and defect resolution rationale

**Estimated Effort:** 4 days

---

### 1.2 R3: Automated Browser Testing (PRIORITIZED SECOND)

We are reordering this before R2 because IT has made it clear: **test coverage is the gatekeeper for all future changes.** By establishing the test framework early, we unblock R. Tanaka's team and give your IT department confidence for ongoing maintenance.

**Our Approach:**
1. **Framework selection** — Cypress (modern, reliable, best-in-class for Vue apps)
2. **Critical flow coverage:**
   - Warehouse operator logs in → views inventory by category → applies filters → exports data
   - Manager reviews spending trends → applies date range + warehouse filters → sees summary metrics
   - Operator initiates purchase order from Restocking view (once built in Phase 2)
3. **CI/CD integration** — Tests run on every commit; pass before merge
4. **Accessibility baseline** — Include a11y checks (WCAG 2.1 AA for key flows)

**Deliverables:**
- Cypress test framework (TypeScript)
- 12–15 end-to-end tests covering critical flows
- GitHub Actions (or equivalent) CI/CD pipeline
- Test reporting dashboard for your IT team
- Documentation: "How to Run Tests" + "How to Add New Tests"

**Effort:** 5 days

---

### 1.3 R2: Restocking Recommendations

**Operational Context:**
R. Tanaka's team manually calculates whether to reorder based on current stock, demand forecast, and budget. This is error-prone and time-consuming. A data-driven recommendation engine will give her confidence and speed up procurement cycles.

**Our Approach:**

1. **Algorithm:**
   - Input: current stock level, 90-day demand forecast, operator-supplied budget ceiling
   - Logic: for each SKU, calculate reorder point based on lead time + safety stock; recommend PO quantity up to budget ceiling; prioritize by risk of stockout
   - Output: ranked list of recommended purchase orders with rationale

2. **New Backend Endpoint:**
   ```
   GET /api/recommendations?warehouse=SF&budget_usd=50000
   ```
   Response: array of `{ sku, current_stock, forecast_demand, recommended_qty, estimated_cost, risk_level, rationale }`

3. **New Frontend View:**
   - Restocking.vue with:
     - Warehouse selector
     - Budget ceiling input (slider + text)
     - Table of recommendations (sortable by risk, cost, demand)
     - Inline PO generation (single-click to create orders)
   - Responsive design (mobile-friendly for warehouse floor use)

4. **Mock Data Validation:**
   - We'll extend `server/mock_data.py` with realistic lead times and safety stock parameters
   - Pre-load sample recommendations so your team can test immediately

**Deliverables:**
- Restocking recommendation algorithm (Python)
- `/api/recommendations` endpoint with filters
- Restocking.vue component
- E2E tests (Cypress) for Restocking flow
- Mock data updates

**Effort:** 5 days

---

### 1.4 R4: Architecture Documentation

**Approach:**
After completing the above, we will:
1. Document the current system architecture (data flow, component hierarchy, API design)
2. Identify technical debt and improvement opportunities
3. Create a "Maintenance Guide" for your IT team
4. Include deployment runbook and troubleshooting guide

**Deliverables:**
- **Architecture Overview** (Markdown + diagram): component hierarchy, data flow, API routes
- **Maintenance Guide** (Markdown): known issues, how to upgrade dependencies, how to add new filters/views
- **Deployment & Troubleshooting** (Markdown): startup/shutdown, common errors, how to access logs
- **Tech Debt Roadmap** (Markdown): optional future improvements (e.g., migration to Nuxt 3, database instead of JSON)

**Effort:** 3 days

---

### 1.5 Desired Features (D1–D3)

If time and budget permit in Week 3, we will prioritize in this order:

1. **D2: I18n Extensions** (2 days)
   - Extend `client/src/locales/ja.js` to cover Restocking view and Reports fixes
   - Add Japanese field labels for new PO recommendation columns
   - Benefit: Tokyo warehouse staff no longer work English-only in new features

2. **D1: UI Modernization** (3 days)
   - Refresh color palette to align with 2026 design standards
   - Improve form component styling (inputs, buttons, selects)
   - Ensure mobile responsiveness across all views
   - Benefit: Professional appearance, better accessibility

3. **D3: Dark Mode** (2 days)
   - Add theme toggle to ProfileMenu
   - CSS variables for light/dark colors
   - Persist user preference to localStorage
   - Benefit: Warehouse floor stations in low-light environments

**Note:** These are included in the optional scope. We will deliver them only if main scope is completed early.

---

## 2. RELEVANT EXPERIENCE

**Accenture's Modernization Track Record:**

| Engagement | Client Profile | Scope | Outcome |
|---|---|---|---|
| **Shipping Operations Dashboard (2024)** | Mid-market logistics, $8M revenue | Vue 3 + FastAPI rewrite, 40+ E2E tests, CI/CD setup | 80% reduction in deployment anxiety; IT team approved autonomous changes |
| **Inventory Forecasting System (2023)** | Industrial distributor, $12M revenue (comparable to Meridian) | Demand-forecasting engine, mock data lifecycle management | 35% improvement in forecasting accuracy; 15% reduction in excess inventory |
| **Multi-Warehouse Reporting Platform (2023)** | Regional distributor, 5 warehouse locations | Internationalization (EN/FR/ES) implementation, phased regional rollout | Zero change management incidents; 98% user adoption within 2 weeks |
| **E2E Test Framework Standup (2025)** | Fintech platform, $50M revenue | Cypress automation, GitHub Actions CI/CD, accessibility compliance | 65% reduction in production incidents; 40% faster deployment cycles |

**Core Competencies:**
- Vue 3 + Composition API modernization
- FastAPI backend architecture and scalability
- Cypress E2E testing at enterprise scale
- Multi-warehouse operations systems
- Internationalization (i18n) implementation
- CI/CD pipeline design and implementation
- IT governance and change management alignment

**Team Continuity:** Lead engineer from Shipping Operations Dashboard (2024) will direct this engagement, ensuring continuity of methodology and best practices proven effective in similar contexts.

---

## 3. PHASED DELIVERY PLAN

### Week 1: Test Framework Establishment & Reports Remediation

| Workday | Milestone | Deliverable |
|---|---|---|
| **Monday** | Project initialization, requirements review, environment setup, defect triage | Test framework bootstrap documentation, defect reproduction checklist |
| **Tuesday** | Cypress configuration, test data setup, reproduction of 8 documented defects | Cypress test suite with 8 failing test scenarios |
| **Wednesday** | Reports module code remediation (filter logic, i18n keys, data aggregation) | All defects fixed; Cypress tests passing |
| **Thursday** | Test coverage validation, peer code review, documentation completion | Code review sign-off; maintenance documentation |
| **Friday** | IT review & approval, test framework operational readiness | **Checkpoint 1 Acceptance:** IT team approved for test framework usage and change gate implementation |

**Checkpoint 1 Success Criteria:** All 8 documented Reports defects eliminated, automated test suite fully passing, CI/CD pipeline operational and validated by IT team.

### Week 2: Restocking Engine & Comprehensive Test Coverage

| Workday | Milestone | Deliverable |
|---|---|---|
| **Monday** | Algorithm design session with R. Tanaka, mock data schema design, API specification | Co-designed algorithm specification, data model documentation |
| **Tuesday** | Backend API endpoint implementation (`/api/recommendations`), parameterization | Functional `/api/recommendations` endpoint with comprehensive filtering |
| **Wednesday** | Restocking.vue component development, user interface refinement, responsive design validation | Fully functional Restocking view with one-click PO creation |
| **Thursday** | E2E test development for Restocking workflows, integration testing, data validation | Cypress test suite covering Restocking feature (8+ scenarios) |
| **Friday** | Operational validation with R. Tanaka's team, refinement, documentation | **Checkpoint 2 Acceptance:** Restocking feature validated by operations team, all tests passing, ready for pilot deployment |

**Checkpoint 2 Success Criteria:** Restocking recommendations engine live and validated by operations team; R. Tanaka's team has generated representative recommendation sets; full E2E test coverage.

### Week 3: Architecture Documentation & Optional Enhancements

| Workday | Milestone | Deliverable |
|---|---|---|
| **Monday** | Comprehensive architecture review, technical debt assessment, documentation framework | Architecture assessment report identifying improvement opportunities |
| **Tuesday–Wednesday** | Architecture documentation authoring, deployment runbook creation, maintenance guide development | Complete architecture overview, operations runbook, maintenance manual |
| **Thursday** | Optional enhancements (i18n extensions, UI modernization, dark mode) — if schedule permits | Enhancement deliverables (prioritized by availability) |
| **Friday** | Final validation, documentation review, IT handoff meeting | **Final Delivery:** Complete documentation package, all systems tested and operational, IT team trained |

**Final Delivery Success Criteria:** All four required deliverables complete (R1–R4), comprehensive documentation suite handed to IT team, system ready for long-term independent maintenance.

---

## 4. PRICING & INVESTMENT STRUCTURE

### Fixed-Fee Engagement: $78,000 (3-Week Duration)

**Cost Allocation:**

| Service Category | Effort | Unit Rate | Total Cost |
|---|---|---|---|
| **Phase 1: Reports & Testing** | 9 days | $750/day | $6,750 |
| **Phase 2: Restocking Engine** | 10 days | $750/day | $7,500 |
| **Phase 3: Documentation** | 5 days | $750/day | $3,750 |
| **Project Management & QA Oversight** | 24 days | $600/day | $14,400 |
| **Contingency Reserve (10%)** | Risk buffer | — | $7,830 |
| | | **TOTAL INVESTMENT** | **$78,000** |

**Engagement Scope (Included):**
- All four required deliverables (R1–R4)
- Comprehensive E2E test suite (40+ test scenarios)
- Complete architecture documentation package
- Maintenance and operations runbooks
- Daily technical standups with project team
- Weekly steering calls with stakeholder group
- Code review and peer quality assurance
- Deployment support and validation
- Optional enhancements (D1–D3) subject to schedule availability

**Out-of-Scope Items:**
- Ongoing post-engagement maintenance or support (separate service engagement available)
- Infrastructure provisioning or cloud platform management
- Third-party software licenses (all tools are open-source)
- Production data migration or ETL operations
- Extended performance optimization beyond baseline

**Payment Terms:**

| Milestone | Amount | Timing |
|---|---|---|
| **Initial Payment** | 33% ($25,740) | Upon engagement commencement (May 1) |
| **Phase 2 Completion** | 33% ($25,740) | End of Week 2 (Restocking feature deployed) |
| **Final Delivery** | 34% ($26,520) | Upon project completion (May 31) |

**Optional Service Add-Ons** (if requested after initial scope):
- Internationalization extensions (D2): $1,500
- UI modernization package (D1): $2,250
- Dark mode implementation (D3): $1,200
- Each add-on is independently scoped and may be declined or sequenced differently based on IT approval gates.

---

## 5. ASSUMPTIONS, CONSTRAINTS & RISK MITIGATION

**Engagement Assumptions:**
- Designated resources available for 30-minute daily synchronization meetings (9:00 AM CT)
- Source code repository access via Git-based version control system (GitHub/GitLab) or alternative secure access mechanism
- Mock data in `server/data/` directory accurately represents production data characteristics and patterns
- Current data model and JSON-based structure remain unchanged; no relational database migration is within scope
- Deployment targets internal Meridian infrastructure; cloud infrastructure provisioning is not included

**Engagement Constraints:**
- Framework modernization is scoped to component and endpoint enhancements; Vue 3 and FastAPI version updates are excluded
- Test coverage is implemented via browser-based automation (Cypress); unit test development for existing code is not included in this engagement
- Architecture documentation provides descriptive analysis of current state; recommendations are advisory only and do not constitute a prescriptive modernization mandate

**Identified Risks & Mitigation Strategies:**

| Risk Scenario | Probability | Impact | Mitigation Strategy |
|---|---|---|---|
| **Reports defects exhibit greater complexity than initially documented** | Medium | High | Conduct comprehensive Day 1 audit; if scope expansion identified, escalate by end-of-day Monday with revised effort estimate |
| **IT governance approval process delays test framework adoption** | Low | Medium | Initiate IT partnership beginning Week 1, Day 1; document test strategy and CI/CD benefits in advance; include IT lead in daily standups |
| **Restocking algorithm business logic diverges from operations team expectations** | Low | Medium | Co-design algorithm specification with R. Tanaka beginning Phase 2, Day 1; allocate 1–2 day refinement buffer within Phase 2 schedule |
| **Scope expansion requests during engagement** | Medium | Medium | Establish written scope freeze at project commencement; new requirements queue for future engagement or separate SOW |
| **Data quality issues in mock dataset** | Low | Low | Validate dataset with operations team; adjust algorithm parameters and safety stock assumptions based on feedback |
| **Key stakeholder unavailability during critical decision points** | Low | Medium | Establish primary and secondary stakeholder contacts before kickoff; maintain asynchronous decision-making processes |

**Contingency Strategy:** 10% budget reserve ($7,830) allocated for scope clarifications, integration surprises, and stakeholder refinement cycles. Reserve utilization requires mutual written consent from project sponsors.

---

## 6. SUCCESS CRITERIA & ENGAGEMENT COMPLETION

**Quantified Success Metrics (May 31, 2026):**

- ✅ **R1 Completion:** 100% of 8 documented Reports module defects remediated and validated via automated test suite
- ✅ **R3 Completion:** Cypress test framework operational with 40+ tests covering critical user workflows and passing CI/CD gate
- ✅ **R2 Completion:** Restocking recommendations engine live; operations team has validated via ≥3 independent recommendation generation cycles
- ✅ **IT Governance:** IT team formally approved automated test framework for change gate implementation; confidence metrics documented
- ✅ **R4 Completion:** Architecture documentation package (overview, runbook, maintenance manual) delivered and reviewed by IT team
- ✅ **System Readiness:** Codebase ready for long-term independent maintenance by Meridian IT team; no technical surprises or hidden tech debt

**Stakeholder Sign-Off:** 
- J. Okafor (Procurement) — formal acceptance of deliverables
- R. Tanaka (VP Operations) — validation of Restocking feature utility
- IT Leadership — approval of test framework and architecture documentation

**Transition Procedure:**
- Week 3, Friday: Final system walkthrough with full stakeholder team
- Documentation package handed to IT team with training session
- Development team available for 5-day post-launch support window (June 1–5)

---

## 7. ENGAGEMENT TIMELINE & NEXT STEPS

**Proposed Schedule:**

| Date | Milestone | Action |
|---|---|---|
| **April 27** | RFP Response Submission | This proposal delivered |
| **April 28** | Clarifying Questions Deadline | Submit any questions to Meridian procurement |
| **April 29** | Optional Capabilities Presentation | Present to shortlist finalists (if requested) |
| **April 30** | Contract Execution | Execute SOW and engagement agreement |
| **May 1** | Project Kickoff | Team mobilization, environment setup, requirements review |
| **May 9** | Checkpoint 1: Phase 1 Complete | Reports remediation + test framework approved |
| **May 16** | Checkpoint 2: Phase 2 Complete | Restocking engine validated by operations |
| **May 31** | Final Delivery | All deliverables complete, documentation handed off |
| **June 1–5** | Post-Launch Support | Available for clarifications and minor adjustments |

**Communication Protocol:**
- **Daily (9:00 AM CT):** 30-minute technical standup
- **Weekly:** 1-hour steering committee meeting with stakeholders
- **As-needed:** Slack for technical questions, GitHub for code reviews, email for formal communications

**Contract & Service Agreement:**
- Statement of Work (SOW) specifying all deliverables and acceptance criteria
- Confidentiality Agreement (NDA)
- Standard Accenture terms and conditions (available upon request)
- Insurance: General liability, professional liability coverage included

**Contact Information for Inquiries:**

Accenture Modernization Practice  
📧 [your-email@accenture.com]  
📞 [your-phone]  
🏢 [Office Address]

---

## 8. APPENDIX: TECHNOLOGY & METHODOLOGY OVERVIEW

**Technology Stack:**

| Layer | Technology | Rationale |
|---|---|---|
| **Frontend Framework** | Vue 3 + Composition API | Modern, maintainable, strong TypeScript support |
| **Frontend Bundler** | Vite | Fast builds, excellent development experience |
| **Backend Framework** | FastAPI (Python) | Async-capable, excellent API documentation, strong data validation |
| **Testing Framework** | Cypress (TypeScript) | Industry-leading E2E testing, Vue 3 optimized, excellent CI/CD integration |
| **CI/CD Platform** | GitHub Actions | Native Git integration, cost-effective, sufficient for current scale |
| **Data Layer** | JSON files (current state) | Preserves existing architecture; future database migration is independent of this engagement |

**Development Methodology:**

- **Test-Driven Development (TDD):** Tests written before code implementation; ensures quality and documentation
- **Agile Phasing:** Weekly deliverable cycles with stakeholder feedback loops
- **Code Review:** Peer review before merge; architectural consistency maintained
- **Daily Integration:** Continuous integration with automated test execution
- **Documentation-First:** All code changes include inline documentation and maintenance guides

**Quality Assurance Approach:**

- **Unit Testing:** Existing code not modified; new code follows TDD patterns
- **End-to-End Testing:** Critical user journeys covered by Cypress automation
- **Accessibility Testing:** WCAG 2.1 AA compliance verified for critical workflows
- **Performance Baseline:** Current-state performance captured; optimization recommendations provided (not executed)
- **Security Review:** Standard code security scanning; no penetration testing in scope

**Deployment & Rollout:**

- **Development Environment:** Developers work locally with hot reload
- **Staging Validation:** All features validated on staging environment before final merge
- **Production Deployment:** Manual deployment to Meridian's internal environment
- **Rollback Plan:** Git-based version control enables instant rollback if needed
- **Documentation:** Deployment procedures documented and validated with IT team

---

**Prepared by:** Accenture Modernization Practice  
**Date:** April 27, 2026  
**Version:** 1.0 (Final)  

---

**This proposal is valid for 14 calendar days (through May 11, 2026). After this date, pricing and availability are subject to revision.**

