# Data

This folder contains all data files for the project, organized into subdirectories.

## Structure

### raw/
Original, immutable data dump. Never modify files in this folder.
- Source data files as received
- Keep original file names when possible
- Document the source and date of acquisition

### processed/
Cleaned and transformed data ready for analysis.
- Processed datasets
- Aggregated data
- Feature-engineered datasets

### external/
Data from third-party sources.
- External datasets
- Reference data
- Lookup tables

## Important Notes
- Add large data files to .gitignore
- Consider using data versioning tools like DVC for large datasets
- Document data sources and processing steps
