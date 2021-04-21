import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC593afd9a9b7d914c381f2829703aa73b"
# Your Auth Token from twilio.com/console
auth_token = "7919b3fe9d6206a52fbc63b2c828ae4a"
client = Client(account_sid, auth_token)

#Step by Step of solution
#Open 6 files in Excel

list_month= ['janeiro','fevereiro','março','abril','maio','junho']

for mes in list_month:

    table_sales = pd.read_excel(f'{mes}.xlsx')

    if (table_sales['Vendas'] > 55000).any():
        vendedor= table_sales.loc[table_sales['Vendas'] > 55000,'Vendedor'].values[0]
        vendas= table_sales.loc[table_sales['Vendas'] > 55000,'Vendas'].values[0]
        print(f'Month {mes} find someone reach the goal. Salesman: {vendedor}, Sales: {vendas} ')
        message = client.messages.create(
            to="+xxx",
            from_="+xxx",
            body=f'Month {mes} find someone reach the goal. Salesman: {vendedor}, Sales: {vendas} ')
        print(message.sid)


# For each file:
    #Verify if any file in collumn Sale is > 55.000


# If >55.000 ---> Send a Sms with the name , and month and sales of salesman
# If less that 55.000 don't do nothing







