# VSCode Devcontainers

The "terminal" of VS Code natively offers the user a command-line to her/his local environment, invoking `bash`, `zsh`, Windows PowerShell, Windows CMD, etc. This can be customized in a variety of ways, for example Windows users running WSL can use that terminal within VS Code, along with PowerShell or the Windows CMD.

The challenge for data scientists is creating and managing project environments without too much complexity or overhead.

Devcontainers provide a method for consistent local terminals by containerizing the interactive terminal. This means all students have the same software, the same environment configuration, and the same paths to their work.

## Advantages :thumbsup:

- Truly local environment, runs 100% on the student machine.
- Configuration can also be used in GitHub Codespaces!
- Supports most languages: Python, R, etc.
- Completely customizable. Can even use custom Dockerfile.
- Allows for port mappings, volume mappings, between computer and container

## Disadvantages :thumbsdown:

- Requires an understanding of the `devcontainers.json` file
- Built-in GitHub authentication is not automatic in all scenarios
- Available container images are specifically built for this use
- Access to other local files (`.ssh` directory, etc.) must be mapped in

## Learn More

Note the `.devcontainer/devcontainer.json` file, which configures the environment. This can include:

- Base devcontainer image to use; OR
- Dockerfile to build from
- Environment variables
- Mounts of local storage into the devcontainer
- Commands to run upon creation
- Port forwarding, etc.
- Other features available

## Try It Out

1. Two prerequisites before you start:

   - Be sure Docker is installed and running on your local machine.
   - Be sure to install the [**UVA Data Science Core Extension Pack**](https://marketplace.visualstudio.com/items?itemName=uva-school-of-data-science.sds-vscode). This includes the Devcontainer plugin.
   
2. In order to use `git` inside of the Devcontainer, a little setup is needed.
   
   - Instead of creating a new `.gitconfig` file for the container, the Devcontainer will map your file into the container.
   - Mark the container path as safe within your `~/.gitconfig` file by running this command:

        ```
        git config --global --add safe.directory '*'
        ```
    - We recommend using SSH key authentication to GitHub. (Go [here](SSH.md) for setup instructions.) Notice line 20 of the `.devcontainer/devcontainer.json` file maps the owner's SSH directory into the container.
    - Line 21 of the configuration maps your `~/.gitconfig` file into the container as well.

3. With that setup complete, fork and clone this repository to your local machine and open in VS Code.

4. You will be prompted in the lower-right corner of the screen that a Devcontainer configuration has been detected for this folder, asking if you would like to reopen it within the container. Click the **Reopen in Container** button to do so. 

5. Once the project reopens in the container, your terminal will display the container environment, running as the `vscode` user, and your project will be in a new path (that does not exist on your local system). Software and paths will be consistent for all users. Take a moment to query the path to Python3, or jq, etc.

6. This project contains a simple Python API framework called FastAPI. To run a preview of the application, run this command:

    ```
    ./preview.sh
    ```
   You will be prompted to open a browser to view and interact with the containerized API.
