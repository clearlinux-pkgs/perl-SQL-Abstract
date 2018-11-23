#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SQL-Abstract
Version  : 1.86
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/SQL-Abstract-1.86.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/SQL-Abstract-1.86.tar.gz
Summary  : 'Generate SQL from Perl data structures'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone::Choose)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Hash::Merge)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Warn)

%description
NAME
SQL::Abstract - Generate SQL from Perl data structures
SYNOPSIS
use SQL::Abstract;

%package dev
Summary: dev components for the perl-SQL-Abstract package.
Group: Development
Provides: perl-SQL-Abstract-devel = %{version}-%{release}

%description dev
dev components for the perl-SQL-Abstract package.


%prep
%setup -q -n SQL-Abstract-1.86

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/DBIx/Class/Storage/Debug/PrettyPrint.pm
/usr/lib/perl5/vendor_perl/5.28.0/SQL/Abstract.pm
/usr/lib/perl5/vendor_perl/5.28.0/SQL/Abstract/Test.pm
/usr/lib/perl5/vendor_perl/5.28.0/SQL/Abstract/Tree.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Class::Storage::Debug::PrettyPrint.3
/usr/share/man/man3/SQL::Abstract.3
/usr/share/man/man3/SQL::Abstract::Test.3
/usr/share/man/man3/SQL::Abstract::Tree.3
