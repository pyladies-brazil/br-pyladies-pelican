Title: Dicas de Python: Importando módulos no Python
Slug: importando-modulos-no-python
Date: 2020-09-28 21:28:08
Tags: dicas, import, módulos
Author: danielle8farias
Comments: true



## O que são módulos?

De maneira resumida: um módulo é um trecho de código pronto que pode ser invocado quando for preciso utilizar algum método dele.

Para ilustrar, vamos imaginar que exista no Python um **módulo de verduras e leguminosas** chamado de **vegetais** como na imagem abaixo:

![vegetais]({filename}/images/vegetable.jpg)

Se usarmos o comando:

```
import vegetais
```

O Python nos trará todos os vegetais mostrado. Como se colocássemos todos sobre a mesa para que durante o preparo, pudéssemos pegá-los de imediato.

Porém ao usarmos o comando:

```
from vegetais import batata
```

O Python nos trará apenas a batata. Como se colocássemos sobre a mesa apenas a batata e mais nenhum outro vegetal. Sendo assim nos sobra mais espaço na mesa para outras funções.

## Usando o import

Usando um exemplo com Python, vamos importar o módulo **math**. Que é um módulo que nos dá acesso a várias funções matemáticas, como raiz quadrada, seno, arredondamentos, etc. 

> você sempre pode consultar a [documentação do Python](https://docs.python.org/3/library/math.html) para saber mais sobre o módulo math e outros.

O módulo **math** é um dos módulos conhecidos como *built in* (pronto para uso); basta apenas chamá-lo.

Nesse exemplo, vamos calcular a raiz quadrada do número 25.

Assim temos:

```py
>>> import math
>>> math.sqrt(25)
5.0
```

Isso quer dizer que importamos todo o módulo **math** e em seguida, apontamos a função **sqrt** que calcula a raiz quadrada do argumento passado entre parênteses.

Outra maneira de fazer essa mesma ação:

``` py
>>> from math import *
>>> sqrt(25)
5.0
```

O asterisco é conhecido como **referência global** e indica que todas as funções do módulo **math** serão trazidos.

Para trazer apenas uma função dentro de um módulo, fazemos:

``` py
>>> from math import sqrt
>>> sqrt(25)
5.0
```

Esse modo é útil quando queremos encurtar a chamada de uma determinada função.

## Import várias funções

Podemos também importar várias funções sem precisar trazer todo o módulo. Assim:

```py
>>> from math import radians, sin, cos, tan
>>> sin(radians(30))
0.49999999999999994
>>>
>>> cos(radians(60))
0.5000000000000001
>>>
>>> tan(radians(45))
0.9999999999999999
```

Acima estamos trazendo apenas as funções que calculam o radiano, seno, cosseno e tangente do módulo **math**.

## Um "apelido" para sua função

Também é possível dar um novo nome para a função de um módulo. Exemplo:

```py
>>> from math import sqrt as raiz
>>> raiz(81)
9.0
```

Acima, demos a nossa função **sqrt** o nome de **raiz** e podemos invocá-la assim durante o nosso programa.

Até a próxima dica! o/
