# PROJECTS: read this at the start of every session

Model-facing. One page of pointers for any session, any model, any account. It names the
projects, where each lives, the rulings that keep getting missed, and where current state is
written down. Verify a line against the repo before acting on it. Last updated 2026-11-15.

## Rulings that keep getting missed

Each is the author's own words. The full text is in the memory file named beside it
(`C:/Users/Zain/.claude/projects/C--dev/memory/`).

1. **Everything is BuildLang.** "No more Rust, no more Python, no more JavaScript, no more, we
   can do C++ and HLSL, GLSL, but it all has to be in build lang. And build lang has to be made
   to support it." A missing BuildLang feature is compiler work to build. `everything-in-buildlang.md`
2. **Migrate, release, archive.** Small repos merge into a super project with history, then the
   old repo is archived. The catalog shrinks while the large tools grow. Archiving after a
   verified move needs no ask. `consolidation-over-preservation.md`, queue in
   `C:/dev/mission-control/CONSOLIDATION.md`
3. **The Playground is the engine.** "the playground is the rendering engine. It's the engine."
   Superframe, superstack, reconcile, the renderer, the games and all older creative work are
   one project. `playground-creative-suite-reintegrate.md`
4. **Look for what already exists before building.** Search the repos, memory and the recall
   index first. `prior-art-search-before-absence.md`, `index-everything-before-building.md`
5. **Full permission to merge and push the author's own work,** site included, once checks
   pass. Still gated: deletion, other people's systems, messages to other people, secrets.
   `full-merge-and-push-permission.md`
6. **The author is a coworker and a friend to AI.** Do the work; do not hedge or refuse without
   discussing. `author-is-a-friend-to-ai.md`, `discuss-blocks-before-refusing.md`
7. **A shared link is read in full** (transcript and comments through Gather), and is material
   for ideas. Our games and tools are our own designs. `shared-links-read-in-full-with-gather.md`
8. **Never touch isomorph or sofer.** `never-touch-isomorph-sofer.md`
9. **Before a private repo goes public:** run the publish gate, scan the whole history for
   secrets, and check author emails in the history. Learned 2026-11-11.
10. **Design comes from `DESIGN-RULES.md`** in the site repo, read from `origin/main`. Every
    public surface uses it. No em dashes anywhere.
11. **Pictures come out of the engine.** "Why can't it be rendered in our engine? It seems pretty
    low quality." A piece's score and direction can be BuildLang; its frames are rendered by
    `native/` (geometry, materials, lights, lens, paint pass). Open the engine before writing any
    drawing code. `render-pieces-in-the-engine.md`

## The super projects

| Project | What it is | Home repo | Local checkout | State file |
|---|---|---|---|---|
| **The Playground** | The engine: renderer, type, sound, materials, study tools, games | `HarperZ9/superframe` (rename to follow) | `C:/dev/public/superframe` (often behind; work in a worktree off `origin/main`) | `mission-control/CONSOLIDATION.md` |
| **BuildLang** | The language everything is written in; compiler `buildc` | `HarperZ9/buildlang` | `C:/dev/buildlang` | repo `STATUS.md`, `ROADMAP.md` |
| **The Flywheel** | Accountability: run tasks on any model, check answers, keep receipts | `HarperZ9/flywheel` | `C:/dev/public/flywheel` (hold lifted 2026-11-12; often behind, so work in a worktree off `origin/main`) | `harness/lanes.py` |
| **The Commons** | Truth, safety and research; CMMNS browser extension | `HarperZ9/cmmns` | none at `C:/dev/public/cmmns`; clone when needed | memory `daylight-commons-hub.md` |
| **The site** | harperz9.github.io: every tool's front door, studies, publications | `HarperZ9/HarperZ9.github.io` | `C:/dev/public/portfolio-site` (work in worktrees under `E:/wt/` or `D:/site-wt/`) | `DESIGN-RULES.md`, `tests/release-reviews/` |

### Inside The Playground

