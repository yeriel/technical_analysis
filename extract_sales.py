import time 
import pandas as pd

from utilities.api import auth_api, refresh, get_sales

if __name__ == '__main__':

    df_sales = pd.DataFrame(columns=['id_client','id', 
                                    'product ','place_purchase',
                                    'gross_price','net_price',
                                    'timestamp'])

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

    print(f'Extract all sales')
    
    count_page = 1
    while True:
        if int(time.time() - time_seccion ) > 55:
            print(f'New token')
            res = refresh(f'{path_base}/api/v1/auth/token/refresh',refresh_token)
            access_token = res['access']
            time_seccion = time.time()

        res = get_sales(f'{path_base}/api/v1/sales?page={count_page}&per_page=100', access_token)
        
        data_ = {
            'id_client':[value for client in res['data'] for key, value in client.items() if key == 'cliente'], 
            'id':[value for client in res['data'] for key, value in client.items() if key == 'id'],
            'product':[value for client in res['data'] for key, value in client.items() if key == 'producto'],
            'place_purchase':[value for client in res['data'] for key, value in client.items() if key == 'lugar_compra'],
            'gross_price':[value for client in res['data'] for key, value in client.items() if key == 'precio_bruto'],
            'net_price':[value for client in res['data'] for key, value in client.items() if key == 'precio_neto'],
            'timestamp':[value for client in res['data'] for key, value in client.items() if key == 'timestamp']
            }

        df_sales = pd.concat([df_sales, pd.DataFrame(data_)])
        print(f'{count_page}\n{res}\n------------')
        
        count_page +=1
        if res['meta']['page'] == res['meta']['total_pages']:
            print(f'Done')
            break

    print(f'Save data in csv file')
    df_sales.to_csv('dataset/sales.csv',index=False)  
