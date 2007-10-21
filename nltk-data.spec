Summary:	Natural Language Toolkit Database
Summary(pl.UTF-8):	Baza danych dla pakietu Natural Language Toolkit
Name:		nltk-data
Version:	0.9
Release:	0.1
License:	BSD
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/nltk/%{name}-%{version}.zip
# Source0-md5:	b2dffb82175857dce950fd1f01896c9d
URL:		http://nltk.sourceforge.net/
BuildRequires:	unzip
Requires:	python-nltk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Langauge Toolkit (NLTK-Lite) database.

%description -l pl.UTF-8
Baza danych dla pakietu Natural Language Toolkit (NLTK-Lite).

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/nltk

cp -a * $RPM_BUILD_ROOT%{_datadir}/nltk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/nltk
