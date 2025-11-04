# Python Data Analysis Project

This repository demonstrates a typical folder structure for a Python data analysis project.

## Project Structure

```
.
├── src/                # Python source code
├── data/               # Data files
│   ├── raw/           # Original, immutable data
│   ├── processed/     # Cleaned and transformed data
│   └── external/      # Data from third-party sources
├── notebooks/         # Jupyter notebooks for exploration and analysis
├── docs/              # Documentation and references
├── tests/             # Unit tests and integration tests
├── requirements.txt   # Python dependencies
└── README.md          # Project overview (this file)
```

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/zander-prinsloo/test-repo.git
cd test-repo
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Workflow

1. **Data Collection**: Place raw data in `data/raw/`
2. **Exploration**: Use Jupyter notebooks in `notebooks/` for initial exploration
3. **Processing**: Write reusable code in `src/` for data processing
4. **Analysis**: Perform analysis using scripts in `src/` or notebooks
5. **Testing**: Write tests in `tests/` to ensure code reliability
6. **Documentation**: Document findings and methodologies in `docs/`

## Version Control Best Practices

- Don't commit large data files (add them to `.gitignore`)
- Clear notebook outputs before committing
- Commit small, logical changes with descriptive messages
- Use branches for new features or experiments
- Write meaningful commit messages

## Contributing

When contributing to this project:
1. Create a new branch for your feature
2. Make your changes
3. Write tests for new functionality
4. Update documentation as needed
5. Submit a pull request

## License

See LICENSE file for details. 
