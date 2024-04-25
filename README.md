# Educational Project

Welcome to my repository for the educational projects and exercises part of the DevOps Course. This repository contains the hands-on projects that I've developed to solidify my understanding of DevOps principles and practices.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Git: For cloning and managing version control.
- Docker and docker-compose: For running API.
- Postman or any API testing tool to interact with the APIs.

What things you need to install the software and how to install them

### Installing

Clone the repository:

```bash
git clone https://github.com/Creampanda/devops_course.git
cd devops_course
```


Configure Environment:
Set up PORT and VERSION environment variables.

### Starting the API

Run docker container

```bash
docker-compose up --build
```

### Verifying the API

Once the API is running, you can access it by opening a web browser and navigating to http://127.0.0.1:8000/info (8000 is default port, but you should use the one you set). For other endpoints, replace the path in the URL accordingly based on the available routes (e.g. /info/currency).

You can also use tools like curl or Postman to test the API endpoints:

```bash
curl http://127.0.0.1:8000/info
```

## API Reference

### General Information Endpoint

Go to http://127.0.0.1:8000/docs to get all endpoints information

#### GET /info

Returns general information about the API.

Response Example:

```json
{
  "version": "1.0.0",
  "service": "currency",
  "author": "a.karaulov"
}
```

### Currency Rates Endpoint

#### GET /info/currency

Fetches currency rates from the Central Bank of Russia. Can return rates for a specific currency or all available currencies.

Parameters:

| Name     | Type     | Data Type | Example    | Description                                                 |
| -------- | -------- | --------- | ---------- | ----------------------------------------------------------- |
| currency | optional | string    | USD        | ISO 4217 currency code. If not provided, returns all rates. |
| date     | optional | string    | 2016-01-06 | Date for the rates in YYYY-MM-DD format.                    |

Example Output:

```json
{
  "service": "currency",
  "data": {
    "USD": 33.4013,
    ...
  }
}
```

### Running the Tests

A step-by-step series of examples that tell you how to run tests


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
