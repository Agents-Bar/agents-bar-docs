set -e

# Build part
export DOMAIN=docs.agents.bar
docker-compose build

# Deploy part
docker stack deploy -c docker-compose.yml --with-registry-auth agents-bar-docs
