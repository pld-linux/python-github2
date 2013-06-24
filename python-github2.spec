%define		module	github2
Summary:	Github API v2 library for Python
Name:		python-%{module}
Version:	0.6.2
Release:	2
License:	New BSD License
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/github2/%{module}-%{version}.tar.gz
# Source0-md5:	1341655d6ca823c1e0cb7eacec68f99f
URL:		http://github.com/ask/python-github2
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	ca-certificates
Requires:	python-httplib2
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an experimental Python library implementing all of the
features available in version 2 of the Github API.

%prep
%setup -q -n %{module}-%{version}

# fix something that doesn't make sense (there is no dateutil-2.1)
%{__sed} -i -e 's/, >= 2.1//' github2.egg-info/requires.txt setup.py

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
%attr(755,root,root) %{_bindir}/github_search_repos
%dir %{py_sitescriptdir}/github2
%{py_sitescriptdir}/%{module}/*.py[co]
%if 0
%{py_sitescriptdir}/%{module}/DigiCert_High_Assurance_EV_Root_CA.crt
%dir %{py_sitescriptdir}/%{module}/bin
%{py_sitescriptdir}/%{module}/bin/__init__.pyc
%{py_sitescriptdir}/%{module}/bin/__init__.pyo
%{py_sitescriptdir}/%{module}/bin/manage_collaborators.pyc
%{py_sitescriptdir}/%{module}/bin/manage_collaborators.pyo
%{py_sitescriptdir}/%{module}/bin/search_repos.pyc
%{py_sitescriptdir}/%{module}/bin/search_repos.pyo
%endif

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/github2-*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}
