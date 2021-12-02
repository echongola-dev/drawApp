# drawApp

Kivy é uma ferramenta GUI independente de plataforma em Python. Como pode ser executado em Android, IOS, Linux e Windows, etc. É basicamente utilizado para desenvolver a aplicação Android, mas não significa que não possa ser utilizado em aplicações Desktop.
Antes de começar com o Kivy, é necessário um conhecimento básico dos fundamentos da programação Python. Agora, vamos começar com a instalação.
  Como fiz a instalação? Vejamos os passos abaixo.
  
  Se você tiver várias versões do Python instaladas em seu computador, terá que instalar o Kivy na versão que deseja usar para o desenvolvimento.
Supondo que o Python esteja instalado, considere as seguintes etapas:

1.	Os pacotes Python podem ser instalados usando pip. Como Kivy precisa de compilação ao instalar com pip, portanto, precisamos de wheels, que é uma distribuição pré-construída de um pacote já compilado. Você também pode usar o git para instalar o Kivy, mas neste tutorial, usaremos a wheel.

Execute o seguinte comando no prompt de comando para instalar o pip e a wheel:

# python -m pip install --upgrade pip wheel setuptools

2. Agora temos que instalar as dependências. Execute os seguintes comandos:
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
Depois:

# python -m pip install kivy.deps.gstreamer

3. Depois de instalar as dependências do Kivy, instale o Kivy usando o seguinte comando:
python –m pip install kivy


Apos concluir essa primeira parte de instalação da ferramenta na nossa mauina passamos para a fase seguinte.

Kivy GUI
Nesta seção, você aprenderá como criar e executar um programa Kivy e como construir uma interface básica no Kivy.
Vamos criar um arquivo com a extensão .py para criarmos a interface Kivy.

Por padrão, o Kivy tenta carregar o arquivo Kv com o mesmo nome da sua classe, mas sem a palavra App e em letras minúsculas.
Se sua classe for TestApp, ele irá procurar um arquivo Kv com o nome test.kv no mesmo diretório para carregar widgets a partir dele. 

E corremos o arquivo .py. e o resultado esta na multimedia abaixo:
