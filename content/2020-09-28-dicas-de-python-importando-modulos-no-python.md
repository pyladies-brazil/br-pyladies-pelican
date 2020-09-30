Title: Dicas de Python: Importando módulos no Python
Slug: importando-modulos-no-python
Date: 2020-09-28 21:28:08
Tags: dicas, import, módulos
Author: danielle8farias
Comments: true



Você já se perguntou o que são os **imports** que muitas vezes vemos no começo do código?

É ele quem torna visível os **módulos** para o arquivo no qual foi chamado.

# O que são módulos?

Segundo a [documentação oficial](https://docs.python.org/pt-br/3/tutorial/modules.html) 
> um módulo é um arquivo contendo definições e instruções Python. [...] Um módulo pode conter tanto instruções executáveis quanto definições de funções e classes. Essas instruções servem para inicializar o módulo. Eles são executados somente na primeira vez que o módulo é encontrado em uma instrução de importação. 

De maneira resumida: um módulo é um trecho de código pronto que pode ser invocado quando for preciso utilizar algum método já implementado dele.

Para ilustrar, vamos imaginar que exista no Python um **módulo de verduras e leguminosas** chamado de **vegetais** como na imagem abaixo:

![vegetais]({filename}/images/vegetable.jpg)

Se usarmos o comando:

```
import vegetais
```

O Python nos trará todos os vegetais mostrado. Como se colocássemos todos sobre a mesa para que durante o preparo, pudéssemos pegá-los de imediato. Porém ao usarmos o comando:

```
from vegetais import batata
```

O Python nos trará apenas a batata. Como se colocássemos sobre a mesa apenas a batata e mais nenhum outro vegetal. Sendo assim nos sobra mais espaço na mesa para outras funções.

## Usando o import

Usando um exemplo com Python, vamos importar o módulo [**math**](https://docs.python.org/pt-br/3/library/math.html?highlight=math#module-math), que é um módulo que nos dá acesso a várias funções matemáticas, como raiz quadrada, seno, arredondamentos, etc. 

O módulo **math** é um dos módulos conhecidos como *built in* (pronto para uso); ou seja, podemos usá-lo sem instalar nenhuma dependência externa, uma vez que fazem parte da biblioteca padrão do Python. Outros exemplos de módulos da biblioteca padrão são [os](https://docs.python.org/pt-br/3/library/os.html) (responsável por funções de sistema operacional) e [re](https://docs.python.org/pt-br/3/library/re.html) (expressões regulares).

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

O asterisco é conhecido como **referência global** e indica que todas as funções do módulo **math** serão trazidas.

Para trazer apenas uma função dentro de um módulo, fazemos:

``` py
>>> from math import sqrt
>>> sqrt(25)
5.0
```

Esse modo é útil quando queremos encurtar a chamada de uma determinada função.

## Importando várias funções

Podemos também importar várias funções específicas sem precisar trazer todo o módulo. Assim:

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
