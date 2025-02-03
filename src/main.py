
# This imports the marimo code and makes it available 
# for building external services or apps
from marimoapp_script import calculate

# Alternative: Import everything
#   from marimoapp_script import *
# Problem: Cerebrium throws a warning during deployment:
# 'from marimoapp import *' used; unable to detect undefined names
# This can be ignored


def run(param_1: str, run_id):  # run_id is optional, injected by Cerebrium at runtime
    result_1 = calculate(666)

    my_status_code = 200 # if you want to return a specific status code

    my_results = {"1": param_1, "2": result_1}

    return {"my_result": my_results, "status_code": my_status_code} 



if __name__ == "__main__":
    print("Starting...")
    result = run('hello', 'xxx')
    print(result)