FROM debian

USER ITPlanet

ENV MyName "ITPlanet"

RUN export Name="ITPlanet"

COPY ITPlanet.txt /home/user/

RUN apt-get update && apt-get install -y apache2 mc htop net-tools nfs-common

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]