FROM zohoanalytics/onprem
RUN mkdir -p /home/zoap/Zoho/Analytics/MyBackup &&\
    cd /home/Zoho/Analytics/bin && \
    sh app_ctl.sh run &
VOLUME /home/zoap/zoho/analytics/backup
EXPOSE 8443