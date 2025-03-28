
import os
from pathlib import Path

files = ['.github/workflows/.gitkeep', 'src/__init__.py', 'src/components/__init__.py', 'src/components/data_ingestion.py', 'src/components/data_transformation.py', 'src/components/model_trainer.py', 'src/components/model_evaluation.py', 'src/components/mlflow_utils.py', 'src/components/dvc_utils.py', 'src/components/terraform_config.py', 'src/pipeline/__init__.py', 'src/pipeline/training_pipeline.py', 'src/pipeline/prediction_pipeline.py', 'src/utils/__init__.py', 'src/utils/utils.py', 'src/logger/__init__.py', 'src/logger/logging.py', 'src/exception/__init__.py', 'src/exception/exception.py', 'tests/unit/__init__.py', 'tests/integration/__init__.py', 'experiment/experiments.ipynb', 'requirements.txt', 'requirements_dev.txt', 'setup.py', 'setup.cfg', 'pyproject.toml', 'tox.ini', 'init_setup.sh', 'Dockerfile', 'dvc.yaml', 'params.yaml', 'README.md', 'template.py']

for file in files:
    path = Path(file)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.touch()
