~~~
[esadmin@dn01 node1]$ bin/elasticsearch &
[1] 6617
[esadmin@dn01 node1]$ [2018-04-19T04:17:22,879][INFO ][o.e.n.Node               ] [node1] initializing ...
[2018-04-19T04:17:22,997][INFO ][o.e.e.NodeEnvironment    ] [node1] using [1] data paths, mounts [[/ (rootfs)]], net usable_space [267.6gb], net total_space [286.4gb], types [rootfs]
[2018-04-19T04:17:22,998][INFO ][o.e.e.NodeEnvironment    ] [node1] heap size [989.8mb], compressed ordinary object pointers [true]
[2018-04-19T04:17:22,999][INFO ][o.e.n.Node               ] [node1] node name [node1], node ID [nzbRg5W1RFCqjCGN7nxtFw]
[2018-04-19T04:17:22,999][INFO ][o.e.n.Node               ] [node1] version[6.2.3], pid[6617], build[c59ff00/2018-03-13T10:06:29.741383Z], OS[Linux/3.10.0-123.el7.x86_64/amd64], JVM[Oracle Corporation/OpenJDK 64-Bit Server VM/1.8.0_161/25.161-b14]
[2018-04-19T04:17:22,999][INFO ][o.e.n.Node               ] [node1] JVM arguments [-Xms1g, -Xmx1g, -XX:+UseConcMarkSweepGC, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Djava.io.tmpdir=/tmp/elasticsearch.UG8Hvqmx, -XX:+HeapDumpOnOutOfMemoryError, -XX:+PrintGCDetails, -XX:+PrintGCDateStamps, -XX:+PrintTenuringDistribution, -XX:+PrintGCApplicationStoppedTime, -Xloggc:logs/gc.log, -XX:+UseGCLogFileRotation, -XX:NumberOfGCLogFiles=32, -XX:GCLogFileSize=64m, -Des.path.home=/home/esadmin/node1, -Des.path.conf=/home/esadmin/node1/config]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [aggs-matrix-stats]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [analysis-common]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [ingest-common]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [lang-expression]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [lang-mustache]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [lang-painless]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [mapper-extras]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [parent-join]
[2018-04-19T04:17:23,650][INFO ][o.e.p.PluginsService     ] [node1] loaded module [percolator]
[2018-04-19T04:17:23,651][INFO ][o.e.p.PluginsService     ] [node1] loaded module [rank-eval]
[2018-04-19T04:17:23,651][INFO ][o.e.p.PluginsService     ] [node1] loaded module [reindex]
[2018-04-19T04:17:23,651][INFO ][o.e.p.PluginsService     ] [node1] loaded module [repository-url]
[2018-04-19T04:17:23,651][INFO ][o.e.p.PluginsService     ] [node1] loaded module [transport-netty4]
[2018-04-19T04:17:23,651][INFO ][o.e.p.PluginsService     ] [node1] loaded module [tribe]
[2018-04-19T04:17:23,651][INFO ][o.e.p.PluginsService     ] [node1] no plugins loaded
[2018-04-19T04:17:25,573][INFO ][o.e.d.DiscoveryModule    ] [node1] using discovery type [zen]
[2018-04-19T04:17:26,065][INFO ][o.e.n.Node               ] [node1] initialized
[2018-04-19T04:17:26,066][INFO ][o.e.n.Node               ] [node1] starting ...
[2018-04-19T04:17:26,190][INFO ][o.e.t.TransportService   ] [node1] publish_address {192.168.131.56:9300}, bound_addresses {[::]:9300}
[2018-04-19T04:17:26,199][INFO ][o.e.b.BootstrapChecks    ] [node1] bound or publishing to a non-loopback address, enforcing bootstrap checks
ERROR: [1] bootstrap checks failed
[1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
[2018-04-19T04:17:26,207][INFO ][o.e.n.Node               ] [node1] stopping ...
[2018-04-19T04:17:26,234][INFO ][o.e.n.Node               ] [node1] stopped
[2018-04-19T04:17:26,234][INFO ][o.e.n.Node               ] [node1] closing ...
[2018-04-19T04:17:26,252][INFO ][o.e.n.Node               ] [node1] closed
~~~
