srpm:
	set -x ;\
	URL=$$(rpmspec -P *.spec | awk '/Source:/ {print $$2}') ;\
	echo "$${URL}" ;\
	FILE=$$(basename "$${URL}") ;\
	FILE=$$(echo "$${FILE%\?*}") ;\
	curl -L -o "$${FILE}" "$${URL}" ;\
	rpmbuild --define "_sourcedir $$(pwd)" \
	         --define "_specdir $$(pwd)" \
	         --define "_builddir $$(pwd)" \
	         --define "_srcrpmdir $$(pwd)" \
	         --define "_rpmdir $$(pwd)" \
	         --nodeps \
	         -bs \
	         *.spec ;\
	mv *.src.rpm "${outdir}"
