# Snippy: Your Personal Command-Line Snippet Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Snippy is a simple yet powerful command-line tool for saving, managing, and running your favorite shell command snippets. Stop memorizing long commands or searching through your shell history. With Snippy, your most-used commands are just a name away.

## Features

- **Save Snippets:** Save any shell command with a short, memorable name.
- **List Snippets:** View all your saved snippets in a clean list.
- **Run Snippets:** Execute a saved command by its name.
- **Edit Snippets:** Modify existing snippets on the fly.
- **Delete Snippets:** Remove snippets you no longer need.
- **Cross-Platform:** Works on macOS and Linux.
- **Lightweight:** A single Python script with no external dependencies.

## Installation

### One-Line Install (macOS/Linux)

You can install Snippy with a single command. This will download the script and set it up for you.

```bash
curl -sSL https://raw.githubusercontent.com/yasakei/Snippy/main/install.sh | sudo bash
```

### Manual Install

1.  **Clone the repository.**
    ```bash
    git clone https://github.com/yasakei/Snippy.git
    cd Snippy
    ```

2.  **Run the installer.**
    ```bash
    sudo ./install.sh
    ```

That's it! Snippy is now installed. You can verify the installation by running:
```bash
snippy list
```

## Usage

Snippy is designed to be intuitive. Here are the available commands:

### `save`

Save a new command snippet.

**Syntax:**
```bash
snippy save <name> "<command>"
```

**Example:**
```bash
snippy save list-all "ls -la"
```

### `list`

List all your saved snippets.

**Syntax:**
```bash
snippy list
```

### `run`

Run a saved snippet.

**Syntax:**
```bash
snippy run <name>
```

**Example:**
```bash
snippy run list-all
```

### `edit`

Edit an existing snippet. You will be prompted to enter the new command.

**Syntax:**
```bash
snippy edit <name>
```

**Example:**
```bash
snippy edit list-all
```

### `delete`

Delete a snippet.

**Syntax:**
```bash
snippy delete <name>
```

**Example:**
```bash
snippy delete list-all
```

## Data Storage

Snippets are stored in a simple JSON file located at `~/.config/snippy/snippets.json`. You can manually edit this file if you need to, but using the `snippy` commands is recommended.

## Contributing

Contributions are welcome! If you have ideas for new features, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
