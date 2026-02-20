%define		packname	RBGL

Summary:	An interface to the BOOST graph library
Name:		R-%{packname}
Version:	1.38.0
Release:	2
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	f7d8dc8c3bede64e8d41d25b951f304e
URL:		http://bioconductor.org/packages/release/bioc/html/RBGL.html
BuildRequires:	R
BuildRequires:	R-graph
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-graph
Suggests:	R-cran-XML
Suggests:	R-Rgraphviz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fairly extensive and comprehensive interface to the graph algorithms
contained in the BOOST library.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/%{packname}.so
%{_libdir}/R/library/%{packname}/XML
%{_libdir}/R/library/%{packname}/boostExamples
%{_libdir}/R/library/%{packname}/demos
%{_libdir}/R/library/%{packname}/dot
%{_libdir}/R/library/%{packname}/dtd
%{_libdir}/R/library/%{packname}/fdep.ps
