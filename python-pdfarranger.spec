%global srcname pdfarranger

Name:           python-%{srcname}
Version:        1.2.1
Release:        2%{?dist}
Summary:        PDF file merging, rearranging, and splitting

License:        GPLv3
URL:            https://github.com/jeromerobert/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  intltool

Requires:       python3-PyPDF2

# These seem to be included in the default desktop install
Requires:       poppler-glib
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-cairo

%description
pdfarranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for python-pyPdf.
pdfarranger is a fork of Konstantinos Poulios's pdfshuffler.


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pdfarranger is a small python-gtk application, which helps the user to merge 
or split pdf documents and rotate, crop and rearrange their pages using an 
interactive and intuitive graphical interface. It is a frontend for python-pyPdf.
pdfarranger is a fork of Konstantinos Poulios's pdfshuffler.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Check fails with "(setup.py:18929): Gtk-WARNING **: 16:47:47.597: cannot open display"
# Disabling for now
#%check
#%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_mandir}/man*/*.*
%{_datadir}/appdata/%{srcname}.appdata.xml
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/%{srcname}/%{srcname}.ui
%{_bindir}/pdfarranger

%changelog
* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1-2
- Add missing requires

* Sat May 18 2019 David Auer <dreua@posteo.de> - 1.2.1
- Packaging pdfarranger based on pdfshuffler's spec file and https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_python_spec_file


