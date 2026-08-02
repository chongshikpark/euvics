# Physics overview publication approval checklist

Prepared: 2026-08-03  
Status: **Approved and allowlisted**

## Publication boundary

This checklist records the smallest sufficient EUVICS source set approved for
the website's project-physics overview. The Proposal
PDF, CDR PDF, CDR layout figure, complete document entry points, cost sections,
archives, reviews, and execution plans remain excluded.

The CDR introduction establishes the project purpose, evidence boundary, and
physical source chain. The CDR source overview provides the explicit physics,
conventions, equations, model limitations, interfaces, and pyEUVICS validation
boundary. The shared bibliography supplies the cited source records. The
Proposal sections are substantively redundant for the website overview and are
therefore not proposed for this narrow allowlist.

## Exact-file publication review

| Repository path and SHA-256 | Used by | Public purpose | Scientific review / approval | Image rights | Sensitive-information check | Proposed manifest action |
| --- | --- | --- | --- | --- | --- | --- |
| `cdr/sections/introduction.tex`<br>`b1e362f6e89c6d79f6840c75c15995960911d8f08043d5baf39530491f3f4c76` | CDR sections 1.1–1.3; future website project overview | Define EUVICS, separate aims from demonstrated performance, and describe the end-to-end source chain | **Approved as written:** Chong Shik Park, Ph.D., project owner and scientific reviewer, 2026-08-03 | No image reference or embedded asset | Passed targeted scan: no local path, credential, internal URL, private contact, cost, procurement, personnel, or correspondence content | Allowlisted as exact `latex-source`, version `physics-overview-v1`, status `public-draft` |
| `cdr/sections/source_overview.tex`<br>`988b309fadf0cb5b2a8114575c77acac101218014c44e757fd2548b77c7658ab` | CDR sections 2.1–2.4; future website physics, output-controls, interfaces, and validation sections | Authoritative exact kinematics, conventions, regimes, dependencies, model scope, and limitations | **Approved as written:** Chong Shik Park, Ph.D., project owner and scientific reviewer, 2026-08-03 | No image reference or embedded asset | Passed targeted scan; validation language preserves the CAIN disagreement, provisional 13.5 nm status, and synthetic-calibration limitation | Allowlisted as exact `latex-source`, version `physics-overview-v1`, status `public-draft` |
| `bibliography/references.bib`<br>`c859403aad7ff42b8f0ae963231ae16146329452e43fad7ba794760602be56d9` | Proposal and CDR bibliographies; future website source verification | Supply verified primary/authoritative and locked pyEUVICS citation records referenced by the selected sections | Bibliographic records and exact publication approved: Chong Shik Park, Ph.D., 2026-08-03 | No reproduced images or tables; records contain citations and public source URLs only | Passed targeted scan; no private contacts, credentials, local paths, or restricted data | Allowlisted as exact `bibliography`, version `physics-overview-v1`, status `public-draft` |

## Content and rights findings

- No selected file contains internal planning, correspondence, review registers,
  private contact information, procurement, cost, personnel, credentials,
  secrets, internal URLs, machine names, or absolute local paths.
- No selected file includes or references an image. The permission-unresolved
  CDR layout figure is included only by `cdr/main.tex`, which is not selected.
- No external prose, table, or figure is reproduced. The bibliography contains
  citation metadata and links; the narrative is an original synthesis.
- The 3 MeV kinetic-energy and 800 nm values remain nominal assumed inputs with
  approval pending. The 6.7 nm and 13.5 nm values remain study targets rather
  than facility-performance claims.
- The selected wording explicitly denies unsupported claims of demonstrated
  flux, bandwidth, brilliance, efficiency, stability, readiness, or validation.
- The CAIN discrepancy, provisional 13.5 nm status, model approximations, and
  synthetic detector-calibration limitation remain visible.

## Human approval record

The project owner approved the exact hashes above. Any source edit changes a
hash and requires the review to be repeated.

| Field | Required value |
| --- | --- |
| Scientific reviewer | Chong Shik Park, Ph.D. |
| Scientific review disposition | Approved as written for public-draft website use |
| Scientific review date | 2026-08-03 |
| Project-owner approver | Chong Shik Park, Ph.D. |
| Project-owner approval date | 2026-08-03 |
| Publication status | `public-draft` |
| Version | `physics-overview-v1` |
| Public license | MIT License |
| Attribution | Copyright (c) 2026 Chong Shik Park, Ph.D.; EUVICS project |
| Known limitations | Approved without omission in the manifest's file-specific records |

Proposed file-specific limitations:

- `cdr/sections/introduction.tex`: project aims and candidate cases are not
  demonstrated source performance; application requirements remain unapproved.
- `cdr/sections/source_overview.tex`: model-specific approximations apply;
  6.7 nm CAIN provenance is incomplete with a known disagreement; the 13.5 nm
  case is provisional; synthetic calibration is not measured calibration;
  subsystem values remain TBD.
- `bibliography/references.bib`: the inventory contains contextual sources for
  other subsystems in addition to records cited by the public overview; those
  records do not assign their reported performance to EUVICS.

## Manifest action

Exactly three entries are added to `publication/public-content-v1.json`, one for
each reviewed path. Every prior exclusion is preserved. The resolved website
overview approval-pending decision is removed; the Proposal and CDR PDF
decisions remain pending or blocked.

Do not allowlist:

- `build/proposal/main.pdf` or `build/cdr/main.pdf`;
- `cdr/main.tex`, which references the permission-unresolved layout figure;
- any file under `archive/`, `papers/`, `reviews/`, or `docs/exec-plans/`;
- Proposal/CDR cost sources or any historical/generated artifact.

## Website lock handoff — commit pending

The approved Task 1 wording is committed at
`0e34bbfb163e94d5c9dcaaa6d79ca8e1a81d6a68`, but that commit predates the
allowlist approval and must not be placed in `sources.lock.yml`.

After approval and commit, record:

- repository: `https://github.com/chongshikpark/euvics`;
- immutable reviewed commit: **TBD — full 40-character SHA containing both the
  approved source hashes and manifest entries**;
- manifest: `publication/public-content-v1.json`, contract version `1.0`;
- allowlisted paths: the three exact paths in this checklist;
- approver and approval date: from the approved manifest;
- staged consumer paths:
  `content/imported/euvics/cdr/sections/introduction.tex`,
  `content/imported/euvics/cdr/sections/source_overview.tex`, and
  `content/imported/euvics/bibliography/references.bib`;
- rendered destination: the website-owned `content/project/overview.md` created
  in the subsequent website task; LaTeX and BibTeX inputs are provenance sources,
  not independently rendered MkDocs pages;
- still blocked: both PDFs, the CDR layout figure, costs, internal reviews,
  archives, and all other unlisted source files.

The website lock update must be a separate exact-commit change through the
approved source-update workflow. It must not pull a mutable branch or a dirty
working tree.
