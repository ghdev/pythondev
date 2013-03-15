'''
Created on 2013-3-13

@author: yangao
'''

name = 'Jay'
country_dict = {'dan':'us', 'tim':'us','rupa':'in','shrek':'cn','mirek':'pl','jay':'cn'}

def square(n):
    try:print int(n**2)
    except:print'oops!' 
    
def get_country_by_member_name(first_name):
    try: return country_dict[str(first_name).lower()]
    except: return 'Sorry, not found!'

square(3)
square(2.5)
square(name)

print get_country_by_member_name('jAy')
