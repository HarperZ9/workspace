# Current release verification

Workspace rule adopted by Zain Dana Harper on 5 October 2026. The operator directed: “Only ever check against current release. Do not take anything on claim.” Articulate 0.9.0 was the concrete correction that prompted this rule; that version itself must be refreshed against authoritative release evidence on later work.

## Rule

Before attaching, validating, accepting or describing a tool's current shipped state, resolve its current release from the publisher's authoritative release or package registry. Verify the selected artifact's identity against that release. A claimed version, cached plugin, source checkout, README, old receipt or passing doctor alone cannot satisfy this requirement.

Never attach an old release as a fallback. If the current release cannot be obtained or verified, retain the limitation and stop the dependent attachment or acceptance. Do not silently substitute stale source, an older native bundle or a different distribution channel.

## Required evidence

1. Record the publisher, distribution, current release/version, source URL and retrieval time. Resolve release tags to exact commits where available.
2. Verify downloaded artifact digests against the publisher's release metadata or checksum manifest. Verify installed package/bundle metadata and entrypoint identity. A copied version label is insufficient.
3. Check the running server's initialization identity, tool surface and relevant behavior against the verified current artifact. Separate configured, installed, initialized, attached to the application and functionally checked states.
4. Retain scope, state ownership, grants and account/billing routes. A current version does not justify changed authority or silent fallback.
5. Investigate disagreement between release channels, manifests, docs and runtime. Use verified current artifact evidence to correct stale claims; keep unresolved provenance or channel mismatches explicit.

Historical artifacts may explain chronology or a regression. They cannot satisfy current-release acceptance or justify a current shipped-state claim. False-success controls must exercise the current implementation. Neither a matching digest nor successful initialization establishes semantic truth, enterprise readiness or useful outcomes.

This rule applies across the workspace, including MCP servers, plugins, utilities, benchmark and release checks, public tooling descriptions and resume/CV claims. Current Articulate checks and the required judgment review precede shipping. Preserve old artifacts as historical evidence without keeping their launch paths active as current attachments.
