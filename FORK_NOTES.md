# shazeus RoseSkin Fork Notes

This fork keeps the upstream RoseSkin asset layout intact and adds fork-local maintenance notes plus an inventory checker for quick validation.

## Fork-Specific Changes

- README badges and installer links point at `shazeus` fork repositories.
- `tools/asset_inventory.py` summarizes asset and locale coverage without touching `.rse` packages.
- Binary skin packages are left unchanged in this fork customization pass.

## Maintenance Rules

- Do not rewrite or repackage `.rse` files unless the asset source and expected ID mapping are known.
- Run `python tools/asset_inventory.py` after large asset pulls.
- Keep locale JSON files valid before pushing.
