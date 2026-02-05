#!/usr/bin/env bash
set -e

echo "🔍 Checking duplicated code..."

export DJANGO_SETTINGS_MODULE=receitas.settings
export PYTHONPATH=$(pwd)

OUTPUT=$(pylint \
  --disable=all \
  --enable=duplicate-code \
  --load-plugins=pylint_django \
  $(find . -name "*.py" \
      -not -path "./venv/*" \
      -not -path "./migrations/*") \
  || true)

echo "$OUTPUT"

# Fail if duplicate code detected
if echo "$OUTPUT" | grep -q "R0801"; then
  echo "❌ Duplicate code detected!"
  exit 1
fi

echo "✅ No duplicated code found"

