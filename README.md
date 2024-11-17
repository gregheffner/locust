# Locust Load Testing

This repository contains scripts for load testing using Locust.

## Prerequisites

- Python 3.7+
- Locust

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gregheffner/locust.git
    cd locust
    ```

## Usage

To start the Locust workers on a Mac M2 with 8 cores, use the following commands:
```sh
locust -f locustfile.py --worker --master-host=127.0.0.1 --expect-workers=8
```
```sh
chmod + x start_workers.sh && /.start_workers.sh
```

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.