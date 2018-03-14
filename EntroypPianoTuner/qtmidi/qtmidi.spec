%global debug_package %{nil}
%global container_name qtmidi
%global _summary Platform independent MIDI module for Qt 5.

Name:           qtmidi
Version:        0.1
Release:        2%{?dist}
Summary:        %{_summary}
License:        GPLv3
Url:            https://gitlab.com/tp3/qtmidi

Source:         https://gitlab.com/tp3/qtmidi/repository/archive.tar.bz2?ref=v%{version} #/archive.tar.bz2
BuildRequires:  alsa-lib-devel
BuildRequires:  qt5-qtbase-devel
#to create the forwarding headers
BuildRequires:  perl
BuildRequires:  xz

%description
This package contains a plugin to support MIDI input and output devices
in Qt-based applications.

%package -n qt5-%{name}
Summary:        %{_summary}

%description -n qt5-%{name}
This package contains a plugin to support MIDI input and output devices
in Qt-based applications.

%package -n qt5-%{name}-devel
Summary:        %{_summary} Development files.
Requires:       qt5-%{name} = %{version}
Requires:       qt5-qtbase-devel
Suggests:       libpulse-devel
Suggests:       libwmf-devel
Suggests:       openal-soft-devel

%description -n qt5-%{name}-devel
Header files and libraries for developing applications with qtmidi.

%package -n qt5-%{name}-private-headers-devel
Summary:        Non-ABI stable experimental API for qtmidi
BuildArch:      noarch
Requires:       qt5-%{name}-devel = %{version}

%description -n qt5-%{name}-private-headers-devel
This package provides private headers of libqt5-qtmidi that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%prep
# standard setup, but rename the dir in the archive, because it contains its commit hash!
tar xaf %{SOURCE0}
if [ $? -ne 0 ]; then
  exit $?
fi

# remove commit number and move files to build dir
mv "%{container_name}-v%{version}-"* "%{container_name}-%{version}"
tar caf %{SOURCE0} "%{container_name}-%{version}"
%autosetup -n "%{container_name}-%{version}"

%build
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
qmake-qt5 -r
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
find %{buildroot}/ -type f -name '*.la' -delete
find %{buildroot}/%{_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} \; -exec sed -i -e "s,^moc_location=.*,moc_location=%{_lib}qt5_bindir/moc," -e "s,uic_location=.*,uic_location=%{_lib}qt5_bindir/uic," {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n qt5-%{name}
%license LICENSE.GPLv3
%doc README.md
%{_libdir}/libQt5*.so.*
%{_libdir}/libQt5*.so
%{_libdir}/qt5/plugins/midi

%files -n qt5-%{name}-private-headers-devel
%{_includedir}/qt5/QtMidi/*/QtMidi*

%files -n qt5-%{name}-devel
%license LICENSE.GPLv3
%doc README.md
%{_libdir}/cmake/Qt5*
%{_libdir}/libQt5*.prl
%{_libdir}/pkgconfig/Qt5*.pc
%exclude %{_includedir}/qt5/QtMidi/*/QtMidi*
%{_includedir}/qt5/QtMidi
%{_libdir}/qt5/mkspecs/modules/qt_lib_*.pri

%changelog
* Mon Sep 25 2017 Greg Hellings <greg.hellings@gmail.com> - 0.1-2
- Updates and binary package renames per review
- Clean up superfluous metadata
- Fix spelling problems
- Correct and clarify descriptions and summaries

* Thu May 11 2017 Greg Hellings <greg.hellings@gmail.com> - 0.1-1
- First Fedora package prep
- Adapt upstream provided spec file, remove distro-specific portions
