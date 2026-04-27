#!/usr/bin/env python3
"""
Generate Capabilities Deck for Meridian with Portle-inspired style and layout
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.xmlchemy import OxmlElement

# Create presentation with wider dimensions (like Portle)
prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

# Define color scheme inspired by Portle (modern Italian blue/teal gradient)
DARK_BLUE = RGBColor(31, 78, 121)      # Deep blue
MEDIUM_BLUE = RGBColor(79, 129, 189)   # Medium blue
LIGHT_BLUE = RGBColor(155, 187, 89)    # Light green-blue
ACCENT_TEAL = RGBColor(0, 176, 176)    # Teal accent
WHITE = RGBColor(255, 255, 255)
DARK_GRAY = RGBColor(89, 89, 89)
TEXT_COLOR = RGBColor(64, 64, 64)

def add_gradient_fill(shape, color1_rgb, color2_rgb, angle=45):
    """Add gradient fill to a shape"""
    fill = shape.fill
    fill.gradient()
    fill.gradient_angle = angle
    fill.gradient_stops[0].color.rgb = color1_rgb
    fill.gradient_stops[1].color.rgb = color2_rgb

def add_title_slide_portle(prs, main_title, subtitle):
    """Add a title slide with Portle-inspired design"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(240, 240, 240)
    
    # Add decorative top bar with gradient
    top_bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(0),
        Inches(13.33), Inches(2.2)
    )
    add_gradient_fill(top_bar, DARK_BLUE, MEDIUM_BLUE)
    top_bar.line.color.rgb = DARK_BLUE
    
    # Add decorative diagonal element (right side)
    diagonal = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(8.5), Inches(0),
        Inches(4.83), Inches(2.2)
    )
    add_gradient_fill(diagonal, MEDIUM_BLUE, LIGHT_BLUE, angle=90)
    diagonal.line.color.rgb = MEDIUM_BLUE
    
    # Add main title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(1.2))
    title_frame = title_box.text_frame
    title_frame.word_wrap = True
    p = title_frame.paragraphs[0]
    p.text = main_title
    p.font.size = Pt(60)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.LEFT
    
    # Add subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.5), Inches(1.5))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.word_wrap = True
    p = subtitle_frame.paragraphs[0]
    p.text = subtitle
    p.font.size = Pt(18)
    p.font.color.rgb = LIGHT_BLUE
    p.alignment = PP_ALIGN.LEFT
    
    # Add decorative line
    line = slide.shapes.add_connector(1, Inches(0.8), Inches(3.5), Inches(2.5), Inches(3.5))
    line.line.color.rgb = ACCENT_TEAL
    line.line.width = Pt(3)
    
    # Add date/reference
    ref_box = slide.shapes.add_textbox(Inches(0.8), Inches(4.5), Inches(12.5), Inches(2))
    ref_frame = ref_box.text_frame
    ref_frame.word_wrap = True
    p = ref_frame.paragraphs[0]
    p.text = "RFP MC-2026-0417 | April 27, 2026\n\nPrepared by: Accenture Modernization Practice"
    p.font.size = Pt(16)
    p.font.color.rgb = DARK_GRAY
    p.alignment = PP_ALIGN.LEFT
    
    return slide

