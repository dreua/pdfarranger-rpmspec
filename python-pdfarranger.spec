%global srcname pdfarranger
%global python3_wheelname %{srcname}-%{version}-py3-none-any.whl

Name:           python-%{srcname}
Version:        1.2.1
Release:        4%{?dist}
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

%description
pdfarranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for python-pyPdf.
pdfarranger is a fork of Konstantinos Poulios's pdfshuffler.


%package -n python3-%{srcname}
Summary:        %{summary}

Requires:       python3-PyPDF2

# These seem to be included in the default desktop install
Requires:       poppler-glib
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-cairo

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
pdfarranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for python-pyPdf.
pdfarranger is a fork of Konstantinos Poulios's pdfshuffler.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build_wheel

%install
%py3_install_wheel %{python3_wheelname}
%find_lang %{srcname}

# Fix metainfo location until https://github.com/jeromerobert/pdfarranger/pull/79 is merged
mv %{buildroot}%{_datadir}/appdata %{buildroot}%{_metainfodir}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{srcname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -n python3-%{srcname} -f %{srcname}.lang
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
* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-4
- Buiding with wheel to get lang and icons right

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-3
- Move Requires to the right location

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-2
- Add missing requires

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1
- Packaging pdfarranger based on pdfshuffler's spec file and https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_python_spec_file


