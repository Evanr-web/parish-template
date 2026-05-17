# Parish Website Platform — Full Build Plan

## Vision
A complete system that lets any UGCC parish go from "we need a website" to "it's live" in one afternoon, with zero technical skill required. Centralized content distribution, remote management, and tiered complexity for parishes that want more control.

**Product name:** Byzantine Doors Parish Platform
**URL:** byzantinedoors.com/parish

---

## Phase 1: Bulletproof Template
*The foundation everything else builds on.*

### 1.1 Finalize the Template Design
- [ ] Lock in the 5-page structure (Home, Visit, About, Schedule, Community)
- [ ] Finalize all global CSS — no more design tweaks after this
- [ ] Responsive testing: mobile, tablet, desktop (375px → 1440px)
- [ ] Accessibility pass: contrast ratios, ARIA labels, keyboard nav, screen reader
- [ ] Performance: Lighthouse 90+ on all pages (already static, should be easy)
- [ ] Liturgical calendar dynamic theming (the killer differentiator)
  - Wire `--liturgical-accent` to Calendar API response
  - Test all 6 color states: Gold, Violet, Wine, Blue, Green, Red

### 1.2 Pre-Written Content Library
- [ ] "About Byzantine Catholicism" — universal, works for any UGCC parish
- [ ] "What to Expect at Your First Visit" — generic first-visit guide
- [ ] Sacrament descriptions (Baptism, Chrismation, Eucharist, Confession, Marriage, Anointing, Holy Orders)
- [ ] "About Our Rite" short explainer
- [ ] FAQ: "Is this Catholic?", "Do I have to be Ukrainian?", "What's the Divine Liturgy?"
- [ ] Footer disclaimer text (independent parish, consult your pastor)
- [ ] All content bilingual-ready (English primary, Ukrainian optional)

### 1.3 Image Library
- [ ] 5-6 hero banner options (public domain / permissioned):
  - Iconostasis interior (golden, candlelit)
  - Church dome/ceiling (painted, looking up)
  - Candles and incense (close-up, warm)
  - Church exterior (Ukrainian style with domes)
  - Icon detail (face of Christ or Theotokos)
  - Empty nave (pews, natural light)
- [ ] Default patron icon placeholder
- [ ] Default pastor photo placeholder
- [ ] All images optimized (WebP, multiple sizes, lazy loading)

### 1.4 Config Completeness
- [ ] Audit `parish.config.ts` — does it cover everything a parish needs?
- [ ] Add missing fields:
  - Multiple pastors/deacons
  - Ministry/group list with contacts
  - Announcement banner (toggle + text)
  - Social links (Facebook, YouTube, Instagram)
  - Giving platform config (Zeffy, Canada Helps, PayPal)
  - Livestream embed
  - Bulletin upload path
  - Parish history blurb (short, for About page)
- [ ] Add config validation with helpful error messages
- [ ] Document every field with inline comments

### 1.5 Deploy Pipeline
- [ ] GitHub Actions workflow: push → build → deploy to GitHub Pages
- [ ] Cloudflare Pages alternative workflow
- [ ] Custom domain guide (CNAME setup)
- [ ] SSL automatic (both platforms handle this)

**Deliverable:** A template repo that, when you fill in the config and push, produces a beautiful, complete parish website with zero code changes.

---

## Phase 2: Parish Builder Wizard
*The web-based form that generates a parish site.*

### 2.1 Wizard UI (byzantinedoors.com/parish/builder)
- [ ] Multi-step form with progress indicator
- [ ] **Step 1: Parish Identity**
  - Parish name (English + Ukrainian)
  - Eparchy (dropdown — pre-populated with all North American eparchies/exarchates)
  - Rite (pre-filled: Byzantine Ukrainian)
  - Address (with Google Places autocomplete → auto-generates map embed)
  - Phone, email, website
- [ ] **Step 2: People**
  - Pastor name, title (dropdown: Fr., Very Rev., Rt. Rev., etc.)
  - Pastor photo upload (optional)
  - Additional clergy (add more button)
- [ ] **Step 3: Service Times**
  - "Add a service" interactive builder
  - Day picker (Sun-Sat), time picker, language toggle (Eng/Ukr/Both)
  - Service type dropdown (Divine Liturgy, Vespers, Matins, Moleben, Akathist, Panakhyda, etc.)
  - Confession times (separate section)
  - "Add another" pattern
  - Drag to reorder
- [ ] **Step 4: Look & Feel**
  - Hero image selector (click to choose from 5-6 options, visual grid)
  - Accent palette selector (3-4 curated palettes, visual swatches)
  - Patron icon upload (optional — "Don't have one? That's fine, we'll use a beautiful default")
