%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pdfshuffler
Version:        0.3.1
Release:        2%{?dist}
Summary:        PDF file merging, rearranging, and splitting

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://sourceforge.net/projects/pdfshuffler/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-desktop.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)     
BuildArch:      noarch

BuildRequires:  python
BuildRequires:  pygtk2-devel
BuildRequires:  pyPdf
BuildRequires:  ghostscript-devel
BuildRequires:  python-setuptools-devel

BuildRequires:  desktop-file-utils
BuildRequires:  gettext


%description
PDF-Shuffler is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.


%prep
%setup -q
chmod -x {AUTHORS,ChangeLog,COPYING,README,TODO,doc/pdfshuffler.1}
%patch0 -p0 -b .desktop


%build
python ./setup.py build


%install
rm -rf %{buildroot}
python ./setup.py install --skip-build --root %{buildroot}
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
* Sat Jan 31 2009 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-2
- Fixed typo in summary and .desktop file

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-1
- Initial package for Fedora

