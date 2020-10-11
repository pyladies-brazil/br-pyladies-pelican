Title: Dicas de Python: Mostrando mensagens na tela
Slug: imprimindo-mensagem-na-tela
Date: 2020-10-11 13:06:08
Tags: dicas, print, função
Author: danielle8farias
Comments: true


Você já se perguntou como o Python mostra ao usuário uma **mensagem** na tela?

Ele faz isso através de uma **função** chamada **print**.

Essa função é invocada da seguinte maneira:

```py
>>> print()

```

Ela retorna na tela (ou outro dispositivo de saída usado) uma **string**, ou qualquer outro **objeto** que será convertido em string antes.

No exemplo, acima, como não passamos nenhum **argumento** para a **função**, tivemos apenas como retorno uma quebra de linha (pulou para a próxima linha).


## Imprimindo uma mensagem simples

Se quisermos apenas imprimir uma mensagem, basta digitá-la entre **aspas (simples ou duplas)**; desse modo:

```py
>>> print('Bem-vinda à Pyladies') #iniciar e terminar a string com o mesmo tipo de aspas
Bem-vinda à Pyladies
```

Como podemos ver, a mensagem aparece exatamente como foi digitada.

Se quisermos usar aspas (para fazer uma citação, por exemplo) dentro da string, fazemos do seguinte modo:

```py
>>> print('"Somos poeira de estrelas", disse o astrônomo Carl Sagan.')
"Somos poeira de estrelas", disse o astrônomo Carl Sagan.
```

Para o uso de aspas duplas, iniciamos a string com aspas simples.

```py
>>> print("don't let me down")
don't let me down
```

E para o uso de aspas simples, iniciamos a string com aspas duplas.

Também é possível imprimir uma mensagem através de variáveis; assim:

```py
>>> x = 'Pyladies Brasil' #atribuindo à variável x uma string
>>> print(x)
Pyladies Brasil
```

Nesse caso, não se faz necessário o uso de aspas (simples ou duplas) dentro da função.

```py
>>> ano = 2020 #atribuindo um número inteiro à variável ano
>>> print(ano)
2020
>>> 
>>> print('Estamos no ano de', ano) #a variável ano será convertida para string antes de aparecer na tela
Estamos no ano de 2020
```


## Usando o separador

É possível também imprimir mais de uma string:

```py
>>> print('Olha para o', 'céu, meu amor!')
Olha para o céu, meu amor!
```

Ao usar a vírgula para separar as strings, o Python acrescentará um espaço entre elas no momento do retorno. Por isso não temos a saída:

```
Olha para océu, meu amor!
```

Isso acontece porque o **separador** padrão do Python é o **espaço**. Entretanto podemos modificá-lo. Desse modo:

```py
>>> print('Pois paz sem voz.', 'Não é paz', 'é medo!', sep=' - ')
Pois paz sem voz. - Não é paz - é medo!
```

No exemplo acima, estamos usando o separador **espaço, traço, espaço**.

```py
>>> print('Se', 'eu', 'me', 'tornar', 'menos', 'faminto', 'e', 'curioso', sep='*')
Se*eu*me*tornar*menos*faminto*e*curioso
```

Aqui estamos usando como **separador** apenas o **asterisco**.

É possível usar diversos caracteres ou combinações desses como separador.


## Finalizando o print

Quando usamos a função print em sequência, num script Python, temos:

[entrada]:

```py
print('Respirar o amor')
print('aspirando liberdade')
```

[saída]:

```py
Respirar o amor
aspirando liberdade
```

Ao final da primeira chamada da função houve uma **quebra de linha** e então a chamada da segunda.

Isso acontece porque, por padrão, o Python usa como finalização da função print os caracteres **'\n'**  que indicam a quebra de linha. Mas também é possível modificar isso:

[entrada]:

```py
print('Respirar o amor', end=' ') #usando espaço para finalização da função
print('aspirando liberdade')
```

[saída]:

```py
Respirar o amor aspirando liberdade
```

Desse modo, após a primeira chamada da função não ocorreu a quebra de linha e a saída se deu na mesma linha.

[entrada]:

```py
print('Lista de frutas:', end='\n * ')
print('Pêssego', end='\n * ')
print('Morango', end='\n * ')
print('Limão')
```

[saída]:

```py
Lista de frutas:
 * Pêssego
 * Morango
 * Limão
```

No exemplo acima usamos vários caracteres para finalizar a função (quebra de linha, espaço, asterisco e espaço novamente). Perceba que eles foram executados em sequência.


## Imprimindo x vezes

Também é possível repetir, a string de retorno da função print, por um número determinado de vezes. Assim:

```py
>>> print('-'*42)
------------------------------------------
```

No exemplo acima temos o traço repetido por 42 vezes antes de haver a quebra de linha da função; formando assim uma linha pontilhada.


A função print possui ainda outros recursos (aguarde os próximos episódios). Aqui eu mostrei alguns e você pode, inclusive, fazer combinações entre eles.

Nos vemos na próxima dica! o/
