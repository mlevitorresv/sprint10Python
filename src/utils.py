from config.sql import mydb


def update_element(data, element):
    cursor = mydb.cursor()
    fields_to_modify = []
    data_to_fields = []
    
    element_modify = element.view()
    
    print(f"Element to modify:\n{element_modify}")
    choose = input(f'\n Choose field to modify (q for exit): {data} \n')
    while choose != 'q':
        data_input = input(f'\nEnter data to {data[choose]}\n')
        fields_to_modify.append(data[choose])
        data_to_fields.append(data_input)
        choose = input(f'\n Choose other field to modify (q for exit): {data} \n')

    set_clause = ','.join([f"{field} = %s" for field in fields_to_modify])
    mydb.reconnect()
    query = (f"UPDATE {element.table} SET {set_clause} WHERE id = %s")
    cursor.execute(query, data_to_fields + [element_modify[0]['id']])
    mydb.commit()
            
    return 'Update completed.'
    
    
