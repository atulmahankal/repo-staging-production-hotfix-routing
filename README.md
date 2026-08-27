# repo-staging-production-hotfix-routing

Test repository for the development -> staging -> production promotion workflow.

## Branches

| Branch | Deployed to |
|---|---|
| `main` | production server |
| `staging` | testing / staging server |

## Documentation

- **[WORKFLOW.md](WORKFLOW.md)** — full worked walkthrough of the staging → production
  promotion flow, the emergency hotfix bypass, the divergence it creates, and how to
  reconcile back to `0 | 0`. Includes every command, diagrams, and screenshots.