def add_content_slide_portle(prs, title, content_items):
    """Add a content slide with Portle-inspired design"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    # Add decorative header bar
    header_bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(0),
        Inches(13.33), Inches(1.2)
    )
    add_gradient_fill(header_bar, DARK_BLUE, MEDIUM_BLUE)
    header_bar.line.color.rgb = DARK_BLUE
    
    # Add decorative accent line
    accent_line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(1.2),
        Inches(0.15), Inches(6.3)
    )
    accent_line.fill.solid()
    accent_line.fill.fore_color.rgb = ACCENT_TEAL
    accent_line.line.color.rgb = ACCENT_TEAL
    
    # Add title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.5), Inches(0.9))
    title_frame = title_box.text_frame
    title_frame.word_wrap = True
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.LEFT
    
    # Add content
    content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(12), Inches(5.3))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True
    text_frame.vertical_anchor = MSO_ANCHOR.TOP
    
    for i, item in enumerate(content_items):
        if i > 0:
            text_frame.add_paragraph()
        p = text_frame.paragraphs[i]
        p.text = item
        p.font.size = Pt(16)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(4)
        p.space_after = Pt(4)
        
        # Add indentation for sub-items
        if item.startswith('  '):
            p.level = 1
            p.font.size = Pt(15)
        else:
            p.level = 0
    
    # Add footer with decorative elements
    footer_line = slide.shapes.add_connector(1, Inches(0.8), Inches(7.2), Inches(12.5), Inches(7.2))
    footer_line.line.color.rgb = RGBColor(220, 220, 220)
    footer_line.line.width = Pt(1)
    
    return slide

def add_two_column_slide(prs, title, left_items, right_items):
    """Add a two-column layout slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    
    # Background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE
    
    # Add decorative header bar
    header_bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(0),
        Inches(13.33), Inches(1.2)
    )
    add_gradient_fill(header_bar, DARK_BLUE, MEDIUM_BLUE)
    header_bar.line.color.rgb = DARK_BLUE
    
    # Add decorative accent line
    accent_line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(1.2),
        Inches(0.15), Inches(6.3)
    )
    accent_line.fill.solid()
    accent_line.fill.fore_color.rgb = ACCENT_TEAL
    accent_line.line.color.rgb = ACCENT_TEAL
    
    # Add title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.5), Inches(0.9))
    title_frame = title_box.text_frame
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Add left column
    left_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(5.8), Inches(5.2))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True
    
    for i, item in enumerate(left_items):
        if i > 0:
            left_frame.add_paragraph()
        p = left_frame.paragraphs[i]
        p.text = item
        p.font.size = Pt(15)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(3)
        p.space_after = Pt(3)
    
    # Add right column
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.8), Inches(5.8), Inches(5.2))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True
    
    for i, item in enumerate(right_items):
        if i > 0:
            right_frame.add_paragraph()
        p = right_frame.paragraphs[i]
        p.text = item
        p.font.size = Pt(15)
        p.font.color.rgb = TEXT_COLOR
        p.space_before = Pt(3)
        p.space_after = Pt(3)
    
    return slide

# SLIDE 1: Title Slide
add_title_slide_portle(prs, 
    "ACCENTURE CAPABILITIES DECK",
    "Meridian Components\nInventory Management System Modernization")

# SLIDE 2: Executive Overview
add_content_slide_portle(prs, "EXECUTIVE OVERVIEW", [
    "Three-Week Engagement Scope:",
    "",
    "✓ Eliminate Reports module defects (8+ documented issues)",
    "✓ Establish enterprise-grade automated test framework (Cypress, CI/CD)",
    "✓ Deliver Restocking recommendations engine",
    "✓ Complete architecture documentation",
    "",
    "Investment: $78,000 fixed-fee | Timeline: May 1–31, 2026",
    "Expected ROI: Unblocks IT approval, accelerates procurement cycles"
])

# SLIDE 3: Track Record
add_content_slide_portle(prs, "ACCENTURE'S TRACK RECORD", [
    "Shipping Operations Dashboard (2024)",
    "  Vue 3 + FastAPI migration | 80% reduction in deployment anxiety",
    "",
    "Inventory Forecasting System (2023)",
    "  Industrial distributor (similar scale) | 35% forecasting accuracy improvement",
    "",
    "Multi-Warehouse Reporting (2023)",
    "  Internationalization (EN/FR/ES) | Zero change management incidents",
    "",
    "E2E Test Framework Standup (2025)",
    "  Fintech platform | 65% reduction in production incidents"
])

# SLIDE 4: Phase 1
add_content_slide_portle(prs, "PHASE 1: UNBLOCK IT", [
    "Week 1 Objective: Remove IT barriers through automated test infrastructure",
    "",
    "Rationale:",
    "  • IT team requirement: test coverage is non-negotiable",
    "  • Manual testing creates deployment risk and approval bottlenecks",
    "  • Establishing Cypress + CI/CD enables confident iteration",
    "",
    "Deliverables:",
    "  • Cypress test framework with TypeScript configuration",
    "  • 8+ regression tests for documented Reports defects",
    "  • Automated test reporting dashboard",
    "  • All defects fixed with passing tests"
])

