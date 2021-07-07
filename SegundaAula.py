#!/usr/bin/env python
# coding: utf-8

# In[1]:


idade = input("Informe a sua idade: ")
print(idade, type(idade))


# In[2]:


idade = input("Informe sua idade: ")
x = int(idade) + 1
print(x)


# In[3]:


salario_mensal = input("Digite o seu salário: ")
salario_mensal = float(salario_mensal)

gasto_mensal = input("Digite o seu gasto mensal: ")
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print("O montante que você pode economizar é: ", montante_economizado)


# In[6]:


valor_pacoca = 10

preco_pacoca = input("Moço, quanto tá a paçoca!? 3 paçocas!?")

if float(preco_pacoca) <= 10:
    print("Passa pra cá!")


# In[11]:


valor_pacoca = 10

preco_pacoca = input("Moço, quanto tá a paçoca!? 3 paçocas!?")

if float(preco_pacoca) <= 10:
    print("Passa pra cá, uai! *u*")
elif float(preco_pacoca) <= 15:
    print("Vish, deixa para amanhã. ^^''")
else:
    print("Tem diamante nessa paçoca? Tá doido! O_O")
   


# In[ ]:





# In[18]:


pele_media = 3

gols_pele = input("Quantos gols o Pelé marcou hoje?")

if float(gols_pele) >= 3:
    print("Homem é bom mesmo hein!?")
elif float(gols_pele) <= 1:
    print("OXI, se não fez gol, não jogou!")
else:
    print("Menos que isso nem comemoro!")      


# In[ ]:





# In[ ]:




