#!/usr/bin/env python3
"""
Generate PowerPoint presentation from Capabilities Deck Markdown
Meridian Components Engagement - RFP MC-2026-0417
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define color scheme (Accenture brand-inspired)
ACCENT_BLUE = RGBColor(0, 51, 102)  # Dark blue
LIGHT_BLUE = RGBColor(0, 102, 204)  # Light blue
WHITE = RGBColor(255, 255, 255)
DARK_GRAY = RGBColor(64, 64, 64)
LIGHT_GRAY = RGBColor(242, 242, 242)

def add_title_slide(prs, title, subtitle):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = ACCENT_BLUE
    
    # Add title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.word_wrap = True
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Add subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(2))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.word_wrap = True
    p = subtitle_frame.paragraphs[0]
    p.text = subtitle
    p.font.size = Pt(24)
    p.font.color.rgb = LIGHT_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_content_slide(prs, title, content_items):
    """Add a content slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    # Add header bar
    header_shape = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = ACCENT_BLUE
    header_shape.line.color.rgb = ACCENT_BLUE
    
    # Add title
    title_frame = header_shape.text_frame
    title_frame.word_wrap = False
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_before = Pt(6)
    p.space_after = Pt(6)
    
    # Add content
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.2), Inches(8.6), Inches(5.8))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True
    
    for i, item in enumerate(content_items):
        if i > 0:
            text_frame.add_paragraph()
        p = text_frame.paragraphs[i]
        p.text = item
        p.font.size = Pt(18)
        p.font.color.rgb = DARK_GRAY
        p.space_before = Pt(6)
        p.space_after = Pt(6)
        p.level = 0
    
    return slide

# SLIDE 1: Title
add_title_slide(prs, "ACCENTURE CAPABILITIES DECK", 
                "Meridian Components Inventory Management System Modernization\nRFP MC-2026-0417 | April 27, 2026")

# SLIDE 2: Executive Overview
add_content_slide(prs, "EXECUTIVE OVERVIEW", [
    "✓ Three-Week Engagement Scope:",
    "  • Eliminate Reports module defects (8+ documented issues)",
    "  • Establish enterprise-grade automated test framework (Cypress, CI/CD)",
    "  • Deliver Restocking recommendations engine for data-driven procurement",
    "  • Complete architecture documentation for IT stewardship",
    "",
    "Investment: $78,000 fixed-fee",
    "Timeline: May 1–31, 2026",
    "Expected ROI: Immediate — unblocks IT approval, accelerates procurement cycles"
])

# SLIDE 3: Accenture Track Record
add_content_slide(prs, "ACCENTURE'S TRACK RECORD", [
    "✓ Shipping Operations Dashboard (2024)",
    "  Vue 3 + FastAPI migration | 80% reduction in deployment anxiety",
    "",
    "✓ Inventory Forecasting System (2023)",
    "  Industrial distributor (similar scale) | 35% forecasting accuracy improvement",
    "",
    "✓ Multi-Warehouse Reporting (2023)",
    "  Internationalization (EN/FR/ES) | Zero change management incidents",
    "",
    "✓ E2E Test Framework Standup (2025)",
    "  Fintech platform | 65% reduction in production incidents"
])

# SLIDE 4: Phase 1 Strategy
add_content_slide(prs, "PHASE 1: UNBLOCK IT", [
    "Week 1 Objective: Remove IT barriers through automated test infrastructure",
    "",
    "Rationale:",
    "  • IT team has made clear: test coverage is non-negotiable",
    "  • Manual testing creates deployment risk and change approval bottlenecks",
    "  • Establishing Cypress + CI/CD in Week 1 enables confident iteration",
    "",
    "Deliverables:",
    "  • Cypress test framework (TypeScript configuration, GitHub Actions)",
    "  • 8+ regression tests for documented Reports defects",
    "  • Automated test reporting dashboard for IT monitoring",
    "  • All Reports defects fixed and passing"
])

# SLIDE 5: Reports Module Defects
add_content_slide(prs, "REPORTS MODULE: 8+ KNOWN DEFECTS", [
    "1. Filter Behavior — Date range filters not persisting",
    "2. Category Filter — Some product categories missing from dropdown",
    "3. Warehouse Filter — London warehouse data sometimes missing",
    "4. Internationalization — Japanese labels incomplete",
    "5. Data Aggregation — Spending summary calculations inconsistent",
    "6. Export Function — CSV export missing columns",
    "7. Loading State — UI not displaying while data loads",
    "8. Pagination — Page navigation broken on large datasets",
    "",
    "Approach: Reproduce each defect → Fix root cause → Automated test passes"
])

