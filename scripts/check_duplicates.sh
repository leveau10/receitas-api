#!/usr/bin/env bash
set -e

echo "🔍 Checking duplicated code..."

# Activate venv if CI uses one (optional)
# source venv/bin/activate

# Export Django settings
export DJANGO_SETTINGS_MODULE=receitas.settings

# Add project root to PYTHONPATH
export PYTHONPATH=$(pwd)

# Run pylint duplicate detection
pylint \
  --disable=all \
  --enable=duplicate-code \
  --load-plugins=pylint_django \
  $(find . -name "*.py" \
      -not -path "./venv/*" \
      -not -path "./migrations/*")

echo "✅ Duplicate check finished"
