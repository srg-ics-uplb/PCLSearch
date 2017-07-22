#based from https://www.elastic.co/blog/how-to-make-a-dockerfile-for-elasticsearch
#make sure that "vm.max_map_count=262144" is set in /etc/sysctl.conf on host machine

FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

RUN apt-get install curl -y

RUN apt-get install -y --no-install-recommends software-properties-common && add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    (echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections) && \
    apt-get install --no-install-recommends -y oracle-java8-installer && \
    rm -rf /var/cache/oracle-jdk8-installer && \
    echo "networkaddress.cache.ttl=60" >> /usr/lib/jvm/java-8-oracle/jre/lib/security/java.security && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

#RUN echo "permission javax.management.MBeanTrustPermission 'register';" >> $JAVA_HOME/jre/lib/security/java.policy

RUN groupadd -g 1000 elasticsearch && useradd elasticsearch -u 1000 -g 1000

RUN mkdir -p /opt/dev/elasticsearch 

RUN chown -R elasticsearch.elasticsearch /opt

USER elasticsearch

WORKDIR /opt/dev/elasticsearch

RUN curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.0.tar.gz

RUN tar -xvf elasticsearch-5.5.0.tar.gz

ENV PATH=$PATH:/opt/dev/elasticsearch/elasticsearch-5.5.0/bin

COPY logging.yml /opt/dev/elasticsearch/elasticsearch-5.5.0/config/

COPY elasticsearch.yml /opt/dev/elasticsearch/elasticsearch-5.5.0/config/

CMD ["elasticsearch"]

EXPOSE 9200 9300
