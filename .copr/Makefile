srpm:
	set -e ;\
	URL=$$(rpmspec -P *.spec | awk '/Source/ {print $$2}') ;\
	FILE=$$(basename "$${URL}") ;\
	FILE=$$(echo "$${FILE%\?*}") ;\
	curl -o "$${FILE}" "$${URL}" ;\
	rpmbuild --define "_sourcedir $$(pwd)" \
	         --define "_specdir $$(pwd)" \
	         --define "_builddir $$(pwd)" \
	         --define "_srcrpmdir $$(pwd)" \
	         --define "_rpmdir $$(pwd)" \
	         --nodeps \
	         -bs \
	         *.spec ;\
	mv *.src.rpm "${outdir}"
