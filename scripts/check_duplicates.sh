
echo "🔍 Checking duplicated code..."

OUTPUT=$(pylint --jobs=1 --enable=R0801 $(git ls-files "*.py") || true)

echo "$OUTPUT"

if echo "$OUTPUT" | grep -q "R0801"; then
  echo "❌ Duplicate code detected!"
  exit 1
else
  echo "✅ No duplicated code found."
fi