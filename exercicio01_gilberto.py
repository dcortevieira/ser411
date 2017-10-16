#encoding: utf-8

#carregando as bibloiotecas
import sys 
import os #biblioteca OS fornece funcionalidades associadas ao sistema operacional
import numpy as np #biblioteca NumPy é utilizada na criação de matrizes

try:
    from osgeo import gdal, ogr, osr
except:
    sys.exit("Erro: a biblioteca GDAL não foi encontrada!") #biblioteca GDAl e seus módulos: raster, vetorial, sistema de referencia espacial
    
from utils import * #carrega as rotinas auxiliares que encontram-se definidasna mesma pasta deste programa

#configurações da biblioteca GDAL
gdal.UseExceptions()
ogr.UseExceptions()
osr.UseExceptions()

#definindo as constantes globais do programa para se facilitar futuras modificações no programa
vector_file = r"C:/Users/Denis/Desktop/PDI_AV/Aula_02/focos/focos-2016.shp"
vector_file_base_name = os.path.basename(vector_file)
layer_name = os.path.splitext(vector_file_base_name)[0]

spatial_extent = {'xmin': -89.975, 'ymin': -59.975, 'xmax': -29.975, 'ymax': 10.025}
spatial_resolution = {'x': 0.05, 'y': 0.05}
grid_dimensions = {'cols': 1200, 'rows': 1400}

file_format = "GTiff"
output_file_folder = r"C:/Users/Denis/Desktop/PDI_AV/Aula_02/focos/"

#abrir arquivo shp com focos de queimada
shp_focos = ogr.Open(vector_file)
if shp_focos is None:
    sys.exit("Erro: não foi possível abrir o arquivo '{0}'.".format(vector_file))
    
#recupera a camada de informações com os focos
layer_focos = shp_focos.GetLayer(layer_name)
if layer_focos is None:
    sys.exit("Erro: não foi possível acessar a camada '{0}' no arquivo'{1}'!".format(layer_name, vector_file)) 



