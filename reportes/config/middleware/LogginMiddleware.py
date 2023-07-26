import logging


logger = logging.getLogger(__name__)


class LogginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        

    def __call__(self, request):
        response = self.get_response(request)
        level_status_code = {"DEBUG": [200], "WARNING": [400], "ERROR": [500]}

        status = response.status_code
        path = request.path_info

        if status in level_status_code["DEBUG"]:
            logger.info(f"{path}  {status}  Ok")
        
        elif status in level_status_code["WARNING"]:
            logger.warning(f"{path}  {status}  Not Ok")

        elif status in level_status_code["ERROR"]:
            logger.error(f"{path}  {status}  Important")
            
        return response
