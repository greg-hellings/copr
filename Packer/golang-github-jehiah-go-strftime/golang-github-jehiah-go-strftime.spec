# Generated by go2rpm
%bcond_without check

%global gitrev 1d33003b386959af197ba96475f198c114627b5e

# https://github.com/mitchellh/cli
%global goipath         github.com/jehiah/go-strftime
Version:                0^20121006git1d3300

%gometa

%global common_description %{expand:
Go implementation of strftime}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of strftime

# Upstream license specification: MPL-2.0
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{gitrev}.tar.gz

%description
%{common_description}

%gopkg

%prep
tar xaf %{SOURCE0}
mv go-strftime-%{gitrev} go-strftime-%{version}
tar caf %{SOURCE0} go-strftime-%{version}
rm -r go-strftime-%{version}
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Oct 6 2021 Greg Hellings <greg.hellings@gmail.com> - 0^202101006git1d3300-1
- First attempt to package