- [ ] **Step 5: Features & Links**
  - Toggle switches for optional sections
  - Input fields for: donation link, livestream URL, Facebook, YouTube, bulletin URL
  - Bilingual toggle
- [ ] **Step 6: Preview**
  - Live rendered preview of their site with their actual data
  - Desktop / Mobile toggle
  - "This is what your parishioners will see"
  - Edit buttons on each section that jump back to the relevant step

### 2.2 Export & Deploy
- [ ] **Option A: Download ZIP**
  - Generates complete project with their `parish.config.ts` filled in
  - Includes README with deploy instructions
  - For parishes with a tech volunteer
- [ ] **Option B: One-Click Deploy** (stretch goal)
  - "Deploy to GitHub Pages" button
  - GitHub OAuth flow → creates repo → pushes code → enables Pages
  - Parish gets a URL in 2 minutes: `parishname.github.io`
  - Auto-generates setup guide with their specific URLs
- [ ] **Option C: "We'll Set It Up For You"**
  - Contact form → goes to Evan / eparchy tech support
  - For parishes that can't do A or B
  - You manually deploy for them using the wizard output

### 2.3 Wizard Technical Stack
- [ ] Built as a section/app on byzantinedoors.com (Astro + client-side JS)
- [ ] Form state managed client-side (localStorage persistence — don't lose progress)
- [ ] Preview rendered client-side (same Astro components, hydrated)
- [ ] ZIP generation via JSZip in-browser (no server needed for Option A)
- [ ] GitHub deploy via GitHub API + OAuth app (Option B — needs small serverless function)

**Deliverable:** A web-based wizard at byzantinedoors.com/parish/builder that any parish admin can use to generate their website.

---

## Phase 3: Operations Guides
*Tier-matched documentation so parishes can actually maintain their site.*

### 3.1 Tier 1 Manual: "Set It and Forget It"
- [ ] Printed-friendly PDF format (they will print this)
- [ ] How to change service times (with screenshots of editing parish.config.ts in GitHub's web editor)
- [ ] How to update the pastor's name
- [ ] How to swap the hero image
- [ ] How to add a bulletin PDF
- [ ] How to update the announcement banner
- [ ] Troubleshooting: "My site looks broken" → clear cache, re-deploy
- [ ] Who to contact for help (eparchy support email/phone)

### 3.2 Tier 2 Manual: "We Post Updates"
- [ ] Everything in Tier 1
- [ ] How to post an announcement (create a markdown file in GitHub's web editor)
- [ ] How to add an event
- [ ] How to upload photos
- [ ] Understanding the content folder structure
- [ ] "Common tasks" quick-reference card (1-page cheat sheet)

### 3.3 Tier 3 Manual: "We Have a CMS"
- [ ] Everything in Tier 2
- [ ] Sanity Studio walkthrough with screenshots
- [ ] How to create/edit/publish content
- [ ] How to manage media
- [ ] How to add new pages
- [ ] User roles (Editor vs. Admin)
- [ ] Backup and restore

### 3.4 Video Guides (stretch goal)
- [ ] 3-5 minute screencasts for the most common tasks
- [ ] Hosted on YouTube, linked from the manual
- [ ] Bilingual (English + Ukrainian) versions

**Deliverable:** Three PDF manuals (one per tier) + optional video guides.

---

## Phase 4: Shared Content API
*Centralized content that flows to all parish sites.*

### 4.1 API Design
- [ ] Endpoint: `byzantinedoors.com/api/eparchy/{eparchy-slug}.json`
- [ ] Schema:
  ```json
  {
    "announcements": [
      { "title": "", "body": "", "date": "", "priority": "normal|urgent", "expires": "" }
    ],
    "events": [
      { "title": "", "date": "", "location": "", "url": "" }
    ],
    "resources": [
      { "title": "", "url": "", "type": "pastoral-letter|document|link" }
    ],
    "liturgicalNotes": [
      { "date": "", "note": "" }
    ],
    "templateVersion": "1.2.0",
    "updatedAt": ""
  }
  ```
- [ ] Admin interface to update (simple form on byzantinedoors.com, auth-protected)
- [ ] Or: Sanity CMS dataset for shared content (reuse existing infrastructure)

### 4.2 Parish Site Integration
- [ ] `<EparchyAnnouncements />` component — fetches and renders shared announcements
- [ ] `<EparchyEvents />` component — shared events feed
- [ ] Fetch at build time (static) + optional client-side refresh
- [ ] Graceful fallback if API is unreachable (show nothing, don't break)
- [ ] Config flag: `eparchy: "edmonton"` in `parish.config.ts`

### 4.3 Rebuild Trigger
- [ ] GitHub Actions `repository_dispatch` webhook
- [ ] Script: "Rebuild all parishes" — hits every parish repo's dispatch endpoint
- [ ] Triggered when shared content updates
- [ ] Dashboard shows last build time per parish

**Deliverable:** A shared content API + components that let you push announcements to every parish site at once.

---

## Phase 4b: Byzantine Doors Content Syndication
*Turn every parish site into a distribution node for byzantinedoors.com.*

### 4b.1 Syndication API
- [ ] Endpoint: `byzantinedoors.com/api/syndication/feed.json`
- [ ] Schema:
  ```json
  {
    "articles": [
      {
        "id": "",
        "title": "",
        "excerpt": "",
        "body": "",
        "category": "narthex|feasts|saints|liturgy|catechesis",
        "canonicalUrl": "https://byzantinedoors.com/narthex/jesus-prayer/",
        "image": "",
        "author": "",
        "authorParish": "",
        "publishedAt": "",
        "updatedAt": ""
      }
    ],
    "categories": [
      { "slug": "narthex", "name": "The Narthex", "description": "" }
    ]
  }
  ```
- [ ] Filterable by category, date range, limit
- [ ] Versioned (`/v1/`) for future-proofing

### 4b.2 Parish Site Integration
- [ ] Config toggle:
  ```ts
  byzantineDoors: {
    enabled: true,
    sections: ["narthex", "feasts", "saints"],
    display: "full" | "preview"
  }
  ```
- [ ] `<ByzantineDoorsArticle />` component — renders syndicated content
- [ ] `<ByzantineDoorsSection />` — auto-generated "Learn" section from syndicated feed
- [ ] "Learn" nav item appears only when syndication is enabled
- [ ] Canonical tag: `<link rel="canonical" href="{canonicalUrl}" />` on every syndicated article
- [ ] Attribution footer on every article: *"From [Byzantine Doors](https://byzantinedoors.com) — Resources for Byzantine Catholic life"*
- [ ] Short articles (<500 words): display in full with canonical tag
- [ ] Long articles: excerpt + "Continue reading on Byzantine Doors →"
- [ ] Graceful fallback if API unreachable

### 4b.3 SEO Architecture
- [ ] Canonical tags on all syndicated content → byzantinedoors.com gets SEO credit
- [ ] Backlinks from every parish site to byzantinedoors.com
- [ ] No duplicate content penalties (canonical handles this)
- [ ] Structured data (JSON-LD) with author + publisher attribution
- [ ] Sitemap excludes syndicated articles (they belong to Byzantine Doors' sitemap)

### 4b.4 Reverse Flow: Parish → Byzantine Doors
- [ ] "Share with Byzantine Doors" flag on Tier 2/3 parish content
- [ ] Submitted content goes to a review queue (you curate)
- [ ] Approved content published on byzantinedoors.com as canonical
- [ ] Syndicated back to ALL parish sites
- [ ] Original author credited: "By Fr. Michael Lutsak, Dormition Parish"
- [ ] Contributor guidelines for priests who want to write

### 4b.5 Wizard Integration
- [ ] Builder Step 5 toggle: "Include teaching articles from Byzantine Doors"
- [ ] Description: "Beautiful articles about Byzantine Catholic faith, prayer, and liturgy — automatically added to your site"
- [ ] Category picker: which sections to include

**Deliverable:** A content syndication system where you publish once on byzantinedoors.com and it appears on every opted-in parish site, with proper SEO attribution driving authority back to Byzantine Doors.

---

## Phase 5: Eparchy Dashboard
*Visibility and control for eparchy administration.*

### 5.1 Dashboard UI (byzantinedoors.com/eparchy)
- [ ] Auth-protected (eparchy admin login)
- [ ] Parish registry: all parishes, their URLs, last updated, template version
- [ ] Status indicators: site up/down, content freshness, template version current/outdated
- [ ] Quick actions: trigger rebuild, view site, access repo

### 5.2 Content Management
- [ ] Shared announcements editor (CRUD)
- [ ] Shared events editor
- [ ] Resource/document uploads
- [ ] "Push to all parishes" button

### 5.3 Support Tools
- [ ] "Parish needs help" queue (contact form submissions)
- [ ] Template version tracker — which parishes are outdated
- [ ] Bulk update trigger — push template updates to all

### 5.4 Analytics (stretch goal)
- [ ] Aggregate: total visits across all parish sites
- [ ] Per-parish: basic traffic (via privacy-respecting analytics like Plausible or Fathom)
- [ ] "Which parishes are actually being visited?"

**Deliverable:** A web dashboard for the eparchy to manage all parish sites from one place.

---

## Phase 6: CMS Addon (Tier 3)
*Optional Sanity CMS layer for parishes that want a visual editor.*

### 6.1 Sanity Schema
- [ ] Announcement schema
- [ ] Event schema  
- [ ] Bulletin schema (PDF upload + metadata)
- [ ] Ministry/group schema
- [ ] Custom page schema
- [ ] Pastor/clergy schema
- [ ] Service times schema (structured, not free text)
- [ ] Site settings schema (mirrors parish.config.ts)

### 6.2 Provisioning
- [ ] "Add CMS" flow in wizard or dashboard
- [ ] Auto-create Sanity project (Sanity Management API)
- [ ] Seed with parish data from config
- [ ] Deploy Sanity Studio (embedded or standalone)
- [ ] Wire Astro to fetch from Sanity instead of config/files

### 6.3 CMS Guide
- [ ] Standalone manual (Tier 3)
- [ ] Sanity Studio customized with parish branding
- [ ] Simplified toolbar — hide complexity, show only what they need

**Deliverable:** A one-click CMS addon that gives a parish a visual editor without touching code.

---

## Phase 7: Template Update System
*Keep all parish sites current without parish effort.*

### 7.1 Upstream Merge Strategy
- [ ] Parish repos are forks of the template repo
- [ ] GitHub Actions workflow on each fork: auto-merge upstream `src/` changes
- [ ] Protected files: `parish.config.ts`, `content/`, `public/images/` — never overwritten
- [ ] Conflict detection: alert Evan/eparchy if merge fails
- [ ] Version tracking: `template.version` in config

### 7.2 Update Flow
- [ ] You push update to template repo `main`
- [ ] All parish forks detect upstream change (scheduled check or webhook)
- [ ] Auto-merge + rebuild + deploy
- [ ] Dashboard shows which parishes updated successfully

### 7.3 Breaking Changes
- [ ] Semantic versioning for template
- [ ] Migration guides for major versions
- [ ] `parish.config.ts` schema validation with clear upgrade messages
- [ ] Rollback capability (git revert on the fork)

**Deliverable:** A system where you push one update and every parish site improves automatically.

---

## Build Order & Dependencies

```
Phase 1 ──→ Phase 2 ──→ Phase 3
  │              │
  │              └──→ Phase 4 ──→ Phase 5
  │
  └──→ Phase 6 (can start after Phase 1)
  
Phase 7 requires Phase 2 + Phase 4
```

**Critical path:** Phase 1 → Phase 2 → Phase 3 → Pilot with 2-3 parishes → Phase 4 → Phase 5

Phase 6 (CMS) and Phase 7 (updates) can be built in parallel once the core is solid.

---

## Milestones

| Milestone | Phases | What It Means |
|---|---|---|
| **M1: Template Complete** | 1 | One parish can deploy manually |
| **M2: Builder Live** | 1 + 2 | Any parish can generate a site via the wizard |
| **M3: Pilot Launch** | 1 + 2 + 3 | 2-3 parishes live, guides in hand |
| **M4: Eparchy Pitch** | 1-5 | Full platform demo for eparchy leadership |
| **M5: Eparchy Rollout** | All | 20+ parishes on the platform |

---

## Open Questions

1. **Domain strategy:** Do parishes get subdomains of the eparchy (`dormition.eeparchy.com`), their own domain, or `parishname.github.io`?
2. **Hosting responsibility:** Who pays if they want a custom domain? (GitHub Pages is free, custom domains need DNS only)
3. **Content ownership:** When a parish uses the template, who owns the site? (They do — it's their repo)
4. **Support SLA:** Who handles "my site is broken" calls? You? The eparchy? A volunteer team?
5. **Multi-eparchy:** Do we build for Edmonton first, then expand? Or design for multi-eparchy from day one?
6. **Bulletin generator integration:** Module 4 of Byzantine Doors — does it feed into the parish site?
7. **Prayer PWA integration:** Embed or link from parish sites?
8. **Analytics/privacy:** Any analytics at all? If so, privacy-first (no Google Analytics)
9. **Language:** Some parishes are primarily Ukrainian, some primarily English, some fully bilingual. How deep does the i18n go?
10. **Non-UGCC:** Could this work for other Byzantine Catholic churches (Ruthenian, Melkite, Romanian)? Just a config change?
