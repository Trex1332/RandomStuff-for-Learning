from time import sleep
from datetime import datetime
 
def main(): 
    time = datetime.now()
    ct = time.strftime('%H:%M:%S')
    print(ct)
    sleep(1)
    main()
main()