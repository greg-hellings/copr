srpm: spectool
	./spectool -g *.spec ;\
	rpmbuild --define "_sourcedir $$(pwd)" \
	         --define "_specdir $$(pwd)" \
	         --define "_builddir $$(pwd)" \
	         --define "_srcrpmdir $$(pwd)" \
	         --define "_rpmdir $$(pwd)" \
	         --nodeps \
	         -bs \
	         *.spec ;\
	mv *.src.rpm "${outdir}"

spectool:
	curl -L -o "spectool" "https://pagure.io/rpmdevtools/raw/master/f/spectool.in"
	chmod +x spectool
