# Source from gitlab
# Change the hash according to the current master branch
%global BRANCH_DATE 20190107
%global BRANCH  ee7857ac

Summary:        Entropy Piano Tuner
Name:           entropypianotuner
Version:        1.2.0
Release:        4.%{BRANCH_DATE}git%{BRANCH}%{?dist}
License:        GPL-3.0
URL:            http://www.piano-tuner.org

# Workaround for source containing a '?' (commend at end)
%global ARCHIVE archive.tar.bz2?ref=%BRANCH
%global OWNER tp3
%global PROJECT Entropy-Piano-Tuner
%global tp3log_ref d0310d65

Source:         https://gitlab.com/%OWNER/%PROJECT/repository/%ARCHIVE #/Entropy-Piano-Tuner.tar.bz2
Source1:        %{name}.desktop
Source101:      https://gitlab.com/tp3/tp3log/repository/archive.tar.bz2?ref=%{tp3log_ref} #/tp3log.tar.bz2
BuildRequires:  fdupes
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtmidi-devel > 0.1-2
BuildRequires:  fftw3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  libuv-devel
BuildRequires:  qwt-qt5-devel
Requires:       qt5-qtbase
Requires:       qt5-qtmultimedia
Requires:       qt5-qtmidi
Requires:       fftw3
Requires:       alsa-lib
Requires:       libuv
Requires:       qwt-qt5

%description
This is a program for tuning your piano. It uses the latest in mathematical
theories to calculate the optimal tuning based on the unique interference
of an individual instrument.

%prep
# standard setup, but rename the dir in the archive, because it contains its commit hash!
tar xaf "%{SOURCE0}"
if [ $? -ne 0 ]; then
  exit $?
fi
tar xaf "%{SOURCE101}"

# remove commit number and move files to build dir
mv "%{PROJECT}-%{BRANCH}-"* "%{PROJECT}-%{BRANCH}"
rmdir "%{PROJECT}-%{BRANCH}/thirdparty/tp3log"
mv "tp3log-%{tp3log_ref}-"* "%{PROJECT}-%{BRANCH}/thirdparty/tp3log"
tar caf "%{SOURCE0}" "%{PROJECT}-%{BRANCH}"
%autosetup -n "%{PROJECT}-%{BRANCH}"

%build
%{qmake_qt5} -r \
	"EPT_INSTALL_BIN_RDIR=%{_bindir}" \
   	"EPT_INSTALL_DATA_RDIR=%{_datadir}" \
    "EPT_INSTALL_LIB_RDIR=%{_libdir}"

make %{?_smp_mflags}


%install
# install files declared in qmake
make INSTALL_ROOT=%{buildroot} install

# install desktop file
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
    --delete-original                          \
    --dir %{buildroot}%{_datadir}/applications \
    "%{SOURCE1}"

# remove unused library files
%{__rm} %{buildroot}%{_libdir}/%{name}/libcore.so

%files
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/mimetypes
%dir %{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/128x128/mimetypes/application-ept.png
%{_datadir}/mime/packages/%{name}-mime.xml
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/algorithms
%{_libdir}/%{name}/lib*
%{_libdir}/%{name}/algorithms/*.so


%changelog
* Thu Jun 13 2019 Greg Hellings <greg.hellings@gmail.com> - 1.2.0-3.20190107gitee7857ac
- Bump build for Qt 5.12

* Mon Jan 07 2019 Greg Hellings <greg.hellings@gmail.com> - 1.2.0-2.20190107gitee7857ac
- Changed to building from git
- Set minimum version for qtmidi

* Tue Mar 13 2018 Greg Hellings <greg.hellings@gmail.com> - 1.2.0-1
- Modified from upstream multi-build version to latest Fedora

* Fri Nov 11 2016 Christoph Wick <info@entropy-tuner.org> - 1.1.7-0
- Updates

* Fri Jun 12 2015 Christoph Wick <info@entropy-tuner.org> - 1.0.4-0
- Initial package.
