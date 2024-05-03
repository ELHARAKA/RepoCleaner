import os
import subprocess
import requests
import pyfiglet # type: ignore

def display_splash():
    ascii_art = pyfiglet.figlet_format("RepoCleaner")
    print(ascii_art)
    print("Developed by Fahd El Haraka")
    print("Version: v1.0.1")
    print("Contact Information:")
    print("  Email: fahd@web3dev.ma")
    print("  Telegram: @thisiswhosthis")
    print("  Website: https://web3dev.ma")
    print("  GitHub: https://github.com/ELHARAKA")
    print("-" * 60)
    print("Important Notice:")
    print("  * Unexpected issues may occur if the instructions are not followed.")
    print("  * Deleting repositories is irreversible.")
    print("  * Ensure you have backed up all important data before proceeding.")
    print("-" * 60 + "\n")

def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def get_credentials():
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub personal access token: ")
    return username, token

def backup_repo(repo_url):
    """Clones the repository to a local directory as a backup."""
    backup_dir = 'backups'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    repo_name = repo_url.split('/')[-1]
    clone_cmd = f"git clone {repo_url} {backup_dir}/{repo_name}"
    print(f"Attempting to backup {repo_name}...")
    try:
        subprocess.run(clone_cmd, check=True, shell=True)
        print(f"Backup of {repo_name} completed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to backup {repo_name}.")

def list_repositories(repositories):
    """Lists all repositories."""
    print("Available repositories:")
    for repo in repositories:
        print(repo['name'])

def delete_repo(username, repo, headers):
    """Delete a specific repository."""
    url = f"https://api.github.com/repos/{username}/{repo['name']}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully deleted {repo['name']}")
    else:
        print(f"Failed to delete {repo['name']}: {response.status_code} {response.reason}")

def fetch_repos(username, headers):
    """Fetch all repositories of the user, both public and private."""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/search/repositories?q=user:{username}&per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get('items', [])
            if not data:
                break
            repos.extend(data)
            page += 1
        else:
            print(f"Failed to fetch repositories: {response.status_code} {response.reason}")
            break
    return repos

def main():
    username, token = get_credentials()
    clear_screen()
    display_splash()

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    print("Select option:\n")
    print("1. Delete all repositories.")
    print("2. Delete all forked repositories.")
    print("3. Delete all archived repositories.")
    print("4. Delete specific repositories.")
    print("5. Exit.\n")

    while True:
        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        repos = fetch_repos(username, headers)
        if not repos:
            print("No repositories found.")
            continue

        repos_to_delete = []
        if choice == '1':
            confirm = input("WARNING: You are about to delete ALL repositories. This cannot be undone. Type 'yes' to confirm: ")
            if confirm.lower() == 'yes':
                repos_to_delete = [repo for repo in repos]
            else:
                print("Deletion cancelled.")
                continue
        elif choice == '2':
            repos_to_delete = [repo for repo in repos if repo['fork']]
        elif choice == '3':
            repos_to_delete = [repo for repo in repos if repo['archived']]
        elif choice == '4':
            list_repositories(repos)
            repo_names = input("Enter repository names to delete, separated by commas: ")
            repo_names = [name.strip() for name in repo_names.split(',')]
            repos_to_delete = [repo for repo in repos if repo['name'] in repo_names]

        if repos_to_delete:
            backup_answer = input("Do you want to back up the selected repositories before deleting? (yes/no): ")
            if backup_answer.lower() == 'yes':
                for repo in repos_to_delete:
                    backup_repo(repo['clone_url'])

            print("Reviewing repositories to delete:")
            for repo in repos_to_delete:
                print(repo['name'])
            confirm = input("Confirm deletion of these repositories? (yes/no): ")
            if confirm.lower() == 'yes':
                for repo in repos_to_delete:
                    delete_repo(username, repo, headers)
            else:
                print("Deletion cancelled.")
        else:
            print("No matching repositories to delete.")

        print("Select another option:\n")

if __name__ == "__main__":
    main()
