#!/usr/bin/env python
# coding: utf-8

# In[1]:


citacao = "\"As andorinhas voltaram\""
print(citacao)


# In[2]:


empresa = "Google"
print(empresa[0],empresa[3])


# In[4]:


wod = "S.P.L.I.T"
wod = wod.split(".")   
print(wod)   


# In[6]:


clube = "cRuZEIro do suL"

print(clube.title())
print(clube.capitalize())
print(clube.lower())
print(clube.upper())


# In[8]:


mensagem = "Você viu a Nami me atrapalhando a estudar?"
citado =  "Nami" in mensagem
print(citado)


# In[10]:


gato = "Frodo"
gata = "Atena"

print(f'{gato} & {gata}')


# In[13]:


Skills = {
    'Q': 'joga magia',
    'W': 'fogo de raposa',
    'E': 'Chame',
    'R': 'Ult'
}

print(type(Skills))
print(Skills)


# In[14]:


Skills['Skin'] = 'Academia de batalha'
print(Skills)


# In[15]:


print(Skills['Q'])


# In[17]:


Skills['Q'] = 'Orbe Espiritual'
print(Skills)


# In[ ]:




