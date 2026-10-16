#!/bin/bash
# redeploy.sh — regenerate SDK table, push, rebuild RTD, re-import + publish GitBook
set -e; cd "$(dirname "$0")"; set -a; source ~/.claude/.env; set +a; export HTTPS_PROXY=http://127.0.0.1:1082
python3 gen-sdk-index.py >/dev/null
git add -A; git -c user.name=hanshs474 -c user.email=hanshs474@users.noreply.github.com commit -qm "${1:-docs update}" || true
git push -q "https://hanshs474:$GITHUB_TOKEN@github.com/hanshs474/emaki-docs.git" main
curl -s -X POST -H "Authorization: Token $RTD_API_TOKEN" https://readthedocs.org/api/v3/projects/emaki/versions/latest/builds/ >/dev/null
H="Authorization: Bearer $GITBOOK_API_TOKEN"
curl -s -o /dev/null -w "gitbook import %{http_code}\n" -X POST -H "$H" -H "Content-Type: application/json" https://api.gitbook.com/v1/spaces/QG9cPTxCsnWyYFW85ISe/git/import -d '{"url":"https://github.com/hanshs474/emaki-docs.git","ref":"refs/heads/main","force":true}'
sleep 15
curl -s -o /dev/null -w "gitbook publish %{http_code}\n" -X POST -H "$H" https://api.gitbook.com/v1/orgs/3LCdcxqOJHNoV0wUxyXQ/sites/site_68aqf/publish
