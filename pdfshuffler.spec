Name:           pdfshuffler
Version:        0.6.0
Release:        11%{?dist}
Summary:        PDF file merging, rearranging, and splitting

License:        GPLv2+
URL:            http://sourceforge.net/projects/pdfshuffler/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
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
%setup -q

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root %{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/pdfshuffler/feature-requests/34/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">pdfshuffler.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      PDF-Shuffler is a small application, which helps the user to merge or split pdf
      documents and rotate, crop and rearrange their pages using an interactive and
      intuitive graphical interface.
      It is a frontend for python-pyPdf.
    </p>
    <!-- FIXME: Probably needs another paragraph or two -->
  </description>
  <url type="homepage">http://pdfshuffler.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/pdfshuffler/screenshots/181783.jpg/</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{python2_sitelib}/%{name}*.egg-info
%{python2_sitelib}/%{name}/

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.6.0-6
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-4
- Update macros

* Thu Aug 22 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-3
- Patch removed
- Rebuilt

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

