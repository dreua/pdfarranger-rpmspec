Name:           pdfarranger
Version:        1.5.1
Release:        1%{?dist}
Summary:        PDF file merging, rearranging, and splitting
Group:          Publishing
License:        GPLv3
URL:            https://github.com/jeromerobert/pdfarranger
Source0:        https://github.com/jeromerobert/pdfarranger/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  python3-distutils-extra
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-pikepdf
Requires:       typelib-1_0-Poppler-0_18

%global app_id com.github.jeromerobert.pdfarranger

%description
PDFArranger is a small python-gtk application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

The tool, which is a graphical front-end for PyPDF2, is a fork of
PDF-Shuffler that aims to "make the project a bit more active".

%prep
%setup -q
%autopatch -p1

%build
%py3_build

%install
python3 setup.py install --root %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/metainfo/%{app_id}.metainfo.xml
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ui
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 20 2020 David Auer <dreua@posteo.de> - 1.5.1-1
- Update to 1.5.1

* Wed Apr 15 2020 David Auer <dreua@posteo.de> - 1.5.0-1
- new version

* Thu Mar 26 2020 David Auer <dreua@posteo.de> - 1.4.2-1
- Update to 1.4.2
- Rebuilt needed for Pyhthon 3.8 update in copr
- Fix requires pikepdf, typelib-1_0-Poppler-0_18

* Mon Dec 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Sun Dec 16 2018 daviddavid <daviddavid> 1.1-1.mga7
+ Revision: 1341749
- initial package pdfarranger

