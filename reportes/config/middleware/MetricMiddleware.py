import logging
import time


logging.basicConfig(
    filename="metric.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
)


class MetricMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        end_time = time.perf_counter()

        total_time = end_time - start_time

        logger = logging.getLogger("debug")
        logger.info(f"Total time: {(total_time):.2f}s")
        print(f"Total time: {(total_time):.2f}s")

        return response
