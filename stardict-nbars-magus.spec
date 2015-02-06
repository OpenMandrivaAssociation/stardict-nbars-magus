%define	dict_name	magus
%define version		2.4.2
%define release		2

Name:			stardict-nbars-%dict_name
Version:		2.4.2
Release:		%mkrel %{release}
Summary:		New Big English-Russian Dictionary
License:		GPLv2+
URL:			http://xdxf.revdanica.com/down/index.php
Group:			Text tools
Source0:		%{dict_name}.dict.dz
Source1:		%{dict_name}.idx
Source2:		%{dict_name}.ifo
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildArch:		noarch
Requires:		stardict

%description
New Comprehensive English-Russian Dictionary under the editorship
of academician Y.D.Apresyan and professor E.M.Mednikova; Transmagus by
Delta Lingotronic Inc.; http://www.callamer.com/~dlingo; ver. 1.2 for
Unix; in stardict format

%install
rm -rf %{buildroot}
install -p -m644 -D %SOURCE0 %{buildroot}%{_datadir}/stardict/dic/%dict_name.dict.dz
install -p -m644 -D %SOURCE1 %{buildroot}%{_datadir}/stardict/dic/%dict_name.idx
install -p -m644 -D %SOURCE2 %{buildroot}%{_datadir}/stardict/dic/%dict_name.ifo
 	
%clean
rm -rf %{buildroot}
	
%files
%{_datadir}/stardict/dic/%{dict_name}*


%changelog
* Sat Jul 23 2011 Yuri Myasoedov <omerta13@mandriva.org> 2.4.2-1mdv2012.0
+ Revision: 691227
- Initial package import

