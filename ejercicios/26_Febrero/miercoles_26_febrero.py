#!/usr/bin/env python
# coding: utf-8

# # Inicio del Web Scraping

# Trabajando con la web de muevete

# In[5]:


import requests


# In[6]:


url = 'http://mueveteformacion.com/'


# In[7]:


url


# In[8]:


muevete = requests.get(url)


# In[9]:


muevete.status_code


# In[10]:


print(muevete.text)


# In[11]:


muevete.headers


# In[12]:


muevete.request.headers


# In[13]:


muevete.request.method


# In[14]:


muevete.request.url


# # PARSEAR

# In[15]:


from bs4 import BeautifulSoup


# In[16]:


soup = BeautifulSoup(muevete.text, 'lxml')


# In[17]:


print(soup.prettify)


# In[18]:


soup.find('ul', attrs={'id': 'main'})


# In[19]:


soup.find('ul', attrs={'id': 'menu-main-menu'})


# In[20]:


menuWeb = soup.find('ul', attrs={'id': 'menu-main-menu'}).find_all('li')


# In[21]:


menuWeb = soup.find('ul', attrs={'id': 'menu-main-menu'}).find_all('li')
menuWeb


# In[22]:


link = menuWeb[0] #* Si queremos cambiar el index 0 a index 1 por ejemplo, arriab hay un panel de Run, parar, volver, damos a volver y despues run de nuevo
link


# In[23]:


link.a


# In[24]:


link.find('a') #Es lo mismo que el anterior.


# In[25]:


link.a.get('href') # HREF de la etiqueta <a> que encontramos


# In[26]:


link.a.get_text() # Contenido de la etiqueta <a> que encontramos


# In[27]:


links = [link.a.get('href') for link in menuWeb] #* Conseguir todos los enlaces de todos los <a> encontrados.
links


# In[28]:


linksG = [link.a for link in menuWeb]
linksG


# In[31]:


# diccLinks = {}

# for i in linksG:
#     diccLinks[i.get_text()] = i.a.get('href') #* NO RESULTO :/


# In[33]:


enlaces = {link.a.get_text():link.a.get('href') for link in menuWeb}
enlaces


# # FUNCIÓN
# Recoger todos los links de las noticias/eventos de la página relacionada. Creando una función para ese uso.

# In[34]:


#* Prueba Try- Except
#* Try-except, por si no encuetra la información.
try:
    link.a.get('href')
except:
    pass


# In[48]:


def noticiasLinks(etiquetaGeneral, etiqueta, valorAtributo, etiquetaEspecifica):
    
    menuWeb = soup.find(etiquetaGeneral, attrs={etiqueta: valorAtributo}).find_all(etiquetaEspecifica)
    
    diccNoticias = {link.get_text():link.get('href') for link in menuWeb}
    
    return diccNoticias

noticiasLinks('div', 'id', 'main', 'a')


# In[42]:


menuWeb2 = soup.find('div', attrs={'id': 'main'}).find_all('a')
menuWeb2


# In[47]:


diccNoticias = {link.get_text():link.get('href') for link in menuWeb2}
diccNoticias


# In[ ]:




