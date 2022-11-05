FROM zohoanalytics/onprem
RUN mkdir -p /home/zoap/Zoho/Analytics/Backup &&\
    cd /home/Zoho/Analytics/bin && \
    sh app_ctl.sh run &
VOLUME /home/zoap/zoho/analytics/backup
EXPOSE 8443
firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 4 -i docker0 -j ACCEPT
firewall-cmd --reload
systemctl restart docker