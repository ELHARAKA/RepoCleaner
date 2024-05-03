# RepoCleaner (V1.0.1)

RepoCleaner was developed by Fahd El Haraka. For inquiries or further information, you can reach out through the following channels:

- **Telegram**: [@Thisiswhosthis](https://t.me/Thisiswhosthis)
- **Website**: [Web3Dev](https://web3dev.ma)

Feel free to contact for any issues, suggestions, or contributions to the project.

## Introduction

RepoCleaner is a powerful command-line tool designed to help you efficiently manage your GitHub repositories. With RepoCleaner, you can effortlessly delete forked, archived, or specific repositories in bulk, ensuring your GitHub account remains clean and organized.

## Features

- **Comprehensive Repository Fetching**: Automatically fetches all repositories associated with your GitHub account.
- **Flexible Deletion Options**: Allows deletion of all forked repositories, all archived repositories, or any specific repositories you choose.
- **Backup Capabilities**: Offers the option to back up any repository before deletion, safeguarding your data.

## Prerequisites

To use RepoCleaner, you need:

- Python 3.10 or higher.
- A GitHub API access token with the following permissions:
  - `repo`: Full control of private repositories and access to public repositories.
  - `delete_repo`: Permission to delete repositories.
  Generate your token [here](https://github.com/settings/tokens).

## Installation

Install RepoCleaner directly from PyPI:

```bash
pip install repocleaner
```

## Usage

Once installed, you can run RepoCleaner from the command line:

```bash
repocleaner
```

### Steps to Follow:
- **Launch the Tool**: Start RepoCleaner by typing the command above in your terminal.
- **Follow On-Screen Instructions**: The tool will guide you through selecting repositories you wish to manage or delete.
- **Backup Recommendations**: Before deleting any repositories, it is strongly recommended to back up your data. This ensures that you do not lose any important information permanently.
- **Select Options Carefully**: Choose the appropriate option based on whether you want to delete all, forked, archived, or specific repositories. Each choice has significant consequences and cannot be undone.

## Contributing

- Contributions to RepoCleaner are welcome! Please refer to the contributing guidelines in the repository for more details on how to contribute.

## License
This project is licensed under the [MIT License](LICENSE).