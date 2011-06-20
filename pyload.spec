Summary:	Download tool for One-Click-Hoster written in python
Name:		pyload
Version:	0.4.6
Release:	0.1
License:	GPL v3+
Group:		Applications
Source0:	%{name}-src-v%{version}.zip
# Source0-md5:	5f03a25d772db32eb5c550bba47294c1
URL:		https://bitbucket.org/spoob/pyload/
BuildRequires:	unzip
Requires:	js
Requires:	python-PyQt4
Requires:	python-flup
Requires:	python-pynotify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyLoad is a free and open source downloader for 1-click-hosting sites
like rapidshare.com or uploaded.to. It supports link decrypter as well
as all important container formarts. pyLoad is written entirely in
Python and currently under heavy development.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s %{_datadir}/%{name}/pyLoadCore.py $RPM_BUILD_ROOT%{_bindir}/pyLoadCore
ln -s %{_datadir}/%{name}/pyLoadCli.py $RPM_BUILD_ROOT%{_bindir}/pyLoadCli
ln -s %{_datadir}/%{name}/pyLoadGui.py $RPM_BUILD_ROOT%{_bindir}/pyLoadGui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pyLoadCli
%attr(755,root,root) %{_bindir}/pyLoadCore
%attr(755,root,root) %{_bindir}/pyLoadGui
%dir %{_datadir}/%{name}
%{_datadir}/pyload/systemCheck.py
# TODO: make localedir verbose
%{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/module
%{_datadir}/%{name}/module/*.py
%{_datadir}/%{name}/module/common
%{_datadir}/%{name}/module/cli
%{_datadir}/%{name}/module/config
%{_datadir}/%{name}/module/database
%{_datadir}/%{name}/module/gui
%{_datadir}/%{name}/module/lib
%{_datadir}/%{name}/module/network
%{_datadir}/%{name}/module/plugins
%{_datadir}/%{name}/module/remote
%{_datadir}/%{name}/module/web
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/*.png
%{_datadir}/%{name}/icons/*.ico

# must be executable to run
%attr(755,root,root) %{_datadir}/%{name}/pyLoadCli.py
%attr(755,root,root) %{_datadir}/%{name}/pyLoadCore.py
%attr(755,root,root) %{_datadir}/%{name}/pyLoadGui.py
