cookiecutter-mytemplate/
├── cookiecutter.json
└── {{cookiecutter.project_slug}}/              # 👈 Project root
    
    │
    ├── artifacts/                              # Auto-generated outputs (checkpoints, logs, intermediate files)
    │   └── logs/                               # Logs for training, evaluation, debugging                
    │
    ├── data/                                   # 📂 Data folder
    │   ├── raw/                                # Unmodified source data
    │   ├── processed/                          # Final cleaned data for ML
    │   └── external/                           # 3rd-party data
    │
    ├── docs/                                   # 📚 Documentation (MkDocs ready)
    │
    ├── models/                                 # 🧠 Trained models and checkpoints
    │
    ├── notebooks/                              # 📒 Jupyter notebooks
    │   └── 1.0-init-exploration.ipynb          # EDA notebooks
    │
    ├── reports/                                # 📊 Generated reports
    │   └── figures/                            # Plots and charts
    │
    │ 
    ├── src/                                    # 🧠 Main source code
    │   ├── __init__.py                         # Makes src a Python package
    │   │
    │   │── data/
    │   │   ├── dataset.py                      # Data loading/generation scripts 
    │   │   ├── features.py                     # Feature engineering scripts   
    │   │   └── preprocess.py                   # Data cleaning and transformation logic 
    │   │
    │   │── models/
    │   │   ├── train.py                        # Model training scripts
    │   │   ├── predict.py                      # Inference logic
    │   │   └── evaluate.py                     # Metrics and model evaluation    
    │   │ 
    │   ├── utils/                              # Utilities
    │   │   ├── exceptions.py                   # Custom exception classes
    │   │   ├── logger.py                       # Centralized logger setup
    │   │   └── config.py                       # Project configs and constants
    │   │    
    │   └── visualization/           
    │       └── visualize.py                    # EDA, model results, charts, plots   
    │
    ├── tests/                                  # Unit and integration tests (pytest structure)
    │   ├── __init__.py
    │   └── test_sample.py
    │
    ├── pyproject.yml                           # 📦 Modern build config (Setuptools/Poetry)
    ├── setup.cfg                               # ⚙️ Config for tools (flake8, black, etc.)
    ├── requirements.txt                        # 📜 Environment dependencies
    ├── README.md                               # 📘 Project introduction
    ├── Makefile                                # 🛠️ Command shortcuts (e.g. make train)
    ├── .gitignore                              # 🙈 Ignore files/folders
    └── setup.py                                # ⚙️ Dynamic setup logic