# Banco de Imagens

| Critérios | Pts. |
|---|---|
| Alteração no .env no nome do diretório | 0.5 | 
| Ao executar, criar o diretório a ser utilizado para os arquivos. | 0.5 |
| Download como zip de qualquer tipo de arquivo enquanto o diretório estiver vazio. Retorna mensagem de erro (caso necessário) com status 404. | 1 |
| Download de um arquivo que ainda não existe. Retorna mensagem de erro (caso necessário) com status 404. | 1 |
| Upload de arquivo menor que 1MB dentre os tipos: PNG, JPG, GIF. Salva arquivo no diretório configurado e retorna o nome do arquivo com o status 201. | 2 |
| GET /files. Lista todos os arquivos com status 200.  | 1 |
| GET /files/\<extension>. Lista todos os arquivos de uma extensão especifica com status 200. | 1 |
| Upload de arquivos de outros formatos. Mensagem de erro (caso necessário) com status 415. | 2 |
| Upload de imagens maiores que 1MB. Mensagem de erro (caso necessário) com status 413. | 2 |
| Upload de arquivo com nome já existente. Mensagem de erro (caso necessário) com status 409. | 2 |
| Download de um arquivo existente. Faz o download do arquivo com código 200. | 1 |
| GET /download-zip?file_extension=png&compression_ratio=1. Download de arquivo zip contendo todos os arquivos da extensão selecionada. Status 200. | 2 |
| Análise do código (organização dos módulos e pacotes, boas práticas). | 2 |
| Arquivos **requirements.txt**, **.env**, **.env.example** e **.gitignore** (**venv** e **.env** adicionados) | 1 |
| Arquivos **.env** e **.env.example** presentes na aplicação | 1 |