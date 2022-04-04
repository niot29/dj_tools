from multiprocessing import context
import subprocess
from .models import sslSiteModel


def listModel():
    data = sslSiteModel.objects.values_list('id','ssl_site')
    print (data.id)
    for da in sslSiteModel.objects.values_list():
        print (da.id)

def run_sslcheckModule():
    url_check = "status.python.org"
    
    
    # output as bytes
    output = subprocess.run(["sslcheck",url_check], capture_output=True)
    
    # Convert output utf-8
    output_str = output.stdout.decode('utf-8')
    print(output_str)
    print("---------------")
    listModel()
    
    
            
#if __name__ == '__main__':
#     run_sslcheckModule(url_check)
#     listModel()