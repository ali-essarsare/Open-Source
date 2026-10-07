## [Unreleased]

### Changed

- Reorganized implementations into internal `_` modules with public exports via
  package `__init__.py` files.
- Added NumPy-style docstrings and `TypeError` validation for non-string inputs.
- Added package-local tests and coverage configuration, and configured Black and Ruff.
- Updated `pyproject.toml` with development dependencies and package discovery settings.

### Added – snake_case() in textutils.transform
### Added – word_frequency() in textutils.frequency
### Added – slugify() in textutils.slug