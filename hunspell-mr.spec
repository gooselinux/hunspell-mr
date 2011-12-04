Name: hunspell-mr
Summary: Marathi hunspell dictionaries
Version: 20060920 
Release: 6.1%{?dist}
Source: http://ftp.freepark.org/OpenOffice.org/contrib/dictionaries/mr_IN.zip
Patch0: hunspell-mr-get-rid-of-broken-line.patch
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Marathi hunspell dictionaries.

%prep
%setup -q -c -n mr-IN
%patch0 -p1

%build
#nothing to do here

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mr_IN.dic mr_IN.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_mr_IN.txt LICENCE
%{_datadir}/myspell/*

%changelog
* Thu Feb 18 2010 Parag <pnemade AT redhat.com> - 20060920-6.1
- Resolves: rh#566390:- Fix disttag from previous commit.

* Thu Feb 18 2010 Parag <pnemade AT redhat.com> - 20060920-6
- Resolves: rh#566390:- Improvements to get rid of the broken line

* Mon Jan 11 2010 Parag <pnemade AT redhat.com> - 20060920-5
- Resolves: rh#554302: Change Source URL to new mirror.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20060920-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Caolán McNamara <caolanm@redhat.com> - 20060920-3
- bring wordlist encoding issue fix from F-11 into devel

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060920-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20060920-1
- Initial Fedora release
