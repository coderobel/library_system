import logging
import time
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def track_access(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        logger.info(f" [{timestamp}] Accessing Method: '{func.__name__}'")
        logger.info(f"Arguments : args={args}, kwargs={kwargs}")
        
        return func(*args, **kwargs)

    return wrapper

def permission_check(required_role):
    
    def decorator(func):
        @wraps(func)

        def wrapper(user_role, *args, **kwargs):
            if user_role == required_role:
                return func(user_role, *args, **kwargs)
            else:
                print(f"Permission Denied: User role '{user_role}' is not '{required_role}' ")
                return None
        
        return wrapper
    return decorator
