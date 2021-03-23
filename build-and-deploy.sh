set -e

# Build part
export DOMAIN=docs.agents.bar \
docker-compose build

# Deploy part
docker stack deploy -c docker-compose.ym --with-registry-auth agent-bar-docs

