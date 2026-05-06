# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| `main`  | ✅ Yes     |

Only the current `main` branch receives security fixes.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report security issues privately by emailing **coding.projects.1642@proton.me**.

Include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested mitigations (optional)

You will receive an acknowledgment within 72 hours. We aim to release a fix within 14 days of a confirmed report, depending on severity and complexity.

## Scope

SourceRegistry resolves named source dependencies to local paths and verifies expected source state. The primary security surface is:

- **Path traversal** via `local_clone_hint` or env-var-derived clone roots — resolved paths must stay within an expected root
- **Git command injection** via untrusted SHA / branch / repo strings passed to `git` subprocesses
- **Force-push consent bypass** — auto-sync must never push without an explicit `auto_sync: true` flag on the source entry
- **Upstream PR push consent bypass** — `push` (open PR against original) must never run without an explicit `auto_pr_push: true` flag
- **Symlink attack** on local clones (a malicious clone could symlink `.git` to an attacker-controlled location)
- **Credential exposure** — `git` operations should not embed credentials in logs or registry yamls

## Out of Scope

- Vulnerabilities in `git` itself or in upstream repos being tracked
- Vulnerabilities in package managers (`uv`, `pip`, `bun`) used by integrators
- Issues requiring physical access to the host machine
- Network-level MITM against `git+https` or `git+ssh` (those are the upstream provider's responsibility)
