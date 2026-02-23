#! /usr/bin/python
#pip install pandas
#pip install lxml
#pip install tabulate //nao usado markdown requer
import pandas as pd 
import xml.etree.ElementTree as ET
import os
import sys
import zipfile


def extract(filename):
        xpaths = [
        '//PARTICIPACAO-EM-PROJETO/*',
        '//PRODUCAO-BIBLIOGRAFICA/TRABALHOS-EM-EVENTOS/TRABALHO-EM-EVENTOS/DADOS-BASICOS-DO-TRABALHO',
        '//PRODUCAO-BIBLIOGRAFICA/ARTIGOS-PUBLICADOS/ARTIGO-PUBLICADO/DADOS-BASICOS-DO-ARTIGO',
        '//PRODUCAO-BIBLIOGRAFICA/ARTIGOS-ACEITOS-PARA-PUBLICACAO/ARTIGO-ACEITO-PARA-PUBLICACAO/DADOS-BASICOS-DO-ARTIGO',
        '//PRODUCAO-BIBLIOGRAFICA/LIVROS-E-CAPITULOS/LIVROS-PUBLICADOS-OU-ORGANIZADOS//DADOS-BASICOS-DO-LIVRO',
        '//PRODUCAO-BIBLIOGRAFICA/LIVROS-E-CAPITULOS/CAPITULOS-DE-LIVROS-PUBLICADOS//DADOS-BASICOS-DO-CAPITULO',
        '//PRODUCAO-BIBLIOGRAFICA/TEXTOS-EM-JORNAIS-OU-REVISTAS/TEXTO-EM-JORNAIS-OU-REVISTASD/DADOS-BASICOS-DO-TEXTO'
        '//PRODUCAO-BIBLIOGRAFICA/DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA//DADOS-BASICOS-DE-OUTRA-PRODUCAO',
        '//PRODUCAO-BIBLIOGRAFICA/DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA/PARTITURA-MUSICAL/DADOS-BASICOS-DA-PARTITURA',
        '//PRODUCAO-BIBLIOGRAFICA/DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA/PREFACIO-POSFACIO/DADOS-BASICOS-DO-PREFACIO-POSFACIO',
        '//PRODUCAO-BIBLIOGRAFICA/DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA/TRADUCAO/DADOS-BASICOS-DA-TRADUCAO',
        '//PRODUCAO-TECNICA/CULTIVAR-REGISTRADA/DADOS-BASICOS-DA-CULTIVAR',
        '//PRODUCAO-TECNICA/SOFTWARE/DADOS-BASICOS-DO-SOFTWARE',
        '//PRODUCAO-TECNICA/PATENTE/DADOS-BASICOS-DA-PATENTE',
        '//PRODUCAO-TECNICA/CULTIVAR-PROTEGIDA/DADOS-BASICOS-DA-CULTIVAR',
        '//PRODUCAO-TECNICA/DESENHO-INDUSTRIAL/DADOS-BASICOS-DO-DESENHO-INDUSTRIAL',
        '//PRODUCAO-TECNICA/MARCA/DADOS-BASICOS-DA-MARCA',
        '//PRODUCAO-TECNICA/TOPOGRAFIA-DE-CIRCUITO-INTEGRADO/DADOS-BASICOS-DA-TOPOGRAFIA-DE-CIRCUITO-INTEGRADO',
        '//PRODUCAO-TECNICA/PRODUTO-TECNOLOGICO/DADOS-BASICOS-DO-PRODUTO-TECNOLOGICO',
        '//PRODUCAO-TECNICA/PROCESSOS-OU-TECNICAS/DADOS-BASICOS-DO-PROCESSOS-OU-TECNICAS',
        '//PRODUCAO-TECNICA/TRABALHO-TECNICO/DADOS-BASICOS-DO-TRABALHO-TECNICO',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/APRESENTACAO-DE-TRABALHO/DADOS-BASICOS-DA-APRESENTACAO-DE-TRABALHO',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/CARTA-MAPA-OU-SIMILAR/DADOS-BASICOS-DE-CARTA-MAPA-OU-SIMILAR',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/CURSO-DE-CURTA-DURACAO-MINISTRADO/DADOS-BASICOS-DE-CURSOS-CURTA-DURACAO-MINISTRADO',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL/DADOS-BASICOS-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/EDITORACAO/DADOS-BASICOS-DE-EDITORACAO',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/MANUTENCAO-DE-OBRA-ARTISTICA/DADOS-BASICOS-DE-MANUTENCAO-DE-OBRA-ARTISTICA',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/MAQUETE/DADOS-BASICOS-DA-MAQUETE',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/ORGANIZACAO-DE-EVENTO/DADOS-BASICOS-DA-ORGANIZACAO-DE-EVENTO',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/PROGRAMA-DE-RADIO-OU-TV/DADOS-BASICOS-DO-PROGRAMA-DE-RADIO-OU-TV',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/RELATORIO-DE-PESQUISA/DADOS-BASICOS-DO-RELATORIO-DE-PESQUISA',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/MIDIA-SOCIAL-WEBSITE-BLOG/DADOS-BASICOS-DA-MIDIA-SOCIAL-WEBSITE-BLOG',
        '//PRODUCAO-TECNICA/DEMAIS-TIPOS-DE-PRODUCAO-TECNICA/OUTRA-PRODUCAO-TECNICA/DADOS-BASICOS-DE-OUTRA-PRODUCAO-TECNICA'
    ]
        
        path=filename
        f = open(path, 'r',encoding='iso-8859-1')
        tree = ET.parse(f)
        data_pd = []
        

        out = open(path[0:len(path)-4]+".csv",'a')
        
        child = tree.find('.//DADOS-GERAIS')
        nome_completo = child.attrib['NOME-COMPLETO']
       
        ''' confs para a saida console do pandas..nao usadas no momento
        with pd.option_context('display.max_rows', None,
                        'display.max_columns', None,
                        'display.width',None,
                        'display.precision', None,
            ):'''
        
        for i in range(len(xpaths)):
            p= xpaths[i]
            try:
                data_pd.append( pd.read_xml(path,encoding='iso-8859-1',xpath=p))
            except ValueError:
                print(p+" sem dados")
                
                

            
        out.write("Nome: {titulo}\n".format(titulo=nome_completo))
        for i in range(len(data_pd)):
            titulo = xpaths[i].replace("/",' ').replace("*",'')
            print(titulo)
            if(not data_pd[i].empty):
                print(data_pd[i])
                out.write("\n{titulo}\n\n".format(titulo=titulo))
                data_pd[i].to_csv(out,lineterminator='\n',mode='a',sep=';')


if __name__ == "__main__":
    
    dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    outdir = sys.argv[2] if len(sys.argv) > 2 else '.'


    os.chdir(dir) 
    for  i in os.listdir('.'):
        if(i.endswith('.zip') ):
            print("Processing file:", i)
            # Unzip the file
            with zipfile.ZipFile(i, 'r') as zip_ref:
                assert len(zip_ref.namelist()) == 1, "Expected exactly one file in the zip archive"
                # Extract the file from the zip archive
                ziped= zip_ref.namelist().pop()
                #print("Files in archive:", ziped)
                zip_ref.extractall('.')
            # Remove the zip file after extraction
            extract(''+ziped)
            os.remove(ziped)  # Remove the zip file after extraction

            
        if i.endswith('.xml') and not i.startswith('pd_'):
            print("Processing file:", i)
            # Call the function to extract data from the XML file
            # Assuming the XML files are in the current directory
            # and have the structure as expected by extract_dados
            extract(i)