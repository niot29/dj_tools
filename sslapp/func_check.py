import subprocess


    
url_check = "google.com"

def run_sslcheckModule(url_check):
    output = subprocess.run(["sslcheck",url_check], capture_output=True)
    print(output.stdout)
    print(type(output.stdout))
    new_str = output.stdout.decode('utf-8')
    print(new_str)

if __name__ == '__main__':
     run_sslcheckModule(url_check)