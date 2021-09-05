import speedtest
from datetime import datetime
import os

def network_test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res['download'], res['upload'], res['ping']

def main():
    now = datetime.now()

    runs = int(input('How many times would you like the test to run? '))
    with open(os.path.join(os.pardir, 'data.txt'), 'a') as f:
        for i in range(runs):
            print('Running test', i + 1)
            d, u, p = network_test()
            dt_string = now.strftime('%d/%m/%Y %H:%M:%S')

            f.write('Network test #{0} at {1}\n'.format(i + 1, dt_string))
            f.write('Download: {:.2f} Mb/s\n'.format((d / 1024) / 1000))
            f.write('Upload: {:.2f} Mb/s\n'.format((u / 1024) / 1000))
            f.write('Ping: {}\n'.format(p))      

            print('Network Test #{0} at {1}'.format(i+1, dt_string))
            print('Download: {:.2f} Mb/s'.format((d / 1024) / 1000))
            print('Upload: {:.2f} Mb/s'.format((u / 1024) / 1000))
            print('Ping: {}\n'.format(p))
    input('Press enter to exit')

if __name__ == '__main__':
    main()