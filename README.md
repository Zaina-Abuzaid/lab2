![CI](https://github.com/Zaina-Abuzaid/lab2/actions/workflows/ci.yml/badge.svg)

# Lab 2 - Bring Your Own Model

## About My Project

In this lab, I worked on a customer churn prediction model. The goal was to take my machine learning model and make it work through an API using FastAPI.

I also used Docker to run the application inside a container, and GitHub Actions to automatically test the project.

## What I Used

* Python for the project.
* FastAPI to create the API.
* A trained machine learning model to predict customer churn.
* Pytest to test the application.
* Docker to build and run the container.
* GitHub Actions for CI/CD.
* Trivy to check the Docker image for security vulnerabilities.

## How to Run My Project

First open the lab2 project in VS code and open a new terminal.

Build the Docker image using this command:

docker build -t lab2-churn .

Then run the container:

docker run –rm -p 8000:8000 lab2-churn

After running it, open this link to test the API:

http://localhost:8000/docs

## The API has two endpoints:

* /health: Checks if the API is working.
* /predict: Uses the model to make a churn prediction.

## How to Run the Tests

To run the tests, use:

python -m pytest

I added automated tests to check that the API works correctly.



GitHub Actions

I created a GitHub Actions workflow to run tests and build the Docker image automatically.

I also added Trivy to scan the image for security issues.

The workflow is set up to publish the Docker image to GitHub Container Registry (GHCR) after a successful run on the main branch.

What Broke

One of the main problems I faced was with the Trivy security scan.

It reported five HIGH vulnerabilities in some Python packages. I tried updating the packages and rebuilding the Docker image, but the scan still reported the same vulnerabilities.

The tests passed, but the Docker job failed because of the security scan.



# What I Learned:

In this lab, I learned how to organize my machine learning project and connect my model to an API.

I also learned how to write automated tests, build Docker images, and use GitHub Actions.

The Trivy problem helped me understand that even when the application works correctly, security checks can still cause the CI/CD pipeline to fail.

I also learned how to read GitHub Actions logs and troubleshoot errors step by step.

## GHCR Image Digest: sha256:0ae96fc880cdf7500d028f708310e01561b091eafe7a80e04b25bd9278963bdc