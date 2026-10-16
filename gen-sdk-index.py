#!/usr/bin/env python3
"""Rebuild docs/sdk/index.md from the emaki-<lang> repos that exist on GitHub (rerun as SDKs land)."""
import json, os, re, subprocess, urllib.request
ROOT = os.path.expanduser('~/shnext/2608/emaki-pkgs')
LANG = {'py': 'Python', 'ts': 'JavaScript / TypeScript', 'go': 'Go', 'rs': 'Rust', 'java': 'Java / Kotlin',
        'rb': 'Ruby', 'dart': 'Dart / Flutter', 'ex': 'Elixir', 'r': 'R', 'lua': 'Lua', 'd': 'D',
        'php': 'PHP', 'dotnet': '.NET', 'clj': 'Clojure', 'docker': 'Docker (CLI image)', 'mcp': 'MCP server'}
req = urllib.request.Request('https://api.github.com/users/hanshs474/repos?per_page=100&sort=created',
                             headers={'User-Agent': 'emaki-docs'})
repos = {r['name'] for r in json.load(urllib.request.urlopen(req))}
rows = []
for suf, name in LANG.items():
    repo = f'emaki-{suf}'
    if repo not in repos or suf == 'mcp':
        continue
    readme = os.path.join(ROOT, repo, 'README.md')
    inst = ''
    if os.path.exists(readme):
        txt = open(readme).read()
        m = re.search(r'^(pip install \S+|npm install \S+|go get \S+|cargo add \S+|gem install \S+|dart pub add \S+|luarocks install \S+|dub add \S+|composer require \S+|dotnet add package \S+|docker run [^\n]+|install\.packages\([^\n]+\)|\{:emaki[^\n]*\})', txt, re.M)
        if m: inst = m.group(1)
        else:
            m = re.search(r'<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>', txt)
            if m: inst = f'{m.group(1)}:{m.group(2)}'
    rows.append(f'| {name} | `{inst}` | [hanshs474/{repo}](https://github.com/hanshs474/{repo}) |' if inst else
                f'| {name} | see the repository | [hanshs474/{repo}](https://github.com/hanshs474/{repo}) |')
out = ['# SDKs', '',
       'Official SDK clients for emaki (emaki.ai), the Japanese-language AI video generator for Seedance 2.5 and Seedance 2.0. '
       'Every client has the same surface: `generate_video(prompt, model="seedance_2_5", ...)` and `generate_image(prompt, model="nano_banana_2_lite", ...)` '
       'wait for the run and return the file URL; `submit`, `status` and `credits` are there for finer control. '
       'All of them read `EMAKI_API_KEY` ([create a key](https://emaki.ai/settings/apikeys)).', '',
       '| Language | Install | Source |', '|---|---|---|', *rows, '',
       'From an agent instead of code: the [MCP server](../integrations/mcp.md). Writing your own client: the [HTTP API](../http.md) is two calls.', '',
       'Default video model: [Seedance 2.5](https://emaki.ai/seedance-2-5). For [image to video](https://emaki.ai/image-to-video), pass a first-frame URL as `image`.', '']
open(os.path.join(ROOT, 'emaki-docs/docs/sdk/index.md'), 'w').write('\n'.join(out))
print('\n'.join(rows))
