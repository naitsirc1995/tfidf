from config import config
from preprocessing.preprocess import pre_procesor


def main():
    text = "Hello. from the NICE LAND of hypoCraticussss ! "
    element = config('/home/cristian/Documents/nlp-project/data-preprocessing/configs/example.yaml')
    
    print(pre_procesor(text,element['preprocesing']))



if __name__ == '__main__':
    main()