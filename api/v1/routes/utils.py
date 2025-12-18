import os
import logging
import subprocess

from core_engine.exceptions import CoreEngineException

logger = logging.getLogger(__name__)

def create_directory(directory_path: str) -> None:
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as e:
        raise CoreEngineException(f"Failed to create directory: {e}")

def run_shell_command(command: str, capture_output: bool = True) -> str:
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        if capture_output:
            return output.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to execute command: {e}")
        raise CoreEngineException(f"Failed to execute command: {e}")