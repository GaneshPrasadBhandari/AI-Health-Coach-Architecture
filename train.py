import os
import yaml
import mlflow
from src.components.data_ingestion import load_data
from src.components.data_transformation import preprocess_data
from src.components.model_trainer import train_model
from src.components.model_evaluation import evaluate_model
from src.components.model_pusher import ModelPusher
from src.logger.logging import CustomLogger
from src.exception.exception import CustomException
import sys

logger = CustomLogger(__name__).get_logger()

def read_params(config_path="params.yaml"):
    with open(config_path) as f:
        return yaml.safe_load(f)

def run_pipeline():
    try:
        config = read_params()

        # Start MLflow experiment
        mlflow.set_experiment(config["experiment"]["name"])
        with mlflow.start_run():
            logger.info("🚀 MLflow Run Started")

            # Load raw data
            data = load_data(config["data"]["path"])
            logger.info("✅ Data loaded successfully")

            # Preprocess
            X_train, X_test, y_train, y_test = preprocess_data(data, config)
            logger.info("🧹 Data preprocessing done")

            # Train
            model = train_model(X_train, y_train, config)
            logger.info("🤖 Model training completed")

            # Evaluate
            metrics = evaluate_model(model, X_test, y_test)
            logger.info(f"📊 Metrics: {metrics}")
            for k, v in metrics.items():
                mlflow.log_metric(k, v)

            # Save model
            model_path = "artifacts/model.pkl"
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            mlflow.sklearn.save_model(model, model_path)
            mlflow.log_artifact(model_path)

            # Push model
            pusher = ModelPusher(model_path=model_path)
            pusher.push()

            logger.info("✅ Pipeline completed successfully")

    except Exception as e:
        logger.error("❌ Pipeline failed")
        raise CustomException(str(e), sys)

if __name__ == "__main__":
    run_pipeline()
