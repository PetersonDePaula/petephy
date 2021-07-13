#!/usr/bin/env python
# coding: utf-8

# In[4]:


horario = int(input('Qual horario é agora? '))

#Acabei de aprender como registrar um comentário
#Laço de repetição irá executar enquanto o horário for maior que zero e menor que seis.
#Caso a condição seja satisfeita o algorítimo irá repetir que horário está na madrugada até que este seja maior que seis.

while 0 < horario < 6:
    print('Você está no horario da madrugada')
    horario = horario + 1
else:
    print('Você nao está no horario da madrugada')


# In[10]:


#O algorítimo vai imprimir o número de pipocas informado de maneira decrescente enquanto for maior que zero.

num_pipocas = int(input('Digite o numero de pipocas: '))

while num_pipocas > 0:
    print('O numero de pipocas é: ', num_pipocas)
    num_pipocas = num_pipocas - 1
else:
    print("Não tem pipoca!Bora comprar mais!")


# In[11]:


# O algorítimo só sai do loop quando o usuário digitar a senha correta:

resposta = input('Informe sua senha: ')
while resposta != '102030':
    resposta = input('SENHA INVÁLIDA! TENTE NOVAMENTE ')
else:
    print("BEM VINDO, MESTRE.")


# In[12]:


nome_paises = ['Brasil','Canadá','Ítalia','Japão']
print(nome_paises)


# In[13]:


print('Tamanho da lista: ', len(nome_paises))


# In[14]:


print('Japão: ', nome_paises(4))


# In[15]:


print('Japão: ', nome_paises[4])


# In[16]:


nome_paises = ['Brasil','Canadá','Ítalia','Japão']
print('Quarto país é o:', nome_paises[4])


# In[17]:


nome_paises = ['Brasil','Canadá','Ítalia','Japão']
print('Quarto país é o:', nome_paises[3])


# In[18]:


print('Primeiro país é o: HUEHUE', nome_paises[0])


# In[19]:


#Slice remove o último elemento informado, no caso o elemento da posição 3.
print(nome_paises[0:3])


# In[20]:


print(nome_paises[1:])


# In[21]:


print (nome_paises[::2])


# In[23]:


print(nome_paises[::-1])


# In[32]:


champions = []
champions.append('Ahri')
champions.append('Ashe')
champions.append('Dr.Mundo')
champions.append('Master Yi')
champions.append('Annie & Chimbres')

print(champions)


# In[ ]:




