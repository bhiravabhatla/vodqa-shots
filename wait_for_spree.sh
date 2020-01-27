#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until  [ $(curl -I spree:3000/login 2>/dev/null | head -n 1 | cut -d$' ' -f2   ) -eq 200 ] 2>/dev/null ; do
  >&2 echo "spree is unavailable - sleeping"
  sleep 1
done

>&2 echo "spree is up - executing tests"
exec $cmd