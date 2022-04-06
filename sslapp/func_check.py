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
        output_str = output.stdout.decode('utf-8')
        #print(len(output_str))
        print(output_str)
        #print(type(output_str))
        
        # search for expire date
        search_string = 'expire on'
        #print (output_str.find(search_string,100,500))
        i = len(search_string) + output_str.find(search_string,100,500) + 1
        x = i + 10
        s_date = ''
        while i < x:
           # print (output_str[i])
            s_date = s_date + output_str[i] 
            i += 1
        
        print (s_date)
        
        s_status = 0
        if "is ok" in output_str:
            s_status = 1

        #Save to DB
        sslSiteModel.objects.filter(pk=url_req.id).update(ssl_status=s_status)
        sslSiteModel.objects.filter(pk=url_req.id).update(ssl_cert_info=output_str)
            
#if __name__ == '__main__':
#     run_sslcheckModule(url_check)
#     listModel()