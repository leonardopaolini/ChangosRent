from .validation_constants import *

vehicle_type_error_messages = {
            'name': {
                'required': 'El nombre es requerido',
                'max_length': f'La longitud del nombre no puede superar los {CHAR_GENERAL_MAX_LENGTH} caracteres'
            },
            'type_of_uses': {
                'required': 'El tipo de uso es requerido',
                'max_length': f'La longitud del tipo de uso no puede superar los {CHAR_GENERAL_MAX_LENGTH} caracteres'
            },
            'km_per_maintenance': {
                'invalid': 'Por favor introduzca una cantidad de km válida',
                'min_value': f'La cantidad de km no puede ser menor a {KM_PER_MAINTENANCE_MIN_VALUE}',
                'max_value': f'La cantidad de km no puede superar los {KM_PER_MAINTENANCE_MAX_VALUE}'
            },
            'price': {
                'invalid': 'Por favor introduzca un precio válido',
                'min_value': f'El precio no puede ser de menor a {NUMBER_MIN_VALUE}',
                'max_value': f'El precio no puede ser mayor a {PRICE_MAX_VALUE}',
            }
        }

rent_error_messages = {
            'start_date': {
                'required': 'Por favor ingrese la fecha de inicio del alquiler'
            },
            'end_date': {
                'required': 'Por favor ingrese la finalización de inicio del alquiler'
            },
            'payment_method': {
                'required': 'Por favor ingrese la forma de pago del alquiler'
            },
            'vehicles': {
                'required': 'Por favor seleccione el / los vehiculos que desea alquilar'
            }
        }

vehicle_error_messages = {
            'brand': {
                'required': 'Por favor introduzca la marca del vehículo',
                'max_length': 'La marca del vehículo no puede superar los 255 caracteres',
            },
            'model': {
                'required': 'Por favor introduzca el modelo del vehículo',
                'max_length': 'El modelo del vehículo no puede superar los 255 caracteres',
            },
            'year': {
                'required': 'El año del vehículo es requerido',
                'invalid': 'El año del vehiculo es inválido',
                'min_value': f'El año no puede ser menor a {YEAR_MIN_VALUE}',
                'max_value': f'El año no puede ser mayor a {YEAR_MAX_VALUE}',
            },
            'buy_date': {
                'required': 'Por favor introduzca la fecha de compra del vehículo'
            }
        }

customer_error_messages = {
            'address': {
                    'required': 'La dirección es requerida',
                    'invalid': 'El dirección es inválida',
                    'max_length': f'El dirección no puede tener más de {CHAR_GENERAL_MAX_LENGTH} caracteres'
                },
            'email': {
                    'required': 'El email es requerido',
                    'invalid': 'El email es inválido',
                    'max_length': f'El email no puede tener más de {CHAR_GENERAL_MAX_LENGTH} caracteres'
                },
            'user': {
                    'required': 'El nombre de usuario es requerido',
                    'min_length': f'El nombre de usuario debe contener al menos {USER_MIN_LENGTH} caracteres',
                    'max_length': f'El nombre de usuario debe contener como máximo {USER_MAX_LENGTH} caracteres',
            },
            'password': {
                'required': 'La contraseña es requerida',
                'min_length': f'La contraseña debe contener al menos {PASSWORD_MIN_LENGTH} caracteres',
                'max_length': f'La contraseña debe contener como máximo {PASSWORD_MAX_LENGTH} caracteres',
            }
        }

company_error_messages = {
            'business_name': {
                'required': 'El nombre de la compañía es requerido',
                'max_length': f'El nombre de la compañía no puede superar los {CHAR_GENERAL_MAX_LENGTH} caracteres',
            },
            'business_type': {
                'required': 'El tipo de negocio es requerido',
                'max_length': f'El tipo de negocio no debe superar los {CHAR_GENERAL_MAX_LENGTH} caracteres',
            },
            'business_id': {
                'required': 'El id de la compañía es requerido',
                'invalid': 'El id de la compañía no es válido',
                'min_value': f'El id de la compañía no puede ser menor a {COMPANY_ID_MIN_VALUE}',
                'max_value': f'El id de la compañía no puede ser de mayor a {COMPANY_ID_MAX_VALUE}',
            }
        }

person_error_messages = {
            'fist_name': {
                'required': 'El nombre de la persona es requerido',
                'max_length': f'El nombre de la persona no puede superar los {CHAR_GENERAL_MAX_LENGTH} caracteres',
            },
            'last_name': {
                'required': 'El apellido de la persona es requerido',
                'max_length': f'El nombre de la persona no puede superar los {CHAR_GENERAL_MAX_LENGTH} caracteres',
            },
            'birth_date': {
                'required': 'La fecha de nacimiento de la persona es requerida',
            },
            'person_id': {
                'required': 'El id de la persona es requerido',
                'invalid': 'El id de la persona no es válido',
                'min_value': f'El id de la persona no puede ser de menor a {PERSON_ID_MIN_VALUE}',
                'max_value': f'El id de la persona no puede ser de mayor a {PERSON_ID_MAX_VALUE}'
            }
        }

person_error_messages.update(customer_error_messages)
company_error_messages.update(customer_error_messages)

