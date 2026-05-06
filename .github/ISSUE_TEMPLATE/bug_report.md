---
name: Bug Report
about: Something is broken or behaving unexpectedly
labels: bug
assignees: ''
---

## Description

A clear description of what is broken.

## Steps to Reproduce

1. 
2. 
3. 

## Expected Behavior

What should have happened.

## Actual Behavior

What actually happened. Include the stage where it failed:

- [ ] Source registry parsing / validation
- [ ] Local clone resolution
- [ ] Verification (`git rev-parse` / `direct_url.json` / etc.)
- [ ] Bump (registry pin update)
- [ ] Rebase (`git rebase` against upstream)
- [ ] Sync (rebase + bump + reinstall)
- [ ] Auto-sync (silent reconcile)
- [ ] Patch record loading
- [ ] Poll (upstream API check)
- [ ] Reconcile suggestion (DROP_PATCH / REBASE_PATCH / PUSH_PATCH)
- [ ] Push (open upstream PR)
- [ ] Drop (remove patch yaml)

## install_kind Affected

- [ ] external
- [ ] cli_tool
- [ ] library
- [ ] binary
- [ ] other (specify):

## Environment

- OS: 
- Python version: 
- SourceRegistry version / commit: 
- git version: 

## Relevant Output

```
paste any error messages, git stderr, or registry yaml here
```

## Source Entry (if applicable)

```yaml
# paste the relevant source entry from the registry
```

## Additional Context

Anything else that might be relevant.
