# Rebanador de correo electronico con python
email = input('Entregue su correo: ').strip()
username = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
format_ = (f'Tu nombre de usuario es: "{username}" y tu dominio es "{domain_name}"')
print(format_)