%define 	module	github2
Summary:	Github API v2 library for Python
Name:		python-%{module}
Version:	0.2.0
Release:	2
License:	New BSD License
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/github2/%{module}-%{version}.tar.gz
# Source0-md5:	0b4e1d454b03450e818c51f4fb6fcf2c
URL:		http://github.com/ask/python-github2
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an experimental python library implementing all of the
features available in version 2 of the Github API.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# tests should be ran not packaged
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.rst LICENSE
%attr(755,root,root) %{_bindir}/github_manage_collaborators
%dir %{py_sitescriptdir}/github2
%{py_sitescriptdir}/github2/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/github2-*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
