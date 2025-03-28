import os
import shutil
from datetime import datetime
import joblib

from src.logger.logging import CustomLogger
from src.exception.exception import CustomException
import sys

logger = CustomLogger(__name__).get_logger()

class ModelPusher:
    def __init__(self, model_path, model_name="best_model.pkl", save_dir="saved_models/"):
        self.model_path = model_path
        self.model_name = model_name
        self.save_dir = save_dir

    def push(self):
        try:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model not found at {self.model_path}")

            versioned_dir = os.path.join(self.save_dir, datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
            os.makedirs(versioned_dir, exist_ok=True)

            dest_path = os.path.join(versioned_dir, self.model_name)
            shutil.copy(self.model_path, dest_path)

            logger.info(f"✅ Model pushed to: {dest_path}")
            return dest_path

        except Exception as e:
            logger.error("❌ Failed to push model")
            raise CustomException(str(e), sys)
