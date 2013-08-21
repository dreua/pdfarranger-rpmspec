Name:           pdfshuffler
Version:        0.6.0
Release:        2%{?dist}
Summary:        PDF file merging, rearranging, and splitting

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://sourceforge.net/projects/pdfshuffler/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         pdfshuffler-ui-location.patch
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
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
%setup -q -n pdfshuffler
%patch0 -b .uilocation

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%{python_sitelib}/%{name}*.egg-info
%{python_sitelib}/%{name}/

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Spec file cleaned
- Switch to release package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.4.20120302svn64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.3.20120302svn64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Fabian Affolter <mail@fabian-affolter.ch>  - 0.6.0-0.2.20120302svn64
- Minor changes

* Thu Jan 26 2012 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.6.0-0.1.20120126svn64
- Update to current SVN snapshot

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Apr 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Updated to new upstream version 0.5.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar 15 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-1
- Updated to new upstream version 0.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Updated to new upstream version 0.4.2

* Sat Apr 25 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-2
- Removed patch0
- Removed permission changing of doc files
- Removed ghostscript and added pypoppler as a requirement

* Sat Apr 25 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Updated to new upstream version 0.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-3
- Fixed requirements

* Sat Jan 31 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-2
- Fixed typo in summary and .desktop file

* Sat Jan 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Initial package for Fedora

