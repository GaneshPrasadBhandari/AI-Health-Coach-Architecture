# import mlflow

# mlflow.set_experiment("test_experiment")

# with mlflow.start_run():
#     mlflow.log_param("learning_rate", 0.001)
#     mlflow.log_metric("accuracy", 0.85)


import mlflow
from src.logger.logging import logger

logger.info("Starting MLflow test run...")

with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("accuracy", 0.92)
    logger.info("Logged param1 and accuracy in MLflow")

logger.info("MLflow test run complete.")



from src.components.mlflow_utils import start_run, log_param, log_metric, log_artifact, end_run

start_run("mlflow_test_run")
log_param("learning_rate", 0.01)
log_metric("accuracy", 0.91)
log_artifact("README.md")  # just as an example
end_run()
