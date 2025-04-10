import os
from dotenv import load_dotenv
import subprocess
from src.logger.logging import logger
from src.exception.exception import CustomException
from src.utils.path_utils import get_local_dvc_path, ensure_path

local_path = get_local_dvc_path()
ensure_path(local_path)


load_dotenv()

def run_cmd(cmd_list, description=""):
    try:
        subprocess.run(cmd_list, check=True)
        logger.info(f"✅ {description}: {' '.join(cmd_list)}")
    except Exception as e:
        logger.error(f"❌ Failed to run {description}: {cmd_list}")
        raise CustomException(e)

try:
    if os.getenv("AZURE_STORAGE_ACCOUNT_NAME"):
        logger.info("Configuring Azure Blob as DVC remote")
        run_cmd(["dvc", "remote", "add", "-d", "azure_remote", f"azure://{os.getenv('AZURE_DVC_CONTAINER')}/dvc"], "Add Azure remote")
        run_cmd(["dvc", "remote", "modify", "azure_remote", "account_name", os.getenv("AZURE_STORAGE_ACCOUNT_NAME")], "Azure account name")
        run_cmd(["dvc", "remote", "modify", "azure_remote", "account_key", os.getenv("AZURE_STORAGE_ACCOUNT_KEY")], "Azure key")

    elif os.getenv("AWS_ACCESS_KEY_ID"):
        logger.info("Configuring AWS S3 as DVC remote")
        run_cmd(["dvc", "remote", "add", "-d", "s3_remote", f"s3://{os.getenv('AWS_DVC_BUCKET')}/dvc"], "Add S3 remote")
        run_cmd(["dvc", "remote", "modify", "s3_remote", "access_key_id", os.getenv("AWS_ACCESS_KEY_ID")], "AWS access key")
        run_cmd(["dvc", "remote", "modify", "s3_remote", "secret_access_key", os.getenv("AWS_SECRET_ACCESS_KEY")], "AWS secret")

    elif os.getenv("LOCAL_DVC_PATH"):
        logger.info("Configuring Local Path as DVC remote")
        local_path = os.getenv("LOCAL_DVC_PATH")
        os.makedirs(local_path, exist_ok=True)
        # run_cmd(["dvc", "remote", "add", "-d", "local_remote", local_path], "Add local remote")
        run_cmd(["dvc", "remote", "add", "-f", "-d", "local_remote", str(local_path)], "Add local remote")


    else:
        raise ValueError("No valid DVC remote configuration found in .env")

except Exception as e:
    logger.exception("Error during DVC remote setup")
