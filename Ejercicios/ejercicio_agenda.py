def agenda():
    
    agenda_dict = {}
    
    def create_contact():
        phone = input("ingresa número del contacto: ")
        if phone.isdigit() and (len(phone)>0 and len(phone)<=10):
            agenda_dict[name]= phone
        else:
            print('El número es incorrecto')
            
    while True:
        print(
        """
        
        1.Busca el contacto 
        2.Inserta el contacto
        3.Actualiza el contacto
        4.Elimina el contacto
        5.Mostrar contactos
        6.Salir
        
        """
        )
        opción = input("Elija un opción del 1 al 6: ")
        
        match opción:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda_dict:
                    print(f'el contacto es {name} ')
                else:
                    print('no existe el contacto')
            case "2":
                name = input("ingresa nombre del contacto: ")
                create_contact()
                print(f'Contacto {name} con el {agenda_dict[name]} fue guardado')
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda_dict:
                    create_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda_dict:
                    del agenda_dict[name]
            case "5":
                print('Contactos')
                for key, value in agenda_dict.items():
                    print(f'{key}: {value}')
            case "6":
                print('Saliendo de la agenda')
                break
            case _:
                print('Elige una opción que se muestra')
                
agenda()