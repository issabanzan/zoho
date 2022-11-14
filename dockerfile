FROM zohoanalytics/onprem
RUN mkdir -p /home/zoap/Zoho/Analytics/MyBackup &&\
    cd /home/Zoho/Analytics/bin && \
    sh app_ctl.sh run &
VOLUME /home/zoap/zoho/analytics/backup
EXPOSE 8080

RUN touch ${LOG_FILE} && touch ${EXECUTE_LOG} && chmod ugo-x ${LOG_FILE} && chmod ugo-x ${EXECUTE_LOG}
RUN chmod +x ${PROJ_DIR}/greeter_client.py
RUN chmod +x ${PROJ_DIR}/server_client.py