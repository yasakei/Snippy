#!/usr/bin/env python3

import argparse
import json
import os
import subprocess
import sys

SNIPPETS_FILE = os.path.expanduser("~/.config/snippy/snippets.json")

def get_snippets():
    if not os.path.exists(SNIPPETS_FILE):
        return {}
    with open(SNIPPETS_FILE, "r") as f:
        return json.load(f)

def save_snippets(snippets):
    with open(SNIPPETS_FILE, "w") as f:
        json.dump(snippets, f, indent=4)

def save_snippet(args):
    snippets = get_snippets()
    snippets[args.name] = args.command
    save_snippets(snippets)
    print(f"Snippet '{args.name}' saved.")

def list_snippets(args):
    snippets = get_snippets()
    if not snippets:
        print("No snippets found.")
        return
    for name, command in snippets.items():
        print(f"{name}: {command}")

def run_snippet(args):
    snippets = get_snippets()
    if args.name not in snippets:
        print(f"Snippet '{args.name}' not found.")
        sys.exit(1)
    
    try:
        subprocess.run(snippets[args.name], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running snippet '{args.name}': {e}", file=sys.stderr)
        sys.exit(e.returncode)

def edit_snippet(args):
    snippets = get_snippets()
    if args.name not in snippets:
        print(f"Snippet '{args.name}' not found.")
        sys.exit(1)
    
    new_command = input(f"Current command for '{args.name}': {snippets[args.name]}\nEnter new command: ")
    if new_command:
        snippets[args.name] = new_command
        save_snippets(snippets)
        print(f"Snippet '{args.name}' updated.")
    else:
        print("No changes made.")

def delete_snippet(args):
    snippets = get_snippets()
    if args.name not in snippets:
        print(f"Snippet '{args.name}' not found.")
        sys.exit(1)
    del snippets[args.name]
    save_snippets(snippets)
    print(f"Snippet '{args.name}' deleted.")

def main():
    parser = argparse.ArgumentParser(description="A shell command snippet manager.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Save command
    save_parser = subparsers.add_parser("save", help="Save a new snippet.")
    save_parser.add_argument("name", help="The name of the snippet.")
    save_parser.add_argument("command", help="The shell command to save.")
    save_parser.set_defaults(func=save_snippet)

    # List command
    list_parser = subparsers.add_parser("list", help="List all snippets.")
    list_parser.set_defaults(func=list_snippets)

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a saved snippet.")
    run_parser.add_argument("name", help="The name of the snippet to run.")
    run_parser.set_defaults(func=run_snippet)

    # Edit command
    edit_parser = subparsers.add_parser("edit", help="Edit a saved snippet.")
    edit_parser.add_argument("name", help="The name of the snippet to edit.")
    edit_parser.set_defaults(func=edit_snippet)

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a saved snippet.")
    delete_parser.add_argument("name", help="The name of the snippet to delete.")
    delete_parser.set_defaults(func=delete_snippet)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
