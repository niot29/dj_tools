from multiprocessing import context
import subprocess
from .models import sslSiteModel


def listModel():
    data = sslSiteModel.objects.all()
    
    for da in data:
        print (da.ssl_site)

def run_sslcheckModule():
    url_check = "status.python.org"
    data = sslSiteModel.objects.all()
    
    for url_req in data:
        
        # output as bytes
        output = subprocess.run(["sslcheck",url_req.ssl_site], capture_output=True)
        
        # Convert output utf-8
        #output_str = output.stdout.decode('utf-8')
        print(output)
        print(type(output))
        
        #Save to DB
        sslSiteModel.objects.filter(pk=url_req.id).update(ssl_cert_info=output)
            
#if __name__ == '__main__':
#     run_sslcheckModule(url_check)
#     listModel()