import time 
import pandas as pd

from utilities.api import auth_api, refresh, get_clients

if __name__ == '__main__':

    df_clients = pd.DataFrame(columns=['id','view_web'])

    path_base = 'https://cf-prueba-tecnica.herokuapp.com'
    data = {
        'email':'yeriel.pruebatecnica@comunidadfeliz.com',
        'password':'suerte_yeriel!!'
    }

    print(f'Auth api')
    data = auth_api(f'{path_base}/api/v1/auth/login',data)

    time_seccion = time.time()
    access_token = data['user']['access']
    refresh_token = data['user']['refresh']

    print(f'Extract all clients')
    
    count_page = 1
    while True:
        if int(time.time() - time_seccion ) > 55:
            print(f'New token')
            res = refresh(f'{path_base}/api/v1/auth/token/refresh',refresh_token)
            access_token = res['access']
            time_seccion = time.time()

        res = get_clients(f'{path_base}/api/v1/clients?page={count_page}', access_token)
        
        data_ = {
            'id':[value for client in res['data'] for key, value in client.items() if key == 'id'], 
            'view_web':[value for client in res['data'] for key, value in client.items() if key == 'visitas_web']
            }

        df_clients = pd.concat([df_clients, pd.DataFrame(data_)])
        print(f'{count_page}\n{res}\n------------')
        
        count_page +=1
        if res['meta']['page'] == res['meta']['total_pages']:
            print(f'Done')
            break

    print(f'Save data in csv file')
    df_clients.to_csv('dataset/clients.csv',index=False)  