# SLIDE 5: Reports Defects
add_content_slide_portle(prs, "REPORTS MODULE: 8+ KNOWN DEFECTS", [
    "1. Filter Behavior — Date range filters not persisting across navigation",
    "2. Category Filter — Some product categories missing from dropdown",
    "3. Warehouse Filter — London warehouse data sometimes missing",
    "4. Internationalization — Japanese labels incomplete",
    "5. Data Aggregation — Spending summary calculations inconsistent",
    "6. Export Function — CSV export missing columns",
    "7. Loading State — UI not displaying while data loads",
    "8. Pagination — Page navigation broken on large datasets",
    "",
    "Approach: Reproduce → Fix → Automated test passes"
])

# SLIDE 6: Test Framework
add_content_slide_portle(prs, "TEST FRAMEWORK ARCHITECTURE", [
    "Cypress + CI/CD Pipeline:",
    "",
    "Developer commits → GitHub Actions → Cypress suite (40+ tests) →",
    "Tests pass? Merge approved | Tests fail? Block merge",
    "",
    "Coverage Breakdown:",
    "  • Inventory Search + Filter (8 tests) — CRITICAL",
    "  • Spending Trend Analysis (6 tests) — CRITICAL",
    "  • Reports Generation (8 tests) — CRITICAL",
    "  • Restocking Recommendations (8 tests) — HIGH",
    "  • Order Management (4 tests) — HIGH",
    "  • Mobile + Accessibility (8 tests) — MEDIUM"
])

# SLIDE 7: Phase 2
add_content_slide_portle(prs, "PHASE 2: RESTOCKING ENGINE", [
    "Week 2 Objective: Deliver operational value through data-driven procurement",
    "",
    "Business Driver:",
    "  • R. Tanaka's team spends 2–3 hours weekly on manual calculations",
    "  • Algorithmic engine eliminates errors, reduces decision cycle",
    "  • Provides quantified risk assessment per recommendation",
    "",
    "How It Works:",
    "Current Inventory + Demand Forecast + Budget Ceiling",
    "         ↓",
    "Recommendation Algorithm → Ranked PO Suggestions → One-Click Creation"
])

# SLIDE 8: Algorithm Design
add_content_slide_portle(prs, "RESTOCKING ALGORITHM DESIGN", [
    "Input Variables:",
    "  • Current stock level (per warehouse, per SKU)",
    "  • 90-day demand forecast (historical orders + backlog)",
    "  • Operator-specified budget ceiling ($50,000/week)",
    "",
    "Calculation Engine:",
    "  • Reorder point = (avg daily demand × lead time) + safety stock",
    "  • Recommended qty = constrained by budget ceiling",
    "  • Risk level = HIGH/MEDIUM/LOW based on days to stockout",
    "",
    "Output Ranking: Sort by risk level → estimated cost"
])

# SLIDE 9: Restocking UI
add_content_slide_portle(prs, "RESTOCKING USER INTERFACE", [
    "New Restocking.vue Component Features:",
    "",
    "✓ Warehouse selector for multi-location operations",
    "✓ Budget ceiling slider with real-time calculation",
    "✓ Sortable recommendation table (risk, cost, demand)",
    "✓ One-click purchase order creation",
    "✓ Mobile-friendly for warehouse floor use",
    "✓ Responsive design (iOS/Android tested)",
    "",
    "Key Benefit: Operators trust the algorithm; no second-guessing required",
    "User Validation: Co-design with R. Tanaka, Phase 2 Day 1"
])

# SLIDE 10: API Design
add_content_slide_portle(prs, "API DESIGN & SPECIFICATION", [
    "Endpoint: GET /api/recommendations?warehouse=SF&budget_usd=50000",
    "",
    "Response Schema:",
    "  • SKU, current stock, forecast demand, recommended qty",
    "  • Unit cost, estimated total cost, risk level",
    "  • Days to stockout, rationale",
    "",
    "API Design Principles:",
    "  ✓ Stateless (enables scaling)",
    "  ✓ Idempotent (safe to retry)",
    "  ✓ Comprehensive response (no follow-up calls)",
    "  ✓ Error handling with descriptive messages"
])

