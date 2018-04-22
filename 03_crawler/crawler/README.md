# 크롤링  

### 크롤링 대상
* [법원경매정보](https://www.courtauction.go.kr/)
* [과거데이터](http://100dream.net:8888/)
* [우리경매](http://www.j123.co.kr/)

### 사용 라이브러리  
  * python 3.6
  * Anaconda 5
  * [Scrapy](http://scrapy.org)  

### Conda 가상환경 
~~~
[eduuser@dn01 ~]$ conda list
# packages in environment at /home/eduuser/anaconda3:
#
_license                  1.1                      py36_1  
alabaster                 0.7.9                    py36_0  
anaconda                  4.3.0               np111py36_0  
anaconda-client           1.6.0                    py36_0  
anaconda-navigator        1.4.3                    py36_0  
astroid                   1.4.9                    py36_0  
astropy                   1.3                 np111py36_0  
babel                     2.3.4                    py36_0  
backports                 1.0                      py36_0  
beautifulsoup4            4.5.3                    py36_0  
bitarray                  0.8.1                    py36_0  
blaze                     0.10.1                   py36_0  
bokeh                     0.12.4                   py36_0  
boto                      2.45.0                   py36_0  
bottleneck                1.2.0               np111py36_0  
cairo                     1.14.8                        0  
cffi                      1.9.1                    py36_0  
chardet                   2.3.0                    py36_0  
chest                     0.2.3                    py36_0  
click                     6.7                      py36_0  
cloudpickle               0.2.2                    py36_0  
clyent                    1.2.2                    py36_0  
colorama                  0.3.7                    py36_0  
conda                     4.3.8                    py36_0  
conda-env                 2.6.0                         0  
configobj                 5.0.6                    py36_0  
contextlib2               0.5.4                    py36_0  
cryptography              1.7.1                    py36_0  
curl                      7.52.1                        0  
cycler                    0.10.0                   py36_0  
cython                    0.25.2                   py36_0  
cytoolz                   0.8.2                    py36_0  
dask                      0.13.0                   py36_0  
datashape                 0.5.4                    py36_0  
dbus                      1.10.10                       0  
decorator                 4.0.11                   py36_0  
dill                      0.2.5                    py36_0  
docutils                  0.13.1                   py36_0  
entrypoints               0.2.2                    py36_0  
et_xmlfile                1.0.1                    py36_0  
expat                     2.1.0                         0  
fastcache                 1.0.2                    py36_1  
flask                     0.12                     py36_0  
flask-cors                3.0.2                    py36_0  
fontconfig                2.12.1                        2  
freetype                  2.5.5                         2  
get_terminal_size         1.0.0                    py36_0  
gevent                    1.2.1                    py36_0  
glib                      2.50.2                        1  
greenlet                  0.4.11                   py36_0  
gst-plugins-base          1.8.0                         0  
gstreamer                 1.8.0                         0  
h5py                      2.6.0               np111py36_2  
harfbuzz                  0.9.39                        2  
hdf5                      1.8.17                        1  
heapdict                  1.0.0                    py36_1  
icu                       54.1                          0  
idna                      2.2                      py36_0  
imagesize                 0.7.1                    py36_0  
ipykernel                 4.5.2                    py36_0  
ipython                   5.1.0                    py36_0  
ipython_genutils          0.1.0                    py36_0  
ipywidgets                5.2.2                    py36_1  
isort                     4.2.5                    py36_0  
itsdangerous              0.24                     py36_0  
jbig                      2.1                           0  
jdcal                     1.3                      py36_0  
jedi                      0.9.0                    py36_1  
jinja2                    2.9.4                    py36_0  
jpeg                      9b                            0  
jsonschema                2.5.1                    py36_0  
jupyter                   1.0.0                    py36_3  
jupyter_client            4.4.0                    py36_0  
jupyter_console           5.0.0                    py36_0  
jupyter_core              4.2.1                    py36_0  
lazy-object-proxy         1.2.2                    py36_0  
libffi                    3.2.1                         1  
libgcc                    4.8.5                         2  
libgfortran               3.0.0                         1  
libiconv                  1.14                          0  
libpng                    1.6.27                        0  
libsodium                 1.0.10                        0  
libtiff                   4.0.6                         3  
libxcb                    1.12                          1  
libxml2                   2.9.4                         0  
libxslt                   1.1.29                        0  
llvmlite                  0.15.0                   py36_0  
locket                    0.2.0                    py36_1  
lxml                      3.7.2                    py36_0  
markupsafe                0.23                     py36_2  
matplotlib                2.0.0               np111py36_0  
mistune                   0.7.3                    py36_0  
mkl                       2017.0.1                      0  
mkl-service               1.1.2                    py36_3  
mpmath                    0.19                     py36_1  
multipledispatch          0.4.9                    py36_0  
nbconvert                 4.2.0                    py36_0  
nbformat                  4.2.0                    py36_0  
networkx                  1.11                     py36_0  
nltk                      3.2.2                    py36_0  
nose                      1.3.7                    py36_1  
notebook                  4.3.1                    py36_0  
numba                     0.30.1              np111py36_0  
numexpr                   2.6.1               np111py36_2  
numpy                     1.11.3                   py36_0  
numpydoc                  0.6.0                    py36_0  
odo                       0.5.0                    py36_1  
openpyxl                  2.4.1                    py36_0  
openssl                   1.0.2k                        0  
pandas                    0.19.2              np111py36_1  
partd                     0.3.7                    py36_0  
path.py                   10.0                     py36_0  
pathlib2                  2.2.0                    py36_0  
patsy                     0.4.1                    py36_0  
pcre                      8.39                          1  
pep8                      1.7.0                    py36_0  
pexpect                   4.2.1                    py36_0  
pickleshare               0.7.4                    py36_0  
pillow                    4.0.0                    py36_0  
pip                       9.0.1                    py36_1  
pixman                    0.34.0                        0  
ply                       3.9                      py36_0  
prompt_toolkit            1.0.9                    py36_0  
psutil                    5.0.1                    py36_0  
ptyprocess                0.5.1                    py36_0  
py                        1.4.32                   py36_0  
pyasn1                    0.1.9                    py36_0  
pycosat                   0.6.1                    py36_1  
pycparser                 2.17                     py36_0  
pycrypto                  2.6.1                    py36_4  
pycurl                    7.43.0                   py36_2  
pyflakes                  1.5.0                    py36_0  
pygments                  2.1.3                    py36_0  
pylint                    1.6.4                    py36_1  
pyopenssl                 16.2.0                   py36_0  
pyparsing                 2.1.4                    py36_0  
pyqt                      5.6.0                    py36_2  
pytables                  3.3.0               np111py36_0  
pytest                    3.0.5                    py36_0  
python                    3.6.0                         0  
python-dateutil           2.6.0                    py36_0  
pytz                      2016.10                  py36_0  
pyyaml                    3.12                     py36_0  
pyzmq                     16.0.2                   py36_0  
qt                        5.6.2                         3  
qtawesome                 0.4.3                    py36_0  
qtconsole                 4.2.1                    py36_1  
qtpy                      1.2.1                    py36_0  
readline                  6.2                           2  
redis                     3.2.0                         0  
redis-py                  2.10.5                   py36_0  
requests                  2.12.4                   py36_0  
rope                      0.9.4                    py36_1  
ruamel_yaml               0.11.14                  py36_1  
scikit-image              0.12.3              np111py36_1  
scikit-learn              0.18.1              np111py36_1  
scipy                     0.18.1              np111py36_1  
seaborn                   0.7.1                    py36_0  
setuptools                27.2.0                   py36_0  
simplegeneric             0.8.1                    py36_1  
singledispatch            3.4.0.3                  py36_0  
sip                       4.18                     py36_0  
six                       1.10.0                   py36_0  
snowballstemmer           1.2.1                    py36_0  
sockjs-tornado            1.0.3                    py36_0  
sphinx                    1.5.1                    py36_0  
spyder                    3.1.2                    py36_0  
sqlalchemy                1.1.5                    py36_0  
sqlite                    3.13.0                        0  
statsmodels               0.6.1               np111py36_1  
sympy                     1.0                      py36_0  
terminado                 0.6                      py36_0  
tk                        8.5.18                        0  
toolz                     0.8.2                    py36_0  
tornado                   4.4.2                    py36_0  
traitlets                 4.3.1                    py36_0  
unicodecsv                0.14.1                   py36_0  
wcwidth                   0.1.7                    py36_0  
werkzeug                  0.11.15                  py36_0  
wheel                     0.29.0                   py36_0  
widgetsnbextension        1.2.6                    py36_0  
wrapt                     1.10.8                   py36_0  
xlrd                      1.0.0                    py36_0  
xlsxwriter                0.9.6                    py36_0  
xlwt                      1.2.0                    py36_0  
xz                        5.2.2                         1  
yaml                      0.1.6                         0  
zeromq                    4.1.5                         0  
zlib                      1.2.8                         3  
[eduuser@dn01 ~]$ conda create -n crawlenv
Fetching package metadata .........
Solving package specifications: 
Package plan for installation in environment /home/eduuser/anaconda3/envs/crawlenv:

Proceed ([y]/n)? y

#
# To activate this environment, use:
# > source activate crawlenv
#
# To deactivate this environment, use:
# > source deactivate crawlenv
#

[eduuser@dn01 ~]$ source activate crawlenv
(crawlenv) [eduuser@dn01 ~]$ conda list
# packages in environment at /home/eduuser/anaconda3/envs/crawlenv:
#
(crawlenv) [eduuser@dn01 ~]$ python -V
Python 3.6.0 :: Anaconda 4.3.0 (64-bit)
(crawlenv) [eduuser@dn01 ~]$ 
(crawlenv) [eduuser@dn01 ~]$ conda install scrapy
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/eduuser/anaconda3/envs/crawlenv:

The following NEW packages will be INSTALLED:

    asn1crypto:       0.22.0-py36_0   
    attrs:            15.2.0-py36_0   
    automat:          0.5.0-py36_0    
    certifi:          2016.2.28-py36_0
    cffi:             1.10.0-py36_0   
    constantly:       15.1.0-py36_0   
    cryptography:     1.8.1-py36_0    
    cssselect:        1.0.1-py36_0    
    hyperlink:        17.1.1-py36_0   
    idna:             2.6-py36_0      
    incremental:      16.10.1-py36_0  
    libffi:           3.2.1-1         
    libiconv:         1.14-0          
    libxml2:          2.9.4-0         
    libxslt:          1.1.29-0        
    lxml:             3.8.0-py36_0    
    openssl:          1.0.2l-0        
    packaging:        16.8-py36_0     
    parsel:           1.2.0-py36_0    
    pip:              9.0.1-py36_1    
    pyasn1:           0.2.3-py36_0    
    pyasn1-modules:   0.0.8-py36_0    
    pycparser:        2.18-py36_0     
    pydispatcher:     2.0.5-py36_0    
    pyopenssl:        17.0.0-py36_0   
    pyparsing:        2.2.0-py36_0    
    python:           3.6.2-0         
    queuelib:         1.4.2-py36_0    
    readline:         6.2-2           
    scrapy:           1.3.3-py36_0    
    service_identity: 17.0.0-py36_0   
    setuptools:       36.4.0-py36_1   
    six:              1.10.0-py36_0   
    sqlite:           3.13.0-0        
    tk:               8.5.18-0        
    twisted:          17.5.0-py36_0   
    w3lib:            1.17.0-py36_0   
    wheel:            0.29.0-py36_0   
    xz:               5.2.3-0         
    zlib:             1.2.11-0        
    zope:             1.0-py36_0      
    zope.interface:   4.4.2-py36_0    

Proceed ([y]/n)? y

openssl-1.0.2l 100% |################################| Time: 0:00:00   4.73 MB/s
xz-5.2.3-0.tar 100% |################################| Time: 0:00:00   5.17 MB/s
zlib-1.2.11-0. 100% |################################| Time: 0:00:00   1.99 MB/s
python-3.6.2-0 100% |################################| Time: 0:00:04   3.54 MB/s
asn1crypto-0.2 100% |################################| Time: 0:00:00   4.76 MB/s
attrs-15.2.0-p 100% |################################| Time: 0:00:00   1.42 MB/s
certifi-2016.2 100% |################################| Time: 0:00:00   5.70 MB/s
constantly-15. 100% |################################| Time: 0:00:00   9.55 MB/s
cssselect-1.0. 100% |################################| Time: 0:00:00   4.22 MB/s
hyperlink-17.1 100% |################################| Time: 0:00:00   7.42 MB/s
idna-2.6-py36_ 100% |################################| Time: 0:00:00   2.97 MB/s
incremental-16 100% |################################| Time: 0:00:00  14.57 MB/s
libxslt-1.1.29 100% |################################| Time: 0:00:00   2.50 MB/s
pyasn1-0.2.3-p 100% |################################| Time: 0:00:00   4.03 MB/s
pycparser-2.18 100% |################################| Time: 0:00:00   4.82 MB/s
pydispatcher-2 100% |################################| Time: 0:00:00  10.21 MB/s
pyparsing-2.2. 100% |################################| Time: 0:00:00   3.49 MB/s
queuelib-1.4.2 100% |################################| Time: 0:00:00   4.75 MB/s
six-1.10.0-py3 100% |################################| Time: 0:00:00   6.07 MB/s
zope-1.0-py36_ 100% |################################| Time: 0:00:00   2.69 MB/s
automat-0.5.0- 100% |################################| Time: 0:00:00   2.14 MB/s
cffi-1.10.0-py 100% |################################| Time: 0:00:00   3.02 MB/s
lxml-3.8.0-py3 100% |################################| Time: 0:00:01   3.06 MB/s
packaging-16.8 100% |################################| Time: 0:00:00   3.58 MB/s
pyasn1-modules 100% |################################| Time: 0:00:00   3.15 MB/s
setuptools-36. 100% |################################| Time: 0:00:00   2.48 MB/s
w3lib-1.17.0-p 100% |################################| Time: 0:00:00   5.67 MB/s
zope.interface 100% |################################| Time: 0:00:00   1.72 MB/s
cryptography-1 100% |################################| Time: 0:00:00   2.81 MB/s
parsel-1.2.0-p 100% |################################| Time: 0:00:00   9.65 MB/s
twisted-17.5.0 100% |################################| Time: 0:00:01   3.22 MB/s
pyopenssl-17.0 100% |################################| Time: 0:00:00   5.19 MB/s
service_identi 100% |################################| Time: 0:00:00  10.27 MB/s
scrapy-1.3.3-p 100% |################################| Time: 0:00:00   4.57 MB/s
(crawlenv) [eduuser@dn01 ~]$ 
(crawlenv) [eduuser@dn01 ~]$ scrapy version
Scrapy 1.3.3
(crawlenv) [eduuser@dn01 ~]$ scrapy shell http://www.j123.co.kr/search01/auction_result.asp
2018-04-19 01:48:42 [scrapy.utils.log] INFO: Scrapy 1.3.3 started (bot: scrapybot)
2018-04-19 01:48:42 [scrapy.utils.log] INFO: Overridden settings: {'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0}
2018-04-19 01:48:42 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole']
2018-04-19 01:48:42 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-04-19 01:48:42 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-04-19 01:48:42 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-04-19 01:48:42 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-04-19 01:48:42 [scrapy.core.engine] INFO: Spider opened
2018-04-19 01:48:42 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.j123.co.kr/search01/auction_result.asp> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x7ffd2f1ea198>
[s]   item       {}
[s]   request    <GET http://www.j123.co.kr/search01/auction_result.asp>
[s]   response   <200 http://www.j123.co.kr/search01/auction_result.asp>
[s]   settings   <scrapy.settings.Settings object at 0x7ffd2d731a90>
[s]   spider     <DefaultSpider 'default' at 0x7ffd2d4c6710>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> quit()
(crawlenv) [eduuser@dn01 ~]$ 
(crawlenv) [eduuser@dn01 ~]$ 
(crawlenv) [eduuser@dn01 ~]$ conda install ipython
Fetching package metadata .........
Solving package specifications: .

Package plan for installation in environment /home/eduuser/anaconda3/envs/crawlenv:

The following NEW packages will be INSTALLED:

    decorator:        4.1.2-py36_0 
    ipython:          6.1.0-py36_0 
    ipython_genutils: 0.2.0-py36_0 
    jedi:             0.10.2-py36_2
    path.py:          10.3.1-py36_0
    pexpect:          4.2.1-py36_0 
    pickleshare:      0.7.4-py36_0 
    prompt_toolkit:   1.0.15-py36_0
    ptyprocess:       0.5.2-py36_0 
    pygments:         2.2.0-py36_0 
    simplegeneric:    0.8.1-py36_1 
    traitlets:        4.3.2-py36_0 
    wcwidth:          0.1.7-py36_0 

Proceed ([y]/n)? y

decorator-4.1. 100% |###################################################################################################################################| Time: 0:00:00   9.69 MB/s
ipython_genuti 100% |###################################################################################################################################| Time: 0:00:00  11.92 MB/s
jedi-0.10.2-py 100% |###################################################################################################################################| Time: 0:00:00  14.93 MB/s
path.py-10.3.1 100% |###################################################################################################################################| Time: 0:00:00  17.78 MB/s
ptyprocess-0.5 100% |###################################################################################################################################| Time: 0:00:00  26.05 MB/s
pygments-2.2.0 100% |###################################################################################################################################| Time: 0:00:00   8.81 MB/s
simplegeneric- 100% |###################################################################################################################################| Time: 0:00:00   7.41 MB/s
wcwidth-0.1.7- 100% |###################################################################################################################################| Time: 0:00:00  13.67 MB/s
pexpect-4.2.1- 100% |###################################################################################################################################| Time: 0:00:00   7.37 MB/s
pickleshare-0. 100% |###################################################################################################################################| Time: 0:00:00   8.90 MB/s
prompt_toolkit 100% |###################################################################################################################################| Time: 0:00:00   5.73 MB/s
traitlets-4.3. 100% |###################################################################################################################################| Time: 0:00:00   2.83 MB/s
ipython-6.1.0- 100% |###################################################################################################################################| Time: 0:00:00   2.97 MB/s
(crawlenv) [eduuser@dn01 ~]$ 

~~~

### Scrapy 생성
```bash
> scrapy startproject crawler
> tree
> cd crawler
> cd spiders
> scrapy genspider woori www.j123.co.kr # 추가 생성시
```

### Scrapy Shell 간당 사용법

```
(crawlerenv) D:\edu-project\datatech4>scrapy shell http://www.j123.co.kr/search01/auction_result.asp
2018-04-19 10:24:48 [scrapy.utils.log] INFO: Scrapy 1.5.0 started (bot: scrapybot)
2018-04-19 10:24:48 [scrapy.utils.log] INFO: Versions: lxml 4.2.1.0, libxml2 2.9.8, cssselect 1.0.3, parsel 1.4.0, w3lib 1.19.0,Twisted 17.5.0, Python 3.5.5 |Anaconda, Inc.| (default, Apr  7 2018, 04:52:34) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 17.5.0 (OpenSSL 1.0.2o  27 Mar 2018), cryptography 2.2.2, Platform Windows-10-10.0.16299-SP0
2018-04-19 10:24:48 [scrapy.crawler] INFO: Overridden settings: {'LOGSTATS_INTERVAL': 0, 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter'}
2018-04-19 10:24:48 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.corestats.CoreStats']
2018-04-19 10:24:49 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2018-04-19 10:24:49 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2018-04-19 10:24:49 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-04-19 10:24:49 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6024
2018-04-19 10:24:49 [scrapy.core.engine] INFO: Spider opened
2018-04-19 10:24:49 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.j123.co.kr/search01/auction_result.asp> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x0000022F6D309128>
[s]   item       {}
[s]   request    <GET http://www.j123.co.kr/search01/auction_result.asp>
[s]   response   <200 http://www.j123.co.kr/search01/auction_result.asp>
[s]   settings   <scrapy.settings.Settings object at 0x0000022F70FA4D30>
[s]   spider     <DefaultSpider 'default' at 0x22f711bf978>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
In [1]: from scrapy.http import FormRequest, TextResponse

In [2]: fd = {'resBubwon':'0201',
   ...: 'resGae':'05',
   ...: 'resSerStartdate':'20180305',
   ...: 'resSerEnddate':'',
   ...: 'resChgPage':'1',
   ...: 'nowPge':'1',
   ...: 'resSort2':''}

In [3]: r = FormRequest(url='http://www.j123.co.kr/search01/auction_Result.asp',formdata=fd)

In [4]: fetch(r)
2018-04-19 10:25:23 [scrapy.core.engine] DEBUG: Crawled (200) <POST http://www.j123.co.kr/search01/auction_Result.asp> (referer: None)

In [5]: view(response)
Out[5]: True

In [6]: doc = response.xpath('//tr[contains(@bgcolor, "#ffffff")]')

In [7]: doc
Out[7]:
[<Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>,
 <Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>,
 <Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>,
 <Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>,
 <Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>,
 <Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>,
 <Selector xpath='//tr[contains(@bgcolor, "#ffffff")]' data='<tr onmouseout="this.style.backgroundCol'>]

In [8]: sel = Selector(text=doc.extract_first())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-7b546e369182> in <module>()
----> 1 sel = Selector(text=doc.extract_first())

NameError: name 'Selector' is not defined

In [9]: from scrapy.selector import Selector

In [10]: sel = Selector(text=doc.extract_first())

In [11]: tr = Selector(text=doc.extract_first())

In [12]: td = tr.xpath('//td')

In [13]: cell =Selector(text=td[2].extract().replace('\r\n','').replace('\t',''))

In [14]: itemType = cell.xpath('//b//text()').extract_first()

In [15]: itemType
Out[15]: '상가(점포)'

In [16]:%save -r woori 1-9999
```

### Scrapy 실행

```bash
$ scrapy crawl caucayear --set FEED_URI=output_2013.json -s FEED_FORMAT=json --set YEAR=2013 --logfile scrapy.log
```
