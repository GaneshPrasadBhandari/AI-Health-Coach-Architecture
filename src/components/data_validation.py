import pandas as pd
import yaml
import os
from src.logger.logging import logger
from src.exception.exception import CustomException
import sys

class DataValidator:
    def __init__(self, data_path="data/raw/xray_dummy_detailed.csv", expected_schema_path="config/schema.yaml"):
        self.data_path = data_path
        self.expected_schema_path = expected_schema_path

    def validate(self):
        try:
            logger.info(f"Loading dataset from {self.data_path}")
            df = pd.read_csv(self.data_path)

            if not os.path.exists(self.expected_schema_path):
                raise FileNotFoundError(f"Schema file not found: {self.expected_schema_path}")

            with open(self.expected_schema_path, "r") as f:
                schema = yaml.safe_load(f)

            missing_columns = [col for col in schema["columns"] if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing columns: {missing_columns}")

            logger.info("✔️ Column schema validation passed.")

            # Null value check
            nulls = df.isnull().sum()
            null_report = nulls[nulls > 0]
            if not null_report.empty:
                logger.warning(f"⚠️ Null values detected:\n{null_report}")
            else:
                logger.info("✔️ No null values found.")

            logger.info("Data validation completed.")
            return True

        except Exception as e:
            raise CustomException(str(e), sys)
