## **Overview**

The GitHub Test Action is an automated workflow that runs tests on your code every time a pull request is created. This ensures that changes to the code do not break existing functionality. nosetests is a testing framework for Python that makes it easy to write and run tests for your Python code.

## **Prerequisites**

Before you set up the test action, you need to have the following:

*   A GitHub repository for your Python application
*   A Python application with test files using nosetests

## **Set Up the Test Action**

To set up the test action for your Python application, follow these steps:

Create a **.github/workflows** directory in the root of your repository.

Create a new YAML file in the **.github/workflows** directory. You can name the file whatever you like, but it must have a **.yml** extension. For example, **test.yml**.

Add the following code to the YAML file:

```plaintext
name: Test

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: UNIT TEST REPO
              uses: nikson-a/unit-test-action@main
              env:
                  github_token: ${{ secrets.GITHUB_TOKEN }}
                  github_repository: ${{ github.repository }}
                  commit_id: ${{ github.event.pull_request.head.sha }}
                  expect_coverage: 90

```

Commit and push the changes to your repository.

## **Run the Test Action**

The test action will run automatically every time a pull request is created. You can also run the test action manually by following these steps:

Go to the Actions tab in your repository.

Click on the test workflow to view the details.

Click on the "Run workflow" button to run the test action.


## **Sample Output**

<img width="852" alt="Screenshot 2023-02-21 at 11 20 42 PM" src="https://user-images.githubusercontent.com/43266690/220422362-583324fc-f07c-4fd6-a786-ef82dc9cdecf.png">


## **Conclusion**

The GitHub Test Action using Pytest is a powerful tool for ensuring the quality and reliability of your Python application. By following the steps outlined in this readme file, you can easily set up and run tests for your Python code in GitHub. This updated version of the readme is for the repository [https://github.com/nikson-a/nose-test-workflow](https://github.com/nikson-a/nose-test-workflow).