#consultando satelite e mês em vector_file
satelites = {'TERRA_M-M', 'TERRA_M-T', 'AQUA_M-T', 'AQUA_M-M'} #define os satélites a serem buscados em vector file
for satelite in satelites:
    for mes in range(1, 13):
        if mes < 9:
            busca = "satelite = '{0}'and timestamp > '2016/0{1}'and timestamp < '2016/0{2}'".format(satelite, mes, mes + 1)
        elif mes == 9:
            busca = "satelite = '{0}' and timestamp > '2016/0{1}' and timestamp < '2016/{2}'".format(satelite, mes, mes + 1)
        else:
            busca = "satelite = '{0}' and timestamp > '2016/{1}' and timestamp < '2016/{2}'".format(satelite, mes, mes + 1) #definições de busca por satelite e mes

        # realiza a busca na tabela de atributos segundo as definições de busca

        layer_focos.SetAttributeFilter(busca)

        # realiza a contagem e printa o numero de focos
        contagem_focos = layer_focos.GetFeatureCount()
        print("Satélite: {0}, mês: {1}/2016, nº de focos de incêndio: {2}.".format(satelite, mes, contagem_focos))
        #print: #Satélite: TERRA_M-T, mês: 1/2016, nº de focos de incêndio: 3466.
                #Satélite: TERRA_M-T, mês: 2/2016, nº de focos de incêndio: 4123.
                #Satélite: TERRA_M-T, mês: 3/2016, nº de focos de incêndio: 4021.
                #Satélite: TERRA_M-T, mês: 4/2016, nº de focos de incêndio: 5253.
                #Satélite: TERRA_M-T, mês: 5/2016, nº de focos de incêndio: 3403.
                #Satélite: TERRA_M-T, mês: 6/2016, nº de focos de incêndio: 3490.
                #Satélite: TERRA_M-T, mês: 7/2016, nº de focos de incêndio: 7184.
                #Satélite: TERRA_M-T, mês: 8/2016, nº de focos de incêndio: 17765.
                #Satélite: TERRA_M-T, mês: 9/2016, nº de focos de incêndio: 21091.
                #Satélite: TERRA_M-T, mês: 10/2016, nº de focos de incêndio: 13692.
                #Satélite: TERRA_M-T, mês: 11/2016, nº de focos de incêndio: 6929.
                #Satélite: TERRA_M-T, mês: 12/2016, nº de focos de incêndio: 2630.
                #Satélite: TERRA_M-M, mês: 1/2016, nº de focos de incêndio: 2960.
                #Satélite: TERRA_M-M, mês: 2/2016, nº de focos de incêndio: 786.
                #Satélite: TERRA_M-M, mês: 3/2016, nº de focos de incêndio: 2023.
                #Satélite: TERRA_M-M, mês: 4/2016, nº de focos de incêndio: 845.
                #Satélite: TERRA_M-M, mês: 5/2016, nº de focos de incêndio: 829.
                #Satélite: TERRA_M-M, mês: 6/2016, nº de focos de incêndio: 1510.
                #Satélite: TERRA_M-M, mês: 7/2016, nº de focos de incêndio: 3976.
                #Satélite: TERRA_M-M, mês: 8/2016, nº de focos de incêndio: 10797.
                #Satélite: TERRA_M-M, mês: 9/2016, nº de focos de incêndio: 12683.
                #Satélite: TERRA_M-M, mês: 10/2016, nº de focos de incêndio: 7320.
                #Satélite: TERRA_M-M, mês: 11/2016, nº de focos de incêndio: 4836.
                #Satélite: TERRA_M-M, mês: 12/2016, nº de focos de incêndio: 1948.
                #Satélite: AQUA_M-M, mês: 1/2016, nº de focos de incêndio: 1277.
                #Satélite: AQUA_M-M, mês: 2/2016, nº de focos de incêndio: 553.
                #Satélite: AQUA_M-M, mês: 3/2016, nº de focos de incêndio: 862.
                #Satélite: AQUA_M-M, mês: 4/2016, nº de focos de incêndio: 338.
                #Satélite: AQUA_M-M, mês: 5/2016, nº de focos de incêndio: 273.
                #Satélite: AQUA_M-M, mês: 6/2016, nº de focos de incêndio: 529.
                #Satélite: AQUA_M-M, mês: 7/2016, nº de focos de incêndio: 1545.
                #Satélite: AQUA_M-M, mês: 8/2016, nº de focos de incêndio: 4592.
                #Satélite: AQUA_M-M, mês: 9/2016, nº de focos de incêndio: 4896.
                #Satélite: AQUA_M-M, mês: 10/2016, nº de focos de incêndio: 2235.
                #Satélite: AQUA_M-M, mês: 11/2016, nº de focos de incêndio: 1172.
                #Satélite: AQUA_M-M, mês: 12/2016, nº de focos de incêndio: 575.
                #Satélite: AQUA_M-T, mês: 1/2016, nº de focos de incêndio: 5982.
                #Satélite: AQUA_M-T, mês: 2/2016, nº de focos de incêndio: 4148.
                #Satélite: AQUA_M-T, mês: 3/2016, nº de focos de incêndio: 3797.
                #Satélite: AQUA_M-T, mês: 4/2016, nº de focos de incêndio: 3977.
                #Satélite: AQUA_M-T, mês: 5/2016, nº de focos de incêndio: 3570.
                #Satélite: AQUA_M-T, mês: 6/2016, nº de focos de incêndio: 6340.
                #Satélite: AQUA_M-T, mês: 7/2016, nº de focos de incêndio: 19143.
                #Satélite: AQUA_M-T, mês: 8/2016, nº de focos de incêndio: 38211.
                #Satélite: AQUA_M-T, mês: 9/2016, nº de focos de incêndio: 44062.
                #Satélite: AQUA_M-T, mês: 10/2016, nº de focos de incêndio: 30222.
                #Satélite: AQUA_M-T, mês: 11/2016, nº de focos de incêndio: 20169.
                #Satélite: AQUA_M-T, mês: 12/2016, nº de focos de incêndio: 8724.
                        
        #criação de uma matriz numérica
        matriz = np.zeros((grid_dimensions['rows'], grid_dimensions['cols']), np.int16)

        #calculo do numero de focos associado a cada raster, bem como sua localização na grade
        for foco in layer_focos:
            location = foco.GetGeometryRef()
            col, row = Geo2Grid(location, grid_dimensions, spatial_resolution, spatial_extent)
            matriz[row, col] += 1
            
        #criação do raster de saida no formato GeoTiff
        driver = gdal.GetDriverByName(file_format)
        if driver is None:
            sys.exit("Erro: não foi possível identificar o driver '{0}'.".format(file_format))
        output_file_name = output_file_folder + "focos-" + satelite + "-" + str(mes) + ".tiff"
        raster = driver.Create(output_file_name, grid_dimensions['cols'], grid_dimensions['rows'], 1, gdal.GDT_UInt16)
        if raster is None:
            sys.exit("Erro: não foi possível criar o arquivo '{0}'.".format(output_file_name))
            
        raster.SetGeoTransform((spatial_extent['xmin'], spatial_resolution['x'], 0, spatial_extent['ymax'], 0, -spatial_resolution['y'])) #define os paramjetros de transformação de coordenadas
        
        #usa as informações do sistema de coordenadas espacial do layer de focos na definição da grade de saída
        srs_focos = layer_focos.GetSpatialRef()
        raster.SetProjection(srs_focos.ExportToWkt())
        
        #acessa o objeto associado a primeira banda do raster e escreve o array NumPy na banda da GDAL
        band = raster.GetRasterBand(1)
        band.WriteArray(matriz, 0, 0)
        band.FlushCache
        
        #garante que toda a estrutura do raster da GDAL foi deslocada
        raster = None
        del raster, band
            