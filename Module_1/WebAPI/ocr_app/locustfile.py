from locust import HttpUser, between, task
from loguru import logger


class ModelUser(HttpUser):
    # Wait between 1 and 3 seconds between requrests
    wait_time = between(1, 3)

    def on_start(self):
        logger.info("Load your model here")

    @task
    def predict(self):
        # logger.info("Sending POST requests!")
        # image = open('examples/receipt.jpg', 'rb')
        # files = {'file': image}
        # self.client.post(
        #     "/ocr",
        #     files=files,
        # )
        logger.info("Sending GET requests!")
        self.client.get(
            "/simple",
        )
