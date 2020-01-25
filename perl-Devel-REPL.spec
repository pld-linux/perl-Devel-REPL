#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	REPL
Summary:	Devel::REPL - a modern perl interactive shell
Name:		perl-Devel-REPL
Version:	1.003012
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bff993f2799b2e2cfbc89fbb74607106
URL:		http://search.cpan.org/dist/Devel-REPL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-App-Nopaste
BuildRequires:	perl-B-Keywords
BuildRequires:	perl-Data-Dump-Streamer
BuildRequires:	perl-Data-Dumper-Concise
BuildRequires:	perl-File-HomeDir
BuildRequires:	perl-File-Next
BuildRequires:	perl-Lexical-Persistence
BuildRequires:	perl-Module-Refresh
BuildRequires:	perl-Moose >= 0.74
BuildRequires:	perl-MooseX-AttributeHelpers >= 0.16
BuildRequires:	perl-MooseX-Getopt >= 0.18
BuildRequires:	perl-MooseX-Object-Pluggable >= 0.0009
BuildRequires:	perl-PPI
BuildRequires:	perl-Sys-SigAction
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-namespace-clean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an interactive shell for Perl, commonly known as a REPL -
Read, Evaluate, Print, Loop. The shell provides for rapid development
or testing of code without the need to create a temporary source code
file.

Through a plugin system, many features are available on demand. You
can also tailor the environment through the use of profiles and run
control files, for example to pre-load certain Perl modules when
working on a particular project.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/re.pl
%{perl_vendorlib}/Devel/*.pm
%{perl_vendorlib}/Devel/REPL
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
