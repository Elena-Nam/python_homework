import traceback

try:
    with open('diary.txt', 'a') as file: 
        first_prompt = True 
        while True:
            if first_prompt:
                entry = input("What happened today? ")
                first_prompt = False
            else:
                entry = input("What else? ")

            file.write(entry + "\n")  

            if entry.lower() == "done for now":
                break  

except Exception as e:
    print('An exception occurred:', e)

    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
     

