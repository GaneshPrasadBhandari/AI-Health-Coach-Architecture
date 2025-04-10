# AI-Health-Hackers-HealthCoach
Personalized AI Health Coach

---

## 📝 Logging Setup

Custom logging is implemented in `src/logger/logging.py`.

Logs are saved in `logs/YYYY-MM-DD.log` format.

### Format:
```bash
[TIMESTAMP] | [LEVEL] | [MODULE] | [MESSAGE]


Example:
2025-04-10 19:22:30 | INFO | logging | MLflow test run complete.


How to Use:
from src.logger.logging import logger

logger.info(\"Your message here\")




README.md Section to Add
---

## 📦 DVC Multi-Remote Setup (Azure | AWS | Local)

Create a `.env` file and set one of the following remotes:

### ✅ Local Example:
```env
LOCAL_DVC_PATH=./dvc-storage



✅ Azure Example:
AZURE_STORAGE_ACCOUNT_NAME=your_name
AZURE_STORAGE_ACCOUNT_KEY=your_key
AZURE_DVC_CONTAINER=your-container


✅ AWS S3 Example:
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_DVC_BUCKET=your_bucket


---

## 🛠 Universal Path Handling (Cross-Platform)

We use Python's `pathlib` to resolve paths safely across OS (Windows/Linux/macOS).

### 📄 src/utils/path_utils.py

```python
from pathlib import Path
import os

def get_local_dvc_path():
    return Path(os.getenv(\"LOCAL_DVC_PATH\")).expanduser().resolve()


Use like this:
from src.utils.path_utils import get_local_dvc_path
dvc_path = get_local_dvc_path()

Note:- This automatically resolves slashes, user directories, and full paths.


---

## 📊 MLflow Tracking Setup

MLflow is used to log model experiments (parameters, metrics, artifacts).

### ✅ How to Use:

1. Start a run:
```python
start_run(\"run_name\")

Log values
log_param(\"key\", value)
log_metric(\"key\", value)
log_artifact(\"path/to/file\")


End the run:
end_run()

🖥️ Launch UI:
mlflow ui
Visit http://127.0.0.1:5000 to see your experiments.

Logs are also saved in logs/YYYY-MM-DD.log

