%global srcname pdfarranger
%global python3_wheelname %{srcname}-%{version}-py3-none-any.whl

Name:           %{srcname}
Version:        1.2.1
Release:        6%{?dist}
Summary:        PDF file merging, rearranging, and splitting

License:        GPLv3
URL:            https://github.com/jeromerobert/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  intltool
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

# For checks only
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       python3-PyPDF2

# These seem to be included in the default desktop install
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-cairo

%{?python_provide:%python_provide python3-%{srcname}}

# For copr only, to upgrade pyhton(3)-pdfarranger to pdfarranger
Provides: python3-pdfarranger = %{version}-%{release}
Obsoletes: python3-pdfarranger < 1.2.1-6

%description
pdfarranger is a small Python GTK application, which helps the user to merge 
or split PDF documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a front end for 
python-PyPDF2.
pdfarranger is a fork of Konstantinos Poulios's PDF-Shuffler.

%prep
%autosetup -n %{srcname}-%{version}

# Remove wrong and unneccessary shebang until https://github.com/jeromerobert/pdfarranger/pull/80 is released
sed -i '/#\!/d' pdfarranger/__main__.py

%build
%py3_build_wheel

%install
%py3_install_wheel %{python3_wheelname}
%find_lang %{srcname}

# Fix metainfo location until https://github.com/jeromerobert/pdfarranger/pull/79 is released
mv %{buildroot}%{_datadir}/appdata %{buildroot}%{_metainfodir}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{srcname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{srcname}.lang
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{_mandir}/man*/*.*
%{_datadir}/icons/hicolor/*/apps/%{srcname}.*
%{_metainfodir}/%{srcname}.appdata.xml
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/%{srcname}/%{srcname}.ui
%{_bindir}/pdfarranger

%changelog
* Mon May 20 2019 David Auer <dreua@posteo.de> - 1.2.1-6
- Name changed from python-pdfarranger to pdfarranger
- Remove shebang in __main__.py
- Copr only: Add Provides and Obsoletes for old name

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-5
- Fix rpmlint errors and warnings

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-4
- Buiding with wheel to get lang and icons right

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-3
- Move Requires to the right location

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-2
- Add missing requires

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1
- Packaging pdfarranger based on pdfshuffler's spec file and https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_python_spec_file


