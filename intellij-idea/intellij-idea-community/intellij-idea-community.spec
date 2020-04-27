# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
%define debug_package %{nil}
# there are some python 2 and python 3 scripts so there is no way out to bytecompile them ^_^
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global build_vers 201.6668.121
%global idea_name idea-IC

%if 0%{?rhel} > 7 || 0%{?fedora} > 29 || 0%{?epel} > 7
%bcond_with python3
%global shell_python %{__python3}
%global py_devel python3-devel
%global py_runtime python3
%else
%bcond_without python3
%global shell_python %{__python2}
%global py_devel python2-devel
%global py_runtime python2
%endif

Name:          intellij-idea-community
Version:       2020.1
Release:       1%{?dist}
Summary:       Intelligent Java IDE
License:       ASL 2.0
URL:           https://www.jetbrains.com/idea/

Source0:       https://download.jetbrains.com/idea/ideaIC-%{version}-no-jbr.tar.gz
#              https://download-cf.jetbrains.com/idea/ideaIC-2018.1.3-no-jdk.tar.gz

Source101:     intellij-idea.xml
Source102:     intellij-idea-community.desktop
Source103:     intellij-idea-community.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util
BuildRequires: %{py_devel}
Requires:      %{py_runtime}
Requires:      java

%description
IntelliJ IDEA analyzes your code, looking for connections between symbols
across all project files and languages.  Using this information it provides
indepth coding assistance, quick navigation, clever error analysis, and, of
course, refactorings.

%package doc
Summary:       Documentation for intelligent Java IDE
BuildArch:     noarch

%description doc
This package contains documentation for Intelligent Java IDE.

%prep
%setup -q -n %{idea_name}-%{build_vers}
for py_file in $(find . -name '*.py'); do
	sed -e '1s,#!/usr/bin/env python,#!%{shell_python},' \
	    -e '1s,#!/usr/bin/python.*,#!%{shell_python},' \
	    -i "${py_file}";
done

%build

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_bindir}

cp -arf ./{lib,bin,plugins} %{buildroot}%{_javadir}/%{name}/

rm -f %{buildroot}%{_javadir}/%{name}/bin/fsnotifier{,-arm}
cp -af ./bin/idea.png %{buildroot}%{_datadir}/pixmaps/idea.png
cp -af %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
cp -af %{SOURCE102} %{buildroot}%{_datadir}/%{name}.desktop
cp -a %{SOURCE103} %{buildroot}%{_datadir}/appdata
ln -s %{_javadir}/%{name}/bin/idea.sh %{buildroot}%{_bindir}/idea
desktop-file-install \
  --add-category="Development" \
  --delete-original \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/intellij-idea-community.desktop

%check
appstream-util validate-relax \
  --nonet %{buildroot}%{_datadir}/appdata/intellij-idea-community.appdata.xml

%files
%{_datadir}/applications/intellij-idea-community.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/idea.png
%{_datadir}/appdata/intellij-idea-community.appdata.xml
%{_javadir}/%{name}
%{_bindir}/idea

%post
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files doc
%doc *.txt
%license license/

%changelog
* Sun Apr 26 2020 Greg Hellings <greg.hellings@gmail.com> - 2020.1-1
- Update to 2020.1

* Wed May 01 2019 Greg Hellings <greg.hellings@gmail.com> - 2019.1.1-1
- Update to 2019.1.1
- Fixed builds for py2/3 deps, which were inverted

* Mon Feb 17 2019 Greg Hellings <greg.hellings@gmail.com> - 2019.3.3-1
- Update to 2019.3.3

* Tue Nov 27 2018 Greg Hellings <greg.hellings@gmail.com> - 2018.3-1
- Update to 2018.3

* Tue Aug 28 2018 Greg Hellings <greg.hellings@gmail.com> - 2018.2.2-1
- Update to 2018.2.2

* Tue Jul 10 2018 Greg Hellings <greg.hellings@gmail.com> - 2018.1.5-1
- Update to 2018.1.5

* Tue May 22 2018 Lars Kiesow <lkiesow@uos.de> - 2018.1.4-1
- Update to 2018.1.4

* Wed May 16 2018 Lars Kiesow <lkiesow@uos.de> - 2018.1.3-1
- Update to 2018.1.3

* Tue Dec 05 2017 Petr Hracek <phracek@redhat.com> - 2017.3-1
- Initial package
