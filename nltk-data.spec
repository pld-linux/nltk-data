#
# wget http://nltk.googlecode.com/svn/trunk/nltk_data/index.xml
#
# grep "<package " index.xml | \
#  sed 's|.* checksum="\([^"]*\)".* url="\([^"]*\)".*|SourceXX:\t\2\nSourceXX-md5:\t\1|g'
#
Summary:	Natural Language Toolkit Database
Summary(pl.UTF-8):	Baza danych dla pakietu Natural Language Toolkit
Name:		nltk-data
Version:	2.0
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://nltk.googlecode.com/svn/trunk/nltk_data/index.xml
# Source0-md5:	9faafe9f56b2a88db4f8e0cc933205fc
Source1:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/chunkers/maxent_ne_chunker.zip
# Source1-md5:	e211969f0369b83c23f3e7f20250b338
Source2:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/abc.zip
# Source2-md5:	ffb36b67ff24cbf7daaf171c897eb904
Source3:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/alpino.zip
# Source3-md5:	63254e4e055781a1783311d8569ac0a3
Source4:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/biocreative_ppi.zip
# Source4-md5:	d3be36b53ab201372f1cd63ffc75e9a9
Source5:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/brown.zip
# Source5-md5:	3db6ae853b87318c9ae0da5aed0adc28
Source6:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/brown_tei.zip
# Source6-md5:	3c7fe43ebf0a4c7ad3ebb63dab027e09
Source7:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/cess_cat.zip
# Source7-md5:	e91ac59ec6e98e3b297e2d2eab83084d
Source8:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/cess_esp.zip
# Source8-md5:	684432d4f6384b8f0bd19fee5dc15925
Source9:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/chat80.zip
# Source9-md5:	6832873fe92996846ac5bb21c5d84eb8
Source10:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/city_database.zip
# Source10-md5:	29cbf1aa02ad8abc72dd955fe74f882c
Source11:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/cmudict.zip
# Source11-md5:	58f743ff818b983b89ef9302b509fc41
Source12:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/comtrans.zip
# Source12-md5:	8e1e34e2f052d8188fd877b2c821b42d
Source13:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/conll2000.zip
# Source13-md5:	9529b285edd5fe47271da69df1052301
Source14:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/conll2002.zip
# Source14-md5:	67bb4ca75fa81544d42a159524726e78
Source15:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/conll2007.zip
# Source15-md5:	b9015928e35c41f0695525289df5208f
Source16:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/dependency_treebank.zip
# Source16-md5:	631e959acaa42eea718daf04c5cdfa76
Source17:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/europarl_raw.zip
# Source17-md5:	7621d5675990b1decc012c823716ee76
Source18:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/floresta.zip
# Source18-md5:	de5f1df09949f080e0f616f0bc55967d
Source19:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/gazetteers.zip
# Source19-md5:	1dd15c714a2be985c482a13d90e9caa4
Source20:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/genesis.zip
# Source20-md5:	2a76432753c01fe179684e0ae3a4d023
Source21:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/gutenberg.zip
# Source21-md5:	48c9c8605cd70b0230687557ee543633
Source22:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/ieer.zip
# Source22-md5:	34157f569624bc8d642ef8da5722b14a
Source23:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/inaugural.zip
# Source23-md5:	54af23bfe81ee22b2d0cc0e28c8399e1
Source24:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/indian.zip
# Source24-md5:	abf96484a742811f4109e19a3a25fe06
Source25:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/jeita.zip
# Source25-md5:	96e30423d6887fad17fc44f2f30d920d
Source26:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/kimmo.zip
# Source26-md5:	68a8716e0233ad9c0ed0947952e4eb3e
Source27:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/knbc.zip
# Source27-md5:	992f8a3647f333e28a9958eba4bd67c7
Source28:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/langid.zip
# Source28-md5:	77b9b2faf5e08b1986d74f29bb2b3fc1
Source29:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/mac_morpho.zip
# Source29-md5:	cf216ae5b37cca24866909f8594c5395
Source30:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/machado.zip
# Source30-md5:	d186f7d6715479a8bec48b8b8030858e
Source31:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/movie_reviews.zip
# Source31-md5:	155de2b77c6834dd8eea7cbe88e93acb
Source32:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/names.zip
# Source32-md5:	93844d7c995ad28f40528c08a3430175
Source33:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/nombank.1.0.zip
# Source33-md5:	1d0b08de34eba1f013ecb8169d2e3bec
Source34:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/nps_chat.zip
# Source34-md5:	72d1b905ba2be48d711690b012856c79
Source35:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/paradigms.zip
# Source35-md5:	745ee9036c5ca3226be24c97515f5707
Source36:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/pe08.zip
# Source36-md5:	e72135042dc48772acad309a6adbb6f0
Source37:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/pil.zip
# Source37-md5:	d07b2ca7b5b351a24f4db8ae8fbc9e98
Source38:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/pl196x.zip
# Source38-md5:	bcbdcf0fc2420fac238ca17dc7bfe423
Source39:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/ppattach.zip
# Source39-md5:	cce212b7ace8e64722ba2f41f802a5d0
Source40:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/problem_reports.zip
# Source40-md5:	8781ace4c0a181c5875cdbfc01e895fb
Source41:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/propbank.zip
# Source41-md5:	2397782c6e6f46c9657f85db8a5421f6
Source42:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/qc.zip
# Source42-md5:	afd4145ac31cb8d7db715974b9b8b57a
Source43:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/reuters.zip
# Source43-md5:	c2acb24d5cccf8035e0fe8d29f440a68
Source44:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/rte.zip
# Source44-md5:	ca21663daa326a3bb53001c3d82e62d6
Source45:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/semcor.zip
# Source45-md5:	46c095f0ab7090132567f87252af724f
Source46:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/senseval.zip
# Source46-md5:	bfc6a33c62ddc2ec24b02701a2f364ff
Source47:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/shakespeare.zip
# Source47-md5:	2332b32a7d83d657092ba4667c2c84c3
Source48:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/sinica_treebank.zip
# Source48-md5:	3e314e26c852c5796488244ffef2ac91
Source49:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/smultron.zip
# Source49-md5:	8743ff232d76aaf2ff8a10523503a659
Source50:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/state_union.zip
# Source50-md5:	044f2d20c592b17a26ac0102111833c9
Source51:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/stopwords.zip
# Source51-md5:	0669147c05593d0be78501b159561307
Source52:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/swadesh.zip
# Source52-md5:	6612ccb71f327e85780dc7813dee40f6
Source53:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/switchboard.zip
# Source53-md5:	878df010a9f2c2d0a6546a8365f10595
Source54:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/timit.zip
# Source54-md5:	34c047c4749a811287f2c652104d7849
Source55:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/toolbox.zip
# Source55-md5:	26657c1b8b5f5afdc3d5d754393a9216
Source56:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/treebank.zip
# Source56-md5:	fce815010375b9911c68b1e74d8d8a05
Source57:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/udhr.zip
# Source57-md5:	745b3a90feb25c95fc805ebbd1ef5258
Source58:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/unicode_samples.zip
# Source58-md5:	d46699450dd2287f5c115d8c1a0819f1
Source59:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/verbnet.zip
# Source59-md5:	427dac60e4a94ae910248ccd9986a22a
Source60:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/webtext.zip
# Source60-md5:	6c7680030aae5c997b1370f832545c6a
Source61:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/wordnet.zip
# Source61-md5:	da4ca27db8350b38729dc89de4d5a4e1
Source62:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/wordnet_ic.zip
# Source62-md5:	25f0185b31693fa11ea898e4feda528c
Source63:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/words.zip
# Source63-md5:	dc6d4f233a924ddcc40ac3616953bb59
Source64:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/corpora/ycoe.zip
# Source64-md5:	6582cd98ca26c35d9c4eaaa4350ce8f3
Source65:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/grammars/basque_grammars.zip
# Source65-md5:	0e3518cb2aeb2600cb2841df7f035606
Source66:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/grammars/book_grammars.zip
# Source66-md5:	8d1219206f2bbb209ec302cbe18e6a79
Source67:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/grammars/large_grammars.zip
# Source67-md5:	135aa813bd721d59ae595d9d7f115dc8
Source68:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/grammars/sample_grammars.zip
# Source68-md5:	200caa0cbd55f731ae6d592c165c319c
Source69:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/grammars/spanish_grammars.zip
# Source69-md5:	12f66b8e22beadd6ed202e95453465af
Source70:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/help/tagsets.zip
# Source70-md5:	d08ffaa327bed3603d0967509df4ed0d
Source71:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/stemmers/rslp.zip
# Source71-md5:	648798996224694251834699fa6e55f7
Source72:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/taggers/hmm_treebank_pos_tagger.zip
# Source72-md5:	b879eaf39f3dbb97c551e9df5db93ec9
Source73:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/taggers/maxent_treebank_pos_tagger.zip
# Source73-md5:	eb10d0766b03c83123a6d2b297ba9da2
Source74:	http://nltk.googlecode.com/svn/trunk/nltk_data/packages/tokenizers/punkt.zip
# Source74-md5:	7c5bee480312a91c135123c7c3db88da
URL:		http://www.nltk.org/data
BuildRequires:	unzip
Requires:	python-nltk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Natural Langauge Toolkit (NLTK-Lite) database.

%description -l pl.UTF-8
Baza danych dla pakietu Natural Language Toolkit (NLTK-Lite).

%prep
%setup -c -T

PKGS=`grep "<package " %{SOURCE0} | \
  sed 's|.* subdir="\([^"]*\)".*url="\([^"]*\)".*|\1;\2|g'`

for p in $PKGS ; do
	s=`echo $p | cut -f 1 -d \;`
	u=`echo $p | cut -f 2 -d \;`
	f=`basename $u`
	install -d $s
	install $RPM_SOURCE_DIR/$f $s
	unzip $RPM_SOURCE_DIR/$f -d $s
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/nltk_data

cp -a * $RPM_BUILD_ROOT%{_datadir}/nltk_data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/nltk_data
