from src.exception.exception import CustomException
import sys

try:
    something()
except Exception as e:
    raise CustomException(str(e), sys)
