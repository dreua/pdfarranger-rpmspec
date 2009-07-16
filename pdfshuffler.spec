%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pdfshuffler
Version:        0.4.2
Release:        1%{?dist}
Summary:        PDF file merging, rearranging, and splitting

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://sourceforge.net/projects/pdfshuffler/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)     
BuildArch:      noarch

BuildRequires:  python
BuildRequires:  python-setuptools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires:       pygtk2
Requires:       pyPdf
Requires:       pypoppler

%description
PDF-Shuffler is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%{python_sitelib}/%{name}*.egg-info


%changelog
* Fri Jul 17 2009 Fabian Affolter <fabian@bernewireless.net> - 0.4.2-1
- Removed patch0
- Removed permission changing of doc files
- Removed ghostscript and added pypoppler as a requirement
- Updated to new upstream version 0.4.2

* Sat Apr 25 2009 Fabian Affolter <fabian@bernewireless.net> - 0.4-1
- Updated to new upstream version 0.4

* Sat Feb 14 2009 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-3
- Fixed requirements

* Sat Jan 31 2009 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-2
- Fixed typo in summary and .desktop file

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-1
- Initial package for Fedora

