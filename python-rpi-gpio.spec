%global srcname RPi.GPIO
%global sum A class to control the GPIO on a Raspberry Pi

%global __provides_exclude_from ^(%{python2_sitearch}/.*\\.so)$
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Name:           python-rpi-gpio
Version:        0.6.2
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
Source0:        http://sourceforge.net/projects/raspberry-gpio-python/files/RPi.GPIO-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-setuptools


%description
Python library for GPIO access on a Raspberry Pi.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Python library for GPIO access on a Raspberry Pi.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Python library for GPIO access on a Raspberry Pi.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%doc README.txt
%license LICENCE.txt
%{python2_sitearch}/RPi*

%files -n python3-%{srcname}
%doc README.txt
%license LICENCE.txt
%{python3_sitearch}/RPi*

%changelog
* Mon Mar 14 2016 Vaughan <vaughan at agrez dot net> - 0.6.2-1
- New release

* Sun Feb 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Add py3 support
- Update to new upstream version 0.6.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.11-1
- Update to 0.5.11

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 30 2012 Kushal Das <kushal@fedoraproject.org> 0.3.1a-1
- Intial package
