# Created by pyp2rpm-3.3.2
%global pypi_name pyOpenSSL

Name:           python-%{pypi_name}
Version:        17.5.0
Release:        1%{?dist}
Summary:        Python wrapper module around the OpenSSL library

License:        Apache License, Version 2.0
URL:            https://pyopenssl.org/
Source0:        %{pypi_name}-%{version}-py2.py3-none-any.whl
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

%description
 pyOpenSSL -- A Python wrapper around the OpenSSL library High-level wrapper
around a subset of the OpenSSL library. Includes* SSL.Connection objects,
wrapping the methods of Python's portable sockets * Callbacks written in Python
* Extensive error-handling mechanism, mirroring OpenSSL's error codes... and
much more.You can find more information in the documentation_. Development
takes place...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2dist(cryptography) >= 2.1.4
Requires:       python2dist(six) >= 1.5.2
Requires:       python2dist(flaky)
Requires:       python2dist(pretend)
Requires:       python2dist(pytest) < 3.3.0
Requires:       python2dist(pytest) >= 3.0.1
Requires:       python2dist(sphinx-rtd-theme)
Requires:       python2dist(sphinx)
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
 pyOpenSSL -- A Python wrapper around the OpenSSL library High-level wrapper
around a subset of the OpenSSL library. Includes* SSL.Connection objects,
wrapping the methods of Python's portable sockets * Callbacks written in Python
* Extensive error-handling mechanism, mirroring OpenSSL's error codes... and
much more.You can find more information in the documentation_. Development
takes place...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc DESCRIPTION.rst
%{python2_sitelib}/OpenSSL.py*
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 08 2018 greg.hellings@gmail.com - 17.5.0-1
- Initial package.
