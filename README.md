# Scraper do site Aprender.unb.br

Baixa todos os arquivos que foram postados no moodle.

## Requerimentos:    

    ```
        pip3 intall -r requerimentos.txt
    ```

## Antes de executar:     
    
Crie um arquivo credenciais.json na mesma pasta com o seguinte formato:  

```
{
"cpf":"cpf",
"senha":"senha"
}
```

## Executar
```
python3 moodle.py
```

## Informações gerais:

Acessa o conteúdo HTML, analisa os dados. Como HTML é organizado por camadas
 não é possível extrair os dados por processamento ou busca de strings. 
 Então se faz uma navegação no código, cria-se uma árvore de estrutura para extração de dados dos arquivos HTML e XML, e uma busca linear do elemento(arquivo) desejado.

 ## Pseudo-código 

```
# Linear search works in any array.
#
# T(n): O(n)
#

def linear_search(array, query):
    for i in range(len(array)):
        if array[i] == query:
            return i

    return -1
```

### Fork
forked from wagneralbjr/Scrapper-Aprender

