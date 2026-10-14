#!/usr/bin/env bash
# Ship the committed site to the server: ./deploy.sh root@89.108.76.133
set -Eeuo pipefail
HOST="${1:?usage: deploy.sh user@host}"
cd "$(git rev-parse --show-toplevel)"
[[ -z "$(git status --porcelain)" ]] || { echo "Commit your changes first." >&2; exit 1; }
REV="$(git rev-parse --short HEAD)"
# Only published files: no build scripts, README or repository metadata. Files get
# world-readable permissions here, whatever they are in the local checkout.
git archive --format=tar HEAD index.html en assets example-report.html | ssh "$HOST" "set -e
rm -rf /var/www/sitozor.new && mkdir -p /var/www/sitozor.new
tar -x --no-same-owner -C /var/www/sitozor.new
find /var/www/sitozor.new -type d -exec chmod 755 {} +
find /var/www/sitozor.new -type f -exec chmod 644 {} +
rm -rf /var/www/sitozor.old
if [ -d /var/www/sitozor ]; then mv /var/www/sitozor /var/www/sitozor.old; fi
mv /var/www/sitozor.new /var/www/sitozor"
echo "Shipped site $REV to $HOST:/var/www/sitozor"
