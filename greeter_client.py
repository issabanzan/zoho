mport os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

def get_script_logs():
    logs = ""; execute_log = ""
    if os.path.isfile('script_log.log'):
        with open('./script_log.log', 'r') as log_file:
            logs = log_file.read()
    else:
        logs = "Aucun log n'existe pour le script principal [NO_SCRIPT_LOGS]"
    if os.path.isfile('execute_log.log'):
        with open('./execute_log.log', 'r') as execute_log_file:
            execute_log = execute_log_file.read()
    else:
        execute_log = "Aucun log n'existe concernant l'execution du script principal [NO_EXECUTE_LOGS]"
    return [execute_log, logs]

def get_current_cron_status():
    cron_tab = os.popen('crontab -l').read()
    if 'python3 /app/index.py >> /app/script_log.log 2>&1' in cron_tab:
        return [True, "Le CRON est actif", cron_tab]
    else:
        return [False, "Le CRON est inactif ou n'est pas programmé", ""]

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200, "OK")
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
   
        
def run(port):
    server_class=HTTPServer
    handler_class=Server
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Web service is running on port : %s ...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(port=8080)
   
