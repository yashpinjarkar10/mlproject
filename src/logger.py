import logging
import os
from datetime import datetime

# Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory path (not the file path)
logs_dir = os.path.join(os.getcwd(), "logs")

# Try to create logs directory with proper error handling
try:
    os.makedirs(logs_dir, exist_ok=True)
except PermissionError:
    # If we can't create in current directory, use /tmp for Docker
    logs_dir = "/tmp/logs"
    os.makedirs(logs_dir, exist_ok=True)
except Exception:
    # Fallback to /tmp if all else fails
    logs_dir = "/tmp"

# Create full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
try:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
except PermissionError:
    # If file logging fails, use console logging
    logging.basicConfig(
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
