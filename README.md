# Locust App

This README will guide you through the process of downloading and configuring the Locust app.

## Downloading Locust

First, download my repo and Locust app from the official repository and run it:
```sh
git clone https://github.com/gregheffner/locust.git
cd locust
```
```sh
pip install locust
locust
```

## Usage

To start the Locust workers on a Mac M2 with 8 cores, use the following commands:

```sh
locust -f locustfile.py --worker --master-host=127.0.0.1 --expect-workers=8
```
```sh
chmod + x start_workers.sh && /.start_workers.sh
```

## Configuration

Save your changes and run Locust again to see the effects of your configuration.

## Documentation

For more detailed information, please refer to the [official Locust documentation](https://docs.locust.io/en/stable/).
