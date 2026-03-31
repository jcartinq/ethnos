# coding=utf-8
import zipfile
import xml.etree.ElementTree as ET
import os
import shutil

def extract_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        text = []
        for paragraph in tree.iterfind('.//w:p', namespace):
            para_text = []
            for run in paragraph.iterfind('.//w:t', namespace):
                if run.text:
                    para_text.append(run.text)
            if para_text:
                text.append(''.join(para_text))
        return '\n'.join(text)
    except Exception as e:
        return f"Error reading {docx_path}: {e}"

if __name__ == "__main__":
    source_dir = r"C:\Users\uned\Desktop\consultorias\Clientes\Demoscopia\FOCIAS FA"
    proj_dir = r"C:\Users\uned\Desktop\ETHNOS\04_Ecosistema_Cualitativo\00_Proyectos\FOCIAS_FA"
    
    # Files to process
    corpus_file = os.path.join(source_dir, "martes mujeres.docx")
    context_file = os.path.join(source_dir, "Análisis Comparativo Centro-Periferia Electoral 19 de dic rev.docx")
    
    out_corpus = os.path.join(proj_dir, "01_Corpus_RAW", "martes_mujeres_transcripcion.txt")
    out_context = os.path.join(proj_dir, "02_Contexto_Local", "analisis_centro_periferia_contexto.txt")
    
    with open(out_corpus, 'w', encoding='utf-8') as f:
        f.write(extract_text(corpus_file))
        
    with open(out_context, 'w', encoding='utf-8') as f:
        f.write(extract_text(context_file))
    
    print("Extracción completada con éxito.")
