#!/usr/bin/env python3
"""Publish reviewed generated Codex marketplaces; preserve parent history and use ordinary pushes."""
import argparse
import os
from pathlib import Path
import subprocess
import tempfile
import cookbook


def marketplace_files(variant):
    config, files = cookbook.plugin_files('codex', variant)
    root = {f'plugins/{config["name"]}/{name}': data for name, data in files.items()}
    path, metadata = cookbook.marketplace('codex', config)
    root[path] = cookbook.json_bytes(metadata)
    root['README.md'] = (f'# Cookbook by Pengusto — {variant}\n\n'
        f'Generated installation branch for version {config["version"]}. Source and issues: https://github.com/pengusto/cookbook\n\n'
        f'```sh\ncodex plugin marketplace add pengusto/cookbook --ref {variant}\n'
        'codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local\n```\n\n'
        'Start a fresh local Codex session. Install one naming variant at a time. '
        'Preserve an existing installation before explicitly replacing it. '
        'This skills-only package does not include or enable the optional local MCP sidebar.\n').encode()
    return root


def run(args, *, data=None, env=None):
    return subprocess.run(['git', *args], cwd=cookbook.ROOT, input=data, capture_output=True, check=True, env=env).stdout.decode().strip()


def publish(variant, push=False):
    files = marketplace_files(variant)
    if not push:
        print(f'{variant}: {len(files)} reviewed files; no Git mutation (pass --push to publish)')
        return
    ref = f'refs/heads/{variant}'
    remote = run(['ls-remote', '--heads', 'origin', ref])
    parent = None
    if remote:
        run(['fetch', 'origin', f'{ref}:refs/remotes/origin/{variant}'])
        parent = run(['rev-parse', f'refs/remotes/origin/{variant}'])
    with tempfile.TemporaryDirectory(prefix='cookbook-marketplace-') as temporary:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(temporary) / 'index'))
        run(['read-tree', '--empty'], env=env)
        for path, content in sorted(files.items()):
            blob = run(['hash-object', '-w', '--stdin'], data=content)
            mode = '100755' if '/bin/' in path else '100644'
            run(['update-index', '--add', '--cacheinfo', f'{mode},{blob},{path}'], env=env)
        tree = run(['write-tree'], env=env)
    if parent and tree == run(['rev-parse', parent+'^{tree}']):
        print(f'{variant}: unchanged ({parent})')
        return
    args = ['commit-tree', tree]
    if parent:
        args += ['-p', parent]
    source = run(['rev-parse', 'HEAD'])
    commit = run(args, data=f'build: refresh {variant} marketplace from {source}\n'.encode())
    run(['push', 'origin', f'{commit}:{ref}'])
    print(f'{variant}: published {commit} from source {source}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--push', action='store_true', help='Explicitly publish both generated branches; default is read-only')
    args = parser.parse_args()
    for variant in cookbook.VARIANTS:
        publish(variant, args.push)


if __name__ == '__main__':
    main()
