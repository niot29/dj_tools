import subprocess
import json


    
#url_check = "status.python.org"

def run_sslcheckModule(url_check):
    # output as bytes
    output = subprocess.run(["sslcheck",url_check], capture_output=True)
    
    # Convert output utf-8
    output_str = output.stdout.decode('utf-8')
    print(output_str)
    
    
    
            
#if __name__ == '__main__':
#     run_sslcheckModule(url_check)