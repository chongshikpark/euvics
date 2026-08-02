# PDF render readiness — completed

## Scope

Removed mechanical PDF presentation defects from the Proposal and Conceptual
Design Report (CDR), verified every rendered page, and recorded the exact
reasons that both PDFs remain excluded from public website assembly.

This task did not supply missing technical content, grant figure permission,
or invent release metadata or approval.

## Decisions

- Use hidden link borders in both PDFs while retaining functional links.
- Keep Proposal `TBD` statements visible as release-readiness limitations.
- Keep the sparse CDR technical sections visible; their missing content is a
  release blocker, not a layout issue to conceal.
- Keep the CDR layout figure for internal review only while its authorship and
  distribution permission remain unresolved.
- Keep the publication allowlist empty until every required release field is
  recorded and explicitly approved.

## Completed work

- [x] Configured shared PDF hyperlink styling with `hidelinks`; rendered links
      retain their targets without visible red or green annotation borders.
- [x] Applied the existing document font at `small` size only to the Proposal
      bibliography. All nine references now fit on page 5, eliminating the
      bibliography-only sixth page without removing or rewriting a reference.
- [x] Expanded the Proposal and CDR publication-decision records to name the
      content and permission blockers and every required release field:
      version, release date, public license, attribution, known limitations,
      approver, approval date, and checksum.
- [x] Rebuilt both PDFs and visually inspected every rendered page.
- [x] Kept the publication allowlist empty: neither PDF is released or eligible
      for website assembly.

## Verification evidence

- `make check` passed on 2026-08-03: publication-contract validation reported
  zero approved files; all 12 publication-contract tests passed; all five
  archived checksums passed; Proposal and CDR builds passed; and the undefined
  citation/reference/missing-file scan passed.
- Poppler rendering at 140 DPI was visually inspected for all five Proposal
  pages and all four CDR pages. No hyperlink borders, clipping, overlap, or
  bibliography spill page remain.
- Proposal output: 5 pages, SHA-256
  `35174f6c4b90b972b0fd7aa1a9ed32b55c94481c44a96ccabd1a474e269c289a`.
- CDR output: 4 pages, SHA-256
  `5713a4edb96a370e960b08c18d8daa1e37c17c50c13afa1ea1705f242d7e815c`.
- `git diff --check` passed.

## Unresolved release decisions

- Proposal: extensive `TBD` material must be resolved or explicitly accepted,
  and all required release metadata and approval must be recorded.
- CDR: pages 3–4 remain essentially headings and need reviewed technical
  content; distribution permission for the page-2 layout figure must be
  resolved or an approved replacement supplied; all required release metadata
  and approval must then be recorded.
- Neither output is production-release ready. Both remain excluded under the
  deny-by-default publication contract.
