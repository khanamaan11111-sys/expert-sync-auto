# Stage 7 — Free GitHub Pages launch

The website uses static HTML, CSS, JavaScript and JSON. It requires no paid hosting or backend for its current enquiry features.

## Enable GitHub Pages
1. Open repository Settings → Pages.
2. Under Build and deployment, choose Deploy from a branch.
3. Choose main and / (root), then Save.
4. Wait for GitHub to report the live site address and verify it. The expected default URL is https://khanamaan11111-sys.github.io/expert-sync-auto/ but it is not confirmed live until Pages reports successful deployment.
5. Test Home, Explore Cars, Available Cars, Sell Your Car and WhatsApp links on desktop and mobile.

## Search readiness
The repository includes sitemap.xml and robots.txt. Submit the live sitemap in Google Search Console after launch. Search indexing is not guaranteed. Listing-prep.html and review-listing.html are public utilities, not secure admin pages; noindex/robots rules do not protect confidential data.

## Important
No real vehicles are published in listings.json yet. Do not claim actual inventory until seller-authorized, reviewed entries are committed. WhatsApp messages are sent only when visitors choose to send them. Do not commit customer details or credentials to this public repository.

## Stage 50 release checks

The planned development stages are committed, but deployment and public browser tests remain unverified.

1. Enable Pages in Settings using main and the root folder. Confirm the successful deployment and visit the published address in a private browser.
2. Check Home, Tools, Inventory, Sell, Help, Privacy, robots.txt and sitemap.xml for broken links.
3. Test the seven newest tools: emergency-fund.html, expense-tracker.html, sale-proceeds.html, annual-budget.html, warranty-planner.html, commute-cost.html and glossary.html. Try invalid inputs, printing and mobile layouts.
4. Verify tool search, keyboard navigation and enquiry links. WhatsApp messages are enquiries, not confirmed bookings.
5. Keep listings.json limited to seller-authorised, reviewed vehicles. It is currently empty. Never publish private customer data.
6. Record actual results in launch-readiness.html and resolve blockers before announcing a public launch.

Search indexing is not guaranteed. This checklist is manual and does not itself deploy the website.

## Stage 51: repository preflight

The repository now includes site_preflight.py and .github/workflows/site-preflight.yml. The workflow is configured for pushes to main, pull requests and manual dispatch. It checks local page references, title and viewport metadata, sitemap URLs, and the listings.json structure using Python's standard library.

Open GitHub Actions and inspect the Static site preflight run. If it fails, review its reported paths, correct the files and rerun. A passing check only confirms these static repository checks; it does not prove that GitHub Pages is deployed, that external services work or that the pages behave correctly in a browser. Complete the manual checks in launch-readiness.html as well.

## Stage 53: installable web-app foundation

The homepage references manifest.webmanifest and registers service-worker.js, with auto-icon.svg as a branded icon. After a successful HTTPS GitHub Pages deployment, check browser install eligibility on Android and desktop. Browser support for SVG-only app icons varies; a PNG icon set may still be needed for consistent installation prompts. Offline support is limited to a small page shell and does not provide offline inventory, live enquiries or full functionality. This is not an Android APK or Play Store release.

A red X on a GitHub commit means a check needs inspection: open Actions, select the failed run, and read the failing job's logs. The preflight checker was adjusted to permit intentionally unindexed utility pages; a passing run and public Pages deployment must still be verified separately.

## Stage 56: offline behaviour

The web app now has offline.html and a versioned service worker. Only a small app shell is cached. If an uncached navigation fails due to a network error, the visitor sees the offline explanation rather than a misleading homepage. Actual HTTP errors, including missing pages, are not converted into successful homepage responses. Inventory JSON, live vehicle availability and WhatsApp enquiries are not offline features. Test by first loading the published site online, then using browser offline mode and opening an uncached page. Refresh the site after deployment so the updated service worker can activate.
