# RepoCleaner: Introduction

RepoCleaner is a tool designed to help you manage your GitHub repositories efficiently. With RepoCleaner, you can delete forked repositories, archived repositories, or specific repositories in bulk.

## Features

- Fetches all repositories associated with your GitHub account.
- Allows you to delete all forked repositories, all archived repositories, or specific repositories of your choice.
- Provides an option to back up repositories before deletion.

## Prerequisites

Before using RepoCleaner, make sure you have the following:

- Python 3.x
- GitHub API access token. You can generate a token [here](https://github.com/settings/tokens). Ensure your token has the following scopes:
  - `repo`: Full control of private repositories and access to public repositories.
  - `delete_repo`: Permission to delete repositories.

## Usage

1. Install the required dependencies:

    ```bash
    pip install pyfiglet
    ```

2. Run the script:

    ```bash
    python repocleaner.py
    ```

3. Follow the on-screen instructions to select the repositories you want to delete.

## License

This project is licensed under the [MIT License](LICENSE).
