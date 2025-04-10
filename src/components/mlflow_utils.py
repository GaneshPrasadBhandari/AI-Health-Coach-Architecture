import mlflow
from src.logger.logging import logger

def start_run(run_name="default_run"):
    logger.info(f"Starting MLflow run: {run_name}")
    mlflow.start_run(run_name=run_name)

def log_param(key, value):
    logger.info(f"Logging param: {key}={value}")
    mlflow.log_param(key, value)

def log_metric(key, value):
    logger.info(f"Logging metric: {key}={value}")
    mlflow.log_metric(key, value)

def log_artifact(path):
    logger.info(f"Logging artifact from: {path}")
    mlflow.log_artifact(path)

def end_run():
    logger.info("Ending MLflow run")
    mlflow.end_run()
