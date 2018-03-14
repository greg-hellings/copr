srpm:
	set -e ;\
	URL=$$(rpmspec -P *.spec | awk '/Source/ {print $$2}') ;\
	FILE=$$(basename "$${URL}") ;\
	FILE=$$(echo "$${FILE%\?*}") ;\
	curl -o "$${FILE}" "$${URL}" ;\
	rpkg -C /etc/rpkg.conf srpm --outdir "${outdir}" --spec "${spec}"