# SLIDE 6: Test Framework Architecture
add_content_slide(prs, "TEST FRAMEWORK ARCHITECTURE", [
    "Cypress + CI/CD Strategy:",
    "",
    "Developer commits → GitHub Actions triggers Cypress suite →",
    "40+ tests execute → Tests pass? Merge approved | Tests fail? Block merge",
    "",
    "Test Coverage (40+ scenarios):",
    "  • Inventory Search + Filter (8 tests) — CRITICAL",
    "  • Spending Trend Analysis (6 tests) — CRITICAL",
    "  • Reports Generation (8 tests) — CRITICAL",
    "  • Restocking Recommendations (8 tests) — HIGH",
    "  • Order Management (4 tests) — HIGH",
    "  • Mobile Responsiveness + Accessibility (8 tests) — MEDIUM"
])

# SLIDE 7: Phase 2 Strategy
add_content_slide(prs, "PHASE 2: RESTOCKING ENGINE", [
    "Week 2 Objective: Deliver operational value through data-driven procurement",
    "",
    "Business Driver:",
    "  • R. Tanaka's team spends 2–3 hours weekly on manual reorder calculations",
    "  • Algorithmic engine eliminates errors, reduces decision cycle from hours to minutes",
    "  • Provides quantified risk assessment for each recommendation",
    "",
    "How It Works:",
    "Current Inventory + Demand Forecast + Budget Ceiling",
    "         ↓",
    "Recommendation Algorithm → Ranked PO Suggestions with Risk Scores",
    "         ↓",
    "One-Click Purchase Order Creation"
])

# SLIDE 8: Restocking Algorithm Design
add_content_slide(prs, "RESTOCKING ALGORITHM DESIGN", [
    "Inputs:",
    "  • Current stock level (per warehouse, per SKU)",
    "  • 90-day demand forecast (based on historical orders + backlog)",
    "  • Operator-specified budget ceiling (e.g., $50,000/week)",
    "  • Lead time assumptions & safety stock parameters",
    "",
    "Calculation:",
    "  • Reorder point = (avg daily demand × lead time) + safety stock",
    "  • Recommended qty = max(reorder qty, budget remaining / unit cost)",
    "  • Risk level = HIGH/MEDIUM/LOW based on days to stockout",
    "",
    "Output Ranking: Sort by risk level DESC, then by estimated cost DESC"
])

# SLIDE 9: Restocking UI Experience
add_content_slide(prs, "RESTOCKING UI: USER EXPERIENCE", [
    "New Restocking.vue Component Features:",
    "",
    "  • Warehouse selector (multi-location operations)",
    "  • Budget ceiling slider (real-time calculation)",
    "  • Sortable recommendation table (by risk, by cost, by demand)",
    "  • One-click purchase order creation",
    "  • Mobile-friendly for warehouse floor use",
    "  • Responsive design (iOS/Android tested)",
    "",
    "Key Benefit: Users can trust the algorithm; no second-guessing required",
    "",
    "User Validation: Co-design with R. Tanaka during Phase 2, Day 1"
])

# SLIDE 10: API Design
add_content_slide(prs, "API DESIGN: /api/recommendations ENDPOINT", [
    "Endpoint Specification:",
    "  GET /api/recommendations?warehouse=SF&budget_usd=50000",
    "",
    "Response includes:",
    "  • SKU, current stock, forecast demand, recommended qty",
    "  • Unit cost, estimated total cost, risk level, rationale",
    "  • Days to stockout, risk justification",
    "",
    "API Design Principles:",
    "  • Stateless (enables scaling)",
    "  • Idempotent (safe to retry)",
    "  • Comprehensive response (no follow-up calls needed)",
    "  • Error handling with descriptive messages"
])

# SLIDE 11: Phase 3 Strategy
add_content_slide(prs, "PHASE 3: ARCHITECTURE & DOCUMENTATION", [
    "Week 3 Objective: Hand off fully documented, maintainable system",
    "",
    "Deliverables:",
    "",
    "✓ Architecture Overview (4–5 pages)",
    "  Component hierarchy, data flow, API route catalog",
    "",
    "✓ Maintenance Manual (10+ pages)",
    "  Adding filters, extending Reports, dependency upgrades",
    "",
    "✓ Operations Runbook (5–6 pages)",
    "  Startup/shutdown, error solutions, logging configuration",
    "",
    "✓ Technology Roadmap (3–4 pages)",
    "  Technical debt assessment, improvement recommendations"
])

