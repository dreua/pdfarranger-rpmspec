%global srcname pdfarranger

Name:           python-%{srcname}
Version:        1.2.1
Release:        1%{?dist}
Summary:        PDF file merging, rearranging, and splitting

License:        GPLv3
URL:            https://github.com/jeromerobert/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

#TODO
BuildRequires:  python3-devel
#BuildRequires:  python2-setuptools
#BuildRequires:  desktop-file-utils
#BuildRequires:  gettext

#TODO
#Requires:       pygtk2
#Requires:       python2-PyPDF2
#Requires:       pypoppler

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

%check
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/pdfarranger

%changelog
* Sa May 18 David Auer <dreua@posteo.de> - 1.2.1
- Packaging pdfarranger based on pdfshuffler's spec file and https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_python_spec_file

