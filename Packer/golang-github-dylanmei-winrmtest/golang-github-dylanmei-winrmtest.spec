# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/dylanmei/winrmtest
%global goipath         github.com/dylanmei/winrmtest
%global commit          fbc9ae56efb6053a528b6002497191a22cbe0269

%gometa

%global common_description %{expand:
An go-winrm testing package.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        An go-winrm testing package

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/antchfx/xmlquery)
BuildRequires:  golang(github.com/gofrs/uuid)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Oct 06 2021 Gregory Hellings <greg.hellings@gmail.com> - 0-0.1%{?dist}.20211006gitfbc9ae5
- Initial package