# SLIDE 12: Optional Enhancements
add_content_slide(prs, "OPTIONAL ENHANCEMENTS (IF TIME PERMITS)", [
    "D2: Internationalization Extensions (2 days)",
    "  • Extend Japanese localization to Restocking view",
    "  • Tokyo warehouse staff no longer work English-only",
    "",
    "D1: UI Modernization (3 days)",
    "  • Refresh color palette (2026 design standards)",
    "  • Improve form styling & WCAG 2.1 AA compliance",
    "",
    "D3: Dark Mode Support (2 days)",
    "  • Theme toggle in ProfileMenu",
    "  • Warehouse floor stations in low-light environments",
    "",
    "All enhancements tested and documented at core delivery level"
])

# SLIDE 13: Team & Governance
add_content_slide(prs, "ENGAGEMENT TEAM & GOVERNANCE", [
    "Accenture Team (3 weeks):",
    "  • Lead Engineer (Vue 3/FastAPI expert, 12 yrs) — Technical direction",
    "  • QA Automation (Cypress specialist, 8 yrs) — Test framework",
    "  • Junior Developer (Vue/Python fullstack, 4 yrs) — Implementation",
    "  • Engagement Manager — Daily standups, stakeholder comms",
    "",
    "Governance Cadence:",
    "  • Daily (10 min): Standup with your team (9 AM CT)",
    "  • Weekly (30 min): Steering call with J. Okafor + R. Tanaka + IT lead",
    "  • Phase checkpoints: Formal sign-off gates (end of Weeks 1, 2, 3)",
    "",
    "Communication: Slack, GitHub, video calls"
])

# SLIDE 14: Risk Mitigation
add_content_slide(prs, "RISK MITIGATION STRATEGY", [
    "Risk #1: Reports defects more complex than documented",
    "  → Day 1 audit; escalate by EOD if scope larger",
    "",
    "Risk #2: IT approval delays test framework adoption",
    "  → Pair with IT from Week 1; document rationale upfront",
    "",
    "Risk #3: Restocking algorithm doesn't match business logic",
    "  → Co-design with R. Tanaka, Day 1 Phase 2; 1–2 day refinement buffer",
    "",
    "Risk #4: Scope creep (new feature requests mid-engagement)",
    "  → Fixed scope in writing; new requests queued for future engagement",
    "",
    "Contingency Buffer: 10% of budget ($7,830) for clarifications"
])

# SLIDE 15: Pricing & Timeline
add_content_slide(prs, "PRICING & TIMELINE", [
    "Investment: $78,000 fixed-fee (3-week duration)",
    "",
    "Payment Schedule:",
    "  • 33% ($25,740) upfront (May 1)",
    "  • 33% ($25,740) end of Week 2 (Restocking complete)",
    "  • 34% ($26,520) final delivery (May 31)",
    "",
    "Engagement Timeline:",
    "  • April 28: Clarifying questions deadline",
    "  • April 29: Optional capabilities presentation",
    "  • April 30: Contract execution",
    "  • May 1: Project kickoff",
    "  • May 31: Final delivery + handoff"
])

# SLIDE 16: Success Criteria & Next Steps
add_content_slide(prs, "SUCCESS CRITERIA & NEXT STEPS", [
    "Success Definition (May 31):",
    "  ✓ All 8 Reports defects fixed, automated tests passing",
    "  ✓ Cypress test suite operational (40+ tests, CI/CD live)",
    "  ✓ Restocking engine live; R. Tanaka's team validated ≥3 sets",
    "  ✓ IT team approved test framework for change gate",
    "  ✓ Architecture documentation complete and handed to IT",
    "",
    "Next Steps:",
    "  1. Review this proposal & capabilities presentation",
    "  2. Submit clarifying questions by April 28",
    "  3. Contract execution (target April 30)",
    "  4. Project kickoff (May 1)",
    "  5. Final delivery (May 31)"
])

# Save presentation
output_path = r'c:\Users\roger.voyat\OneDrive - Accenture\Documents\Claude\workshop\meridian-workshop\CAPABILITIES_DECK.pptx'
prs.save(output_path)
print(f"✓ PowerPoint presentation created successfully: {output_path}")
print(f"✓ Total slides: {len(prs.slides)}")
