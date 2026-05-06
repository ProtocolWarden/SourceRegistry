---
name: Feature Request
about: Suggest an improvement or new capability
labels: enhancement
assignees: ''
---

## Summary

A one-sentence description of the feature.

## Problem It Solves

What is currently difficult or impossible that this would fix?

## Proposed Solution

How you imagine it working. Include API examples if relevant.

## Affected Layer

Which part of SourceRegistry does this touch?

- [ ] Source entry contract (registry yaml schema)
- [ ] install_kind enum / new verifier
- [ ] Local clone resolution
- [ ] Bump / rebase / sync lifecycle
- [ ] Auto-sync (silent reconcile)
- [ ] Patch records (yaml schema)
- [ ] Poll / upstream API client
- [ ] Reconcile suggestion engine
- [ ] Push (upstream PR creation)
- [ ] CLI surface

## Alternatives Considered

Other approaches and why you ruled them out.

## Scope Check

Confirm this change stays within SourceRegistry's scope:
- It belongs to source resolution / verification / reconciliation (not subprocess execution, not routing, not planning)
- Destructive actions (force-push, PR creation) remain consent-gated
- Failure paths surface explicitly (no silent fallback)

## Additional Context

Related issues, architecture docs, or prior discussion.
