%global src_base src/github.com/hashicorp
%global src_dir %{src_base}/%{name}

Name:		packer
Version:	1.6.2
Release:	1%{?dist}
Summary:	Create machine and container images for multiple platforms
License:	MPLv2.0
URL:		https://www.packer.io/

Source:		https://github.com/hashicorp/packer/archive/v%{version}.tar.gz

ExclusiveArch:	%{go_arches}

BuildRequires:	compiler(go-compiler)
BuildRequires:	golang-github-hashicorp-uuid-devel
BuildRequires:	golang-github-hashicorp-checkpoint-devel
BuildRequires:	golang-github-hashicorp-cleanhttp-devel
BuildRequires:	golang-github-mitchellh-cli-devel
BuildRequires:	golang-github-kardianos-osext-devel

%description
Packer is a tool for creating machine and container images for
multiple platforms from a single source configuration.

%prep
mkdir -p %{src_base}
tar xaf %{SOURCE0} -C %{src_base}
mv %{src_dir}-%{version} %{src_dir}

%build
export GOPATH=$(pwd):%{gopath}
cd %{src_dir}
%gobuild -o bin/packer

%install
cd %{src_dir}
install -d %{buildroot}%{_bindir}
# The name "packer" for the binary competes with other Fedora packages
install -m 755 bin/packer %{buildroot}%{_bindir}/packerio

%files
%license %{src_dir}/LICENSE
%doc %{src_dir}/README.md
%{_bindir}/packerio

%changelog
* Tue Sep 01 2020 Greg Hellings <greg.hellings@gmail.com> - 1.6.2-1
- Upstream version 1.6.2

* Wed Jun 24 2020 Greg Hellings <greg.hellings@gmail.com> - 1.6.0-1
- Upsream version 1.6.0

* Fri May 22 2020 Greg Hellings <greg.hellings@gmail.com> - 1.5.6-1
- Upstream version 1.5.6

* Sun Apr 26 2020 Greg Hellings <greg.hellings@gmail.com> - 1.5.5-1
- Upstream version 1.5.5

* Mon Feb 17 2020 Greg Hellings <greg.hellings@gmail.com> - 1.5.4-1
- Upstream version 1.5.4

* Wed May 01 2019 Greg Hellings <greg.hellings@gmail.com> - 1.4.0-1
- Upstream version 1.4.0

* Tue Nov 27 2018 Greg Hellings <greg.hellings@gmail.com> - 1.3.2-1
- New upstream 1.3.2-1

* Tue Mar 20 2018 Greg Hellings <greg.hellings@gmail.com> - 1.2.1-2
- Change to source build

* Tue Mar 20 2018 Greg Hellings <greg.hellings@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Thu May 05 2016 Josef Strzibny <strzibny@strzibny.name> - 0.10.0-1
- Update to 0.10.0

* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.8.6-1
- Initial package
