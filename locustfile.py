from locust import HttpUser, task, between

class BasicTestUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def load_homepage(self):
        self.client.get("/")  # Replace with your actual endpoint

    @task
    def load_about_page(self):
        self.client.get("/blog.html")  # Replace with your actual endpoint
