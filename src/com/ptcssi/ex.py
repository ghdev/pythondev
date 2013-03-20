'''
Created on 2013-3-13

@author: yangao
'''

name = 'Jay'
country_dict = {'dan':'us', 'tim':'us', 'rupa':'in', 'shrek':'cn', 'mirek':'pl', 'jay':'cn'}

def square(n):
    try:return int(n ** 2)
    except:return 'oops!' 
    
def get_country_by_member_name(first_name):
    try: return country_dict[str(first_name).lower()]
    except: return 'Sorry, not found!'

print square(3)
print square(2.5)
print square(name)

print get_country_by_member_name('jAy')
