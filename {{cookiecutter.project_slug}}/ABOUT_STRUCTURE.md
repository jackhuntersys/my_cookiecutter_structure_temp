cookiecutter-mytemplate/
├── cookiecutter.json
└── {{cookiecutter.project_slug}}/              # 👈 Project root
    ├── pyproject.yml                           # 📦 Modern build config (Setuptools/Poetry)
    ├── setup.cfg                               # ⚙️ Config for tools (flake8, black, etc.)
    ├── requirements.txt                        # 📜 Environment dependencies
    ├── README.md                               # 📘 Project introduction
    ├── Makefile                                # 🛠️ Command shortcuts (e.g. make train)
    ├── .gitignore                              # 🙈 Ignore files/folders
    │
    ├── src/                                    # 🧠 Main source code
    │   └── {{cookiecutter.module_name}}/
    │       ├── __init__.py                     # Makes it a Python package
    │       ├── config.py                       # Project configs and constants
    │       ├── dataset.py                      # Data loading/generation scripts
    │       ├── features.py                     # Feature engineering scripts
    │       ├── exceptions.py                   # Custom exception classes
    │       ├── logger.py                       # Centralized logger setup
    │       ├── plots.py                        # Plotting/visualization functions
    │       └── modeling/                       # Model training/inference
    │           ├── __init__.py
    │           ├── train.py
    │           └── predict.py
    │
    ├── data/                                   # 📂 Data folder
    │   ├── raw/                                # Unmodified source data
    │   ├── processed/                          # Final cleaned data for ML
    │   └── external/                           # 3rd-party data
    │
    ├── notebooks/                              # 📒 Jupyter notebooks
    │   └── 1.0-init-exploration.ipynb
    │
    ├── models/                                 # 🧠 Trained models and checkpoints
    │
    ├── reports/                                # 📊 Generated reports
    │   └── figures/                            # Plots and charts
    │
    └── docs/                                   # 📚 Documentation (MkDocs ready)