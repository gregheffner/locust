"""
This script defines a Locust performance test user for load testing a web application.

Classes:
    BasicTestUser (HttpUser): A Locust user class that simulates a user performing tasks on a web application.

Tasks:
    load_homepage: Simulates a user loading the homepage.
    load_about_page: Simulates a user loading the about page.

Attributes:
    wait_time (between): The wait time between tasks, set to a random value between 1 and 5 seconds.
"""

from locust import HttpUser, between, task


class BasicTestUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def load_homepage(self):
        self.client.get("/")  # Replace with your actual endpoint

    @task
    def load_about_page(self):
        self.client.get("/blog.html")  # Replace with your actual endpoint