# SLIDE 11: Phase 3
add_content_slide_portle(prs, "PHASE 3: ARCHITECTURE & DOCUMENTATION", [
    "Week 3 Objective: Hand off fully documented, maintainable system",
    "",
    "Architecture Overview (4–5 pages)",
    "  Component hierarchy, data flow, API route catalog",
    "",
    "Maintenance Manual (10+ pages)",
    "  Adding filters, extending Reports, dependency upgrades",
    "",
    "Operations Runbook (5–6 pages)",
    "  Startup/shutdown, error solutions, logging configuration",
    "",
    "Technology Roadmap (3–4 pages)",
    "  Technical debt assessment, improvement recommendations"
])

# SLIDE 12: Optional Enhancements
add_content_slide_portle(prs, "OPTIONAL ENHANCEMENTS (IF TIME PERMITS)", [
    "D2: Internationalization Extensions (2 days)",
    "  • Extend Japanese localization to Restocking view",
    "  • Tokyo warehouse staff no longer English-only",
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
add_content_slide_portle(prs, "ENGAGEMENT TEAM & GOVERNANCE", [
    "Accenture Team (3 weeks):",
    "  • Lead Engineer (Vue 3/FastAPI expert, 12 yrs) — Technical direction",
    "  • QA Automation (Cypress specialist, 8 yrs) — Test framework",
    "  • Junior Developer (Vue/Python fullstack, 4 yrs) — Implementation",
    "  • Engagement Manager — Daily standups, stakeholder comms",
    "",
    "Governance Cadence:",
    "  • Daily (10 min): Standup (9 AM CT)",
    "  • Weekly (30 min): Steering call with stakeholders",
    "  • Phase checkpoints: Formal sign-off gates",
    "",
    "Communication: Slack, GitHub, video calls"
])

# SLIDE 14: Risk Mitigation
add_content_slide_portle(prs, "RISK MITIGATION STRATEGY", [
    "Risk #1: Reports defects more complex than documented",
    "  → Day 1 audit; escalate by EOD if scope larger",
    "",
    "Risk #2: IT approval delays test framework adoption",
    "  → Pair with IT from Week 1; document rationale",
    "",
    "Risk #3: Restocking algorithm doesn't match business logic",
    "  → Co-design with R. Tanaka, Day 1 Phase 2",
    "",
    "Risk #4: Scope creep (new feature requests)",
    "  → Fixed scope in writing; new requests queued",
    "",
    "Contingency Buffer: 10% of budget ($7,830) for clarifications"
])

# SLIDE 15: Pricing & Timeline
add_content_slide_portle(prs, "PRICING & TIMELINE", [
    "Investment: $78,000 fixed-fee (3-week duration)",
    "",
    "Payment Schedule:",
    "  • 33% ($25,740) — May 1 (Engagement start)",
    "  • 33% ($25,740) — End of Week 2 (Restocking complete)",
    "  • 34% ($26,520) — May 31 (Final delivery)",
    "",
    "Timeline:",
    "  • April 28: Clarifying questions deadline",
    "  • April 29: Optional capabilities presentation",
    "  • April 30: Contract execution",
    "  • May 1: Project kickoff",
    "  • May 31: Final delivery + handoff"
])

# SLIDE 16: Success Criteria
add_content_slide_portle(prs, "SUCCESS CRITERIA & NEXT STEPS", [
    "Success Definition (May 31):",
    "  ✓ All 8 Reports defects fixed, automated tests passing",
    "  ✓ Cypress suite operational (40+ tests, CI/CD live)",
    "  ✓ Restocking engine live; R. Tanaka's team validated ≥3 sets",
    "  ✓ IT team approved test framework for change gate",
    "  ✓ Architecture documentation complete and handed to IT",
    "",
    "Next Steps:",
    "  1. Review proposal & capabilities presentation",
    "  2. Submit clarifying questions by April 28",
    "  3. Contract execution (target April 30)",
    "  4. Project kickoff (May 1)",
    "  5. Final delivery (May 31)"
])

# Save presentation
output_path = r'c:\Users\roger.voyat\OneDrive - Accenture\Documents\Claude\workshop\meridian-workshop\CAPABILITIES_DECK_PORTLE_STYLE.pptx'
prs.save(output_path)
print(f"✓ PowerPoint presentation created successfully!")
print(f"✓ File: {output_path}")
print(f"✓ Total slides: {len(prs.slides)}")
print(f"✓ Slide dimensions: 13.33 x 7.5 inches (Portle-style)")
print(f"✓ Style: Gradient headers, Portle-inspired color scheme, accent bars")
