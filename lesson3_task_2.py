def pers_data(name, family, year, city, e_mail, tlf):
    print(f'name - {name}, last name - {family}, year of birth - {year}, '
          f'city of residence - {city}, email - {e_mail}, phone number - {tlf}')


name_1 = str(input('Enter your first name -  '))
family_1 = str(input('Enter your last name -  '))
year_1 = str(input('Enter your year of birth -  '))
city_1 = str(input('Enter your city of residence -  '))
e_mail_1 = str(input('Enter your e-mail -  '))
tlf_1 = str(input('Enter your phone number -  '))
pers_data(name=name_1, family=family_1, year=year_1, city=city_1, e_mail=e_mail_1,
          tlf=tlf_1)
