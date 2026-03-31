# coding=utf-8
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

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
    base_dir = r"C:\Users\uned\Desktop\ETHNOS"
    out_dir = os.path.join(base_dir, "txt_exports")
    os.makedirs(out_dir, exist_ok=True)
    
    files_to_process = [
        r"00_Gobernanza\ETHNOS_RACI_Operativo_v1.0.docx",
        r"00_Gobernanza\ETHNOS_ActaInicioOperativa_v1.0.docx",
        r"01_Metodologia_y_Protocolos\metodología para construir proyectos con metacognición simulada.docx",
        r"01_Metodologia_y_Protocolos\ETHNOS_ProtocolosAnaliticosAvanzados_v1.0.docx",
        r"02_Master_y_Entregables\ETHNOS total.docx"
    ]
    
    for rel_path in files_to_process:
        abs_path = os.path.join(base_dir, rel_path)
        if os.path.exists(abs_path):
            text = extract_text(abs_path)
            basename = os.path.basename(abs_path)
            out_file = os.path.join(out_dir, basename.replace('.docx', '.txt'))
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Exported: {out_file}")
        else:
            print(f"File not found: {abs_path}")
