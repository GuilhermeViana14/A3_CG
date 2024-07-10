from PIL import Image, ImageEnhance
import os
import matplotlib.pyplot as plt

# Função para aplicar ajuste combinado de saturação e contraste
def aplicar_ajustes(image):
    enhancer = ImageEnhance.Color(image)
    enhanced_image = enhancer.enhance(1.5)  
    
    enhancer = ImageEnhance.Contrast(enhanced_image)
    enhanced_image = enhancer.enhance(1.5)  
    
    return enhanced_image

# Função para salvar a imagem resultante
def salvar_imagem(image, output_dir, filename):
    output_path = os.path.join(output_dir, filename)
    image.save(output_path)
    print(f'Imagem salva em: {output_path}')
    
# Função para colocar as imagens e seus histogramas
def colocar_imagem_historiograma(original_image, enhanced_image, filename):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # colocar imagem original
    axes[0, 0].imshow(original_image)
    axes[0, 0].set_title(f'{filename} - Original')
    axes[0, 0].axis('off')

    # colocar histograma da imagem original
    historiograma(original_image, axes[0, 1], f'{filename} - Original')

    # colocar imagem modificada
    axes[1, 0].imshow(enhanced_image)
    axes[1, 0].set_title(f'{filename} - Modificada')
    axes[1, 0].axis('off')

    # colocar histograma da imagem modificada
    historiograma(enhanced_image, axes[1, 1], f'{filename} - Modificada')

    plt.tight_layout()
    plt.show()


# Função para colocar o histograma de uma imagem em um eixo específico
def historiograma(image, ax, title):
    ax.set_title(title)
    ax.set_xlabel('Valor de Pixel')
    ax.set_ylabel('Frequência')
    
    # Converter a imagem para RGB
    image = image.convert('RGB')
    
    # Obter os dados de pixel
    pixels = list(image.getdata())
    
    # Separar os canais de cor
    red_channel = [pixel[0] for pixel in pixels]
    green_channel = [pixel[1] for pixel in pixels]
    blue_channel = [pixel[2] for pixel in pixels]
    
    # colocar histogramas para cada canal
    ax.hist(red_channel, bins=256, color='red', alpha=0.5, label='Vermelho')
    ax.hist(green_channel, bins=256, color='green', alpha=0.5, label='Verde')
    ax.hist(blue_channel, bins=256, color='blue', alpha=0.5, label='Azul')
    
    ax.legend()

# Função para aplicar filtros de ajuste de cor (saturação e contraste combinados) em várias imagens
def aplicar_filtro(input_image_paths, output_dir):
    # Criar diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterar sobre todas as imagens de entrada
    for image_path in input_image_paths:
        # Abrir a imagem
        image = Image.open(image_path)
        
        # Aplicar filtros combinados de ajuste de cor
        enhanced_image = aplicar_ajustes(image)
        
        # Salvar a imagem resultante
        filename = os.path.basename(image_path)
        salvar_imagem(enhanced_image, output_dir, filename)
        
        # Plotar as imagens e seus histogramas
        colocar_imagem_historiograma(image, enhanced_image, filename)



# Lista de caminhos das imagens do campus Fapa
input_image_paths = [
    'input_images/imagem_1.jpg',  
    'input_images/Imagem_2.jpg',
    'input_images/imagem_3.jpg',
    'input_images/imagem_4.jpg',
    'input_images/imagem_5.jpg',
    'input_images/imagem_6.jpg',
    'input_images/imagem_7.jpg',
    'input_images/imagem_8.jpg',
    'input_images/imagem_9.jpg',
    'input_images/imagem_10.jpg',
    
]

output_directory = 'output_images'  

aplicar_filtro(input_image_paths, output_directory)