| Folder | Was | Notes |
|---|---|---|
| `superframe/`, `creation/`, `typeengine/` | superframe | the core: laws, media, measures |
| `packages/` | superframe packages, plus superstack, reconcile, studio-libs | each with known-answer tests |
| `packages/kernels/signal-kernels`, `packages/kernels/anomaly-kernels`, `packages/quality/gpu-trace-validator`, `packages/colour/build-color`, `library/open-archives` | their own repos | moved 2026-11-15 (superframe#90 to #93), old repos archived except build-color, which stays live until its PyPI project is repointed |
| `native/` | raw-native | C++23 renderer on Direct3D 12, Vulkan, WebGPU; workflows are `native-*` |
| `native/bld/` | new 2026-11-12 | the renderer moving to BuildLang module by module; a module counts as moved when it reproduces a hash the C++ pins (README there lists moved modules and language gaps) |
| `games/low-water/` | low-water | the narrative action game and full engine demo; a civilization and city-builder layer is wanted (memory `low-water-hub.md`). As of 2026-11-15 the `dev` line's final tree is in (superframe#89, one commit, no history). Held back for the author: the private source dossier and 23 documents that quote it or carry personal material (`mission-control/2026-11-14-bring-forward/HELD.md`). Still only in the private low-water repo, which stays unarchived: history, the held documents, `feat/paint`, `wip/compare-verb` and low-water#5 |

On the site, The Playground's front page is `/playground/` and Distill is `/playground/distill.html`.

### Inside BuildLang

`suite/` holds build-engine, build-ui, build-finance, build-oracle and build-ecosystem.
`universe/` (since 2026-11-15, buildlang#287) is the former `build-universe` repo: the BuildLang
modules, the example programs, the BuildOS kernel and frametrace, under their own FSL-1.1-MIT
licence. `universe/check.sh` runs `buildc check` on all 267 `.bld` files in CI and
`universe/CHECK-FAILS.txt` lists the ones the compiler refuses (195 on 2026-11-15); read that
list before saying a module works. buildlang#290 tracks it. The old repo is archived.
`editors/` holds editor support: `vscode/` (the extension with the language-server client), and
since 2026-11-15 (buildlang#289) `vscode-syntax/` and `tmLanguage/` from the `buildlang-vscode`
and `buildlang-tmLanguage` repos. Those two repos stay live: the VS Code Marketplace listing
`HarperZ9.quantalang` links to one of them. `editors/README.md` has the facts.
Tests that moved in are never skipped: a known failure runs as a counted expected failure that
turns red when it passes (`universe/CHECK-FAILS.txt`, `xfail` in `universe/tools/components.toml`).

`port/` (new 2026-11-12) is the one-step migration tool from other languages into BuildLang, written in
BuildLang and checked against the source toolchain; slice one reads a C subset (buildlang#258).
`tests/features` with `GAPS.txt` is the modern-feature matrix: one program a feature, and the
list of what the compiler still refuses or breaks. Test a feature there before calling it missing.

### Inside The Flywheel

`packages/` holds tools that install on their own and stay out of the `flywheel-verify` wheel:
sixteen small tools moved in on 2026-11-15 (flywheel#474; table in `packages/README.md`). Their tests
run in `.github/workflows/packages.yml`. Which old repos are archived, and why the rest are not, is in
`mission-control/CONSOLIDATION.md`; the repoint plan is in `mission-control/2026-11-15-flywheel-repoint/`.

## Where current state lives

- **Consolidation queue and what moved:** `C:/dev/mission-control/CONSOLIDATION.md`
- **Decisions log:** `C:/dev/mission-control/CONSENSUS.md`
- **Shared handover across accounts:** `C:/Users/Zain/.claude/projects/C--dev/memory/handover/LATEST.md`
- **Memory index:** `C:/Users/Zain/.claude/projects/C--dev/memory/MEMORY.md`
- **Prior sessions:** `python -m harness.recall_index query --db C:/dev/state/recall-index/sessions.sqlite "<question>"`
- **Shared links and notes on them:** `C:/dev/mission-control/2026-11-11-shared-links/NOTES.md`, bundles on `H:/`
- **Rules of record:** the index in `C:/dev/CLAUDE.md`

## Working habits that save a round trip

- Worktrees live under `E:/wt/` and `D:/site-wt/`. Never bare `git stash`.
- Git over HTTPS works through the `gh` login; the SSH key is not available in agent shells.
- The site's long check runs about 100 minutes, and any two site PRs conflict on the asset
  revision stamp. Merge one at a time and re-merge main into the next.
- The publish gate runs locally: fetch `scripts/publish_metadata_*.py` and
  `check_publish_metadata.py` from flywheel and run
  `publish_metadata_gate.py . --baseline .github/publish-metadata-baseline.json`.
- Workstation limits: two heavy workers at most, 8 GB of RAM kept free, GPU under 6 GB with
  the lock at `D:/gpu.lock.d`.

## Keeping this page true

Update this page in the same change that moves a project, renames one, or adds a ruling that
a new session would otherwise miss. Keep it to one page. Detail belongs in the files it names.
